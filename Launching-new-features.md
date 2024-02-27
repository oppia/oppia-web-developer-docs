When developing a new feature, you might want to limit the scope of the feature so that it's only enabled when certain criteria are met (e.g. only enabled in dev environment). In these cases, you can use the feature gating system to gate the enabling of the features with a feature flag.

## Why do we need feature flags?

Feature flags vastly improve/simplify the development process by allowing developers to safely deploy new features to production. They also allow us to quickly disable features if we find that they are causing problems in production.

They also allow us to hide features that are still in development/still being tested. This means that developers can add the feature incrementally to the codebase, and only enable it once it is fully ready for production. Should the feature break, they also allow us to easily disable it without having to remove all the changes from the codebase. This is especially useful when the feature is large and/or complex.

Additionally, feature flags allow us to decouple the feature & binary releases. This allows us to deploy new binaries to the server with less risk of regressions.


## How do you, as a developer, use feature flags?

### When to use feature flags?

Feature flags should be used when you are working on a feature whose scale makes it hard to implement all at once, or for more experimental features that are likely to cause breakages. Essentially, feature flags are a must for features that are not yet ready for production/fully-tested at the time that they're merged into develop.

### How to use feature flags?

Say you are working on a large scale user-facing feature that will take 1 or more PRs to fully implement. In such a case, please use feature flags to gate your feature appropriately by carefully following the steps listed below:

1. The very first PR you make must introduce a new feature flag to the codebase, that is meant to be used with this new feature. The feature flag should be placed in the DEV stage and disabled by default, so that it **cannot** accidentally be turned on in environments for which it is not yet ready (like the test/prod servers). Every single user-facing aspect of the feature -- whether frontend or backend -- must be gated behind the feature flag (both in the first PR, and all the following ones as well). This is to ensure that the feature is not visible to the user until it is fully implemented and ready for production.

2. The first PR above must be merged before any of the following PRs are merged. This is to ensure that the feature flag is available in the codebase for it to be used in the following PRs.

3. When developing, make sure that e2e tests are present for your feature. If the feature is gated behind a feature flag, you may need to use the [enableFeature](https://github.com/oppia/oppia/blob/c48ff1510a680666bfe891d7b2f68130d21e4dcf/core/tests/webdriverio_utils/ReleaseCoordinatorPage.js#L126) utility functions for the release-coordinator page to first enable the required flag, and then proceed to perform the testing. For unit tests, you should include tests for both the `flag=True` and `flag=False` cases.

4. The very last PR you make (to finish up the feature you are working on) must include changes that move the feature flag to the TEST stage. This is to ensure that the feature is available in the test environment, so that we can feature-test it before it is made available to the users in the production environment. **NOTE: Please test all the changes manually to make sure that the feature works fully end-to-end on your local dev server, before moving the flag to the TEST stage.**

5. When the PR is merged, fill out [this form](https://forms.gle/zDCsoN6Xb6JvQku87) to request that your feature be tested. This form will be processed by the server admins team, who will work with you and the feature testers to set a date during which your feature will be available to use on one of our test servers. (We can only surface the feature for a limited time because the servers are also needed for other things, such as release testing.) Once the testing date is confirmed, the server admin will make a deployment, turn the feature flag on, and send instructions to the feature testers for how to test the feature. Feature testers will use this [feature review template](https://docs.google.com/document/d/1ibQC9t1jnOg-o1lrHEM3QEXeF4eSqAiPhs2lD2iCpy4/edit) to conduct the testing.

6. If the feature testing reveals that the feature is not yet ready for production, you must work on fixing the highlighted issues before proceeding further. You can request a re-test once all the testing feedback is addressed.

7. Once you receive a go-ahead from the feature testers, you must merge another PR. This PR should do only one thing, i.e. move the feature flag to the PROD stage, allowing it to be enabled/disabled in production (by the release coordinator(s)). **NOTE: When opening this PR, include a link to the testing doc or other proof that the feature has been approved for release.** While this PR is open, confirm with the release coordinators that the new CUJs for this feature have been added to the overall CUJs used for testing releases in general.

8. Once this PR is merged, send a ["job run request"](https://forms.gle/rUJaHJSpRGemtGDp6) to the release coordinators to turn on the feature in production by adding a rule in the `/release-coordinator` page.
    - (Optional) If you like, you can fill in [this form](https://goo.gl/forms/sNBWrW03fS6dBWEp1) to announce your feature to the public once it's launched!

9. Once the feature is confirmed to be functioning as intended in production (for at least 2 weeks) by the product team, please do the following, in order:
    - Make sure that the feature is ready to be made permanent. To do this, confirm with the PMs that no users have reported issues with it, and that no regressions have been detected via StackDriver or general user feedback. The PMs should also fill in this [post-launch review template](https://docs.google.com/document/d/1DifFAe3oRzjmVPh2fEllfAky4n0QMAXVQc3Y580qkr8/edit).
    - Once you have confirmation that the feature can be made permanent, merge one last PR to "un-gate" the feature and move the feature flag to the deprecated stage (one of the stages listed in `core/feature_flag_list.py`, meant for flags that are no longer in use). Additionally, in the same PR, please remove all remaining references to the feature flag from the codebase (for example, in all the `if` blocks you created to gate the feature).


## Follow the steps below to add a new feature flag

### Creating the flag

1. Add a new unique feature flag name in the `FeatureNames` enum class in `core/feature_flag_list.py`, similar to a key-value pair. Example:

```python
class FeatureNames(enum.Enum):
    """Enum for feature flag names."""
    // ...
    NEW_FEATURE = 'new_feature',

```

2. Add the name of the new feature flag to one of the feature name lists (`DEV_FEATURES_LIST`, `TEST_FEATURES_LIST`, or `PROD_FEATURES_LIST`) in `core/feature_flag_list.py` according to its stage. Example:

```python
DEV_FEATURES_LIST = [
    # ...
    FeatureNames.NEW_FEATURE,
]
```

3. Add feature flag description and feature stage to the `FEATURE_FLAG_NAME_TO_DESCRIPTION_AND_FEATURE_STAGE` present in `core/feature_flag_list.py`.
Example:

```python
FEATURE_FLAG_NAME_TO_DESCRIPTION_AND_FEATURE_STAGE = {
  # ...
  FeatureNames.NEW_FEATURE.value: (
    (
      'This is description for new feature flag.',
      feature_flag_domain.ServerMode.DEV
    )
  ),
  # ...
}
```

4. To make the feature flag available in the front-end, you need to add it into the FeatureNames enum in `core/templates/domain/feature-flag/feature-status-summary.model.ts` as well:

```typescript
export enum FeatureNames {
  // ...
  NewFeature = 'new_feature',
}
```

### Modifying unit tests to account for the creation of the new flag

The above changes are enough to add a new feature flag to the backend.

However, to make sure the frontend tests succeed, please follow the steps below (so they account for the newly created feature flag).

1. Add the newly created flag as a key-value pair in the `featureStatusSummary` object in the unit-test meant for testing the functioning of the session storage in `core/templates/services/platform-feature.service.spec.ts`, like so:

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

### Writing unit tests for gated features

To write unit tests for gated features, follow the steps below:

#### Frontend

1. Import `PlatformFeatureService` in the .spec file.

```typescript
import { PlatformFeatureService } from 'services/platform-feature.service';
```

2. Create a mock for the service, consisting of a getter for the status of the feature flag, like so:

```typescript
class MockPlatformFeatureService {
  get status(): object {
    return {
      NewFeature: {
        isEnabled: true
      }
    };
  }
}
```

3. Add the mock to the `TestBed` configuration, like so:

```typescript
TestBed.configureTestingModule({
  imports: [
    //...
  ],
  providers: [
    // ...
    {
      provide: PlatformFeatureService,
      useClass: MockPlatformFeatureService
    }
    // ...
  ]
});
```

4. Inject the service in the beforeEach block, like so:

```typescript
let platformFeatureService: PlatformFeatureService;
beforeEach(() => {
  platformFeatureService = TestBed.get(PlatformFeatureService);
});
```

5. Spy on the getter to check the status of the feature flag, like so:

```typescript
spyOnProperty(platformFeatureService, 'status', 'get').and.returnValue(
  {
    NewFeature: {
      isEnabled: false // or true, depending on the test
    }
  }
);
```

#### Backend

In general, you should test both the cases in which the feature flag is enabled and when it is not. To write a test with the feature flag enabled, you can do the following:

1. Import the following modules into the test file:

```python
from core import feature_flag_list
from core.tests import test_utils
```

2. Visit the test where you want to enable feature flags. Add the following decorator to the test, @test_utils.enable_feature_flags([feature_flag_list.FeatureNames.NEW_FEATURE]). Example:

```python
@test_utils.enable_feature_flags([
  feature_flag_list.FeatureNames.NEW_FEATURE])
def test_new_feature_flag_is_enabled(self) -> None:
  # ...
```

To write a test with the feature flag disabled, you do not need to add any changes to your test, as by default all the feature flags are disabled.

## Feature Stage Explanation

Features fall in the three types of stages: dev, test and prod. In short, the stage of a feature implies its maturity & stability and the environment where it can be enabled:

- dev feature can only be enabled in dev environment.
- test feature can be enabled in dev or test environments, but it can never be enabled in production environments.
- prod feature can be enabled in any of the dev, test, production environments.

Note: The environment the flag is placed in determines the enviroment(s) where it CAN BE enabled, not where it IS enabled. A feature in `test` stage, as mentioned above, can only be enabled in the `dev` and `test` environments, and not in the `prod` environment. By default (i.e. when the flag is first added to the codebase and its value is yet to be adjusted from the admin page), however, the flag is disabled in all environments. See the [Changing Value of Feature Flags](#changing-value-of-feature-flags) section for details on how to enable/disable feature flags.

## Usage Example

### Gating in Backend

```python
from core import feature_flag_list
from core.domain import feature_flag_services

# ...

if feature_flag_services.is_feature_flag_enabled(
    self.user_id, feature_flag_list.FeatureNames.DUMMY_FEATURE.value):
    # Code of the feature
else:
    raise Exception("Feature is not fully implemented yet.")
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

Feature flags are defaulted to `false/disabled`. To change their values, you can login as the administrator, provide yourself the role of Release Coordinator from the 'Roles' tab present on the Admin page, navigate to the `/release-coordinator` page, then to the feature tab.

In the feature tab, where you will see the feature flag you added, you can change the settings (see the [Setting of Feature Flags](#settings-of-feature-flags) section for detail) of the feature flags.

Note: since only users with release-coordinator permission can edit the settings of feature flags, you can only enable your features on your local dev instance of Oppia. However, on the live site, only release coordinators can enable/disable features.

## Settings of Feature Flags

Feature flags can be configured in two ways:

- **Editing 'Rollout percentage for logged-in users (0-100)'.** This turns on the feature flag for the specified percentage of logged-in users. Logged-out users are not affected.
- **Editing 'Force-enabled for all users'.** This turns on the feature flag for all logged-in and logged-out users, and overrides all the other feature flag settings.

![Example feature setting](images/adminPageFeatureFlagSettings.png)
