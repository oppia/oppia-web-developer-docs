If you are developing a new feature that hasn't been in a stable state, you may want to limit the scope of the feature so that it's only enabled when certain criteria is met (e.g. only enabled in dev environment). In these cases you can use the dynamic feature gating system to gate the enabling of the features with a feature flag.

If you have any question regarding the feature gating system, feel free to contact @MegrezZhu.

## Follow the steps below to add a new feature flag

### Creating the flag

1. Add a new unique feature flag name in the `PARAM_NAMES` enum class in `core/domain/platform_parameter_list.py`, similar to a key-value pair. Example:

```python
PARAM_NAMES = utils.create_enum(
    # ... existing names
    NEW_FEATURE = 'new_feature',
)
```

2. Create and register a feature flag instance in the same file with its name, description and stage (see the [Feature Stage](#feature-stage-explanation) section for more details). Example:

```python
Registry.create_feature_flag(
    PARAM_NAMES.NEW_FEATURE,
    'This is a newly created feature.',
    platform_parameter_domain.FeatureStages.DEV,
)
```

3. Add the name of the newly created feature to one of the feature name lists (`DEV_FEATURES_LIST`, `TEST_FEATURES_LIST`, or `PROD_FEATURES_LIST`) in `core/platform_feature_list.py` according to its stage. Note: if the name is added to the wrong list, a backend test error will raise. Example:

```python
DEV_FEATURES_LIST = [
    # ...
    params.PARAM_NAMES.NEW_FEATURE,
]
```

4. To make the feature flag available in the front-end, you need to add it into the name enum in `core/templates/domain/platform_feature/feature-status-summary.model.ts` as well:

```typescript
export enum FeatureNames {
  // ...
  NewFeature = 'new_feature',
}
```

### Modifying unit tests to account for the creation of the new flag

The following steps ensure existing unit tests account for the newly created feature flag and don't fail.

1. Add the name of the feature flag to the the `EXPECTED_PARAM_NAMES` array in the `ExistingPlatformParameterValidityTests` class. Example:

```python
EXPECTED_PARAM_NAMES = [
    # ... existing names
    'new_feature',
]
```

2. Add the newly created flag as a key-value pair in the `featureStatusSummary` object in the unit-test meant for testing the functioning of the session storage in `core/templates/services/platform-feature.service.spec.ts`, like so:

```typescript
    it('should load from sessionStorage if there are valid results.', fakeAsync(
      () => {
        // ...
        mockSessionStore({
          SAVED_FEATURE_FLAGS: JSON.stringify({
            // ...
            featureStatusSummary: {
                // ...
              [FeatureNames.NewFeature]: true,
            }
          })
        });

        // ...
      })
    );
```

## Feature Stage Explanation

Features fall in the three types of stages: dev, test and prod. In short, the stage of a feature implies its maturity & stability and the environment where it can be enabled:

- dev feature can only be enabled in dev environment.
- test feature can be enabled in dev or test environments, but it can never be enabled in production environments.
- prod feature can be enabled in any of the dev, test, production environments.

Note: The environment the flag is placed in determines the enviroment(s) where it CAN BE enabled, not where it IS enabled. A feature in `test` stage, as mentioned above, can only be enabled in the `dev` and `test` environments, and not in the `prod` environment. By default, however, it is disabled in all environments. See the [Changing Value of Feature Flags](#changing-value-of-feature-flags) section for details on how to enable/disable feature flags.

## Usage Example

### Gating in Backend

```python
from core import platform_feature_list
from core.domain import platform_feature_services

# ...

if platform_feature_services.is_feature_enabled(
    	platform_feature_list.PARAM_NAMES.dummy_feature):
    # Code of the feature
else:
    raise Exception("Not implemented.")
```

## Gating in Frontend

The status of features is loaded during the page initialization, once it's loaded you can access it through the `PlatformFeatureService`:

```typescript
// Assuming this.featureService is the PlatformFeatureService instance.
if (this.featureService.status.NewFeature.isEnabled) {
    // Code of the feature
} else {
    // ...
}
```

## Changing Value of Feature Flags

Feature flags are defaulted to `false/disabled`. To change their values, you can login as the administrator, navigate to the admin page, then to the feature tab.

In the feature tab, where you will see the feature flag you added, you can change the settings (see the [Setting of Feature Flags](#settings-of-feature-flags) section for detail) of the feature flags.

Note: since only users with admin permission can edit the settings of feature flags, you can only enable your features on your local dev instance of Oppia, while in production environment, only administrators can enable/disable features.

## Settings of Feature Flags

We use the following principles to determine the value of a feature flags:

- Each feature flag has multiple *rules*, its value changes to the value specified in the first rule that is matched. If no rule is matched, its value remains default.
- Each rule has multiple *filters*, and a rule is matched only when all of its filters are matched.
- Each filter describes a scenario. There are multiple types of filters (like `server mode` and `client type`) which can be used in combination with each other to describe various scenarios (like `server mode = dev OR server mode = test`).
- Each filter can have multiple conditions, and a filter is matched if any of the conditions specified in the rule are matched.

For example, if we want a feature flag to be enabled only in dev environments, we can configure the flag's rules/filters as shown below.

![Example feature setting](https://i.imgur.com/GnFQ7El.jpg)