Cron jobs are one of the safest ways to run recurring server work in Oppia (cleanup, emails, periodic computations, and so on).

## Table of contents

* [What are cron jobs](#what-are-cron-jobs)
* [How to write cron jobs](#how-to-write-cron-jobs)
  * [1. Define the behavior first](#1-define-the-behavior-first)
  * [2. Add or update a handler in `core/controllers/cron.py`](#2-add-or-update-a-handler-in-corecontrollerscronpy)
  * [3. Register the URL route in `main.py`](#3-register-the-url-route-in-mainpy)
  * [4. Add the schedule in `cron.yaml`](#4-add-the-schedule-in-cronyaml)
  * [5. Add/update tests](#5-addupdate-tests)
  * [6. Add rollout/testing documentation for production](#6-add-rollouttesting-documentation-for-production)
* [How to test cron jobs locally](#how-to-test-cron-jobs-locally)
  * [1. Run Oppia locally and log in as super admin](#1-run-oppia-locally-and-log-in-as-super-admin)
  * [2. Trigger the cron endpoint](#2-trigger-the-cron-endpoint)
  * [3. Verify the result](#3-verify-the-result)
  * [4. Run automated tests](#4-run-automated-tests)
* [How cron jobs work in production](#how-cron-jobs-work-in-production)
* [References](#references)

## What are cron jobs

A cron job is a task that runs on a schedule. In Oppia, cron jobs are used for recurring backend work such as:

* deleting old or stale data;
* sending recurring email notifications;
* triggering periodic Beam computations;
* running cleanup/scrubber routines.

In Oppia's architecture, a cron job is usually composed of 3 parts:

1. A schedule entry in `cron.yaml`.
2. A route in `main.py` whose URL starts with `/cron/...`.
3. A handler in `core/controllers/cron.py` that does the work (or delegates to services/jobs).

## How to write cron jobs

Use this workflow when adding a new cron job.

### 1. Define the behavior first

Before writing code, decide:

* what the cron should do;
* how often it should run;
* whether it is safe to run more than once (idempotency);
* what success and failure output should look like.

If the work is long-running or heavy, prefer triggering a deferred task or Beam job from the cron handler, rather than doing all the work inline.

### 2. Add or update a handler in `core/controllers/cron.py`

Create a handler that uses `@acl_decorators.can_perform_cron_tasks` and delegates to domain services or Beam/taskqueue utilities.

```python
class CronExampleHandler(base.BaseHandler[Dict[str, str], Dict[str, str]]):
    """Handler for running Example cron work."""

    GET_HANDLER_ERROR_RETURN_TYPE = feconf.HANDLER_TYPE_JSON
    URL_PATH_ARGS_SCHEMAS: Dict[str, str] = {}
    HANDLER_ARGS_SCHEMAS: Dict[str, Dict[str, str]] = {'GET': {}}

    @acl_decorators.can_perform_cron_tasks
    def get(self) -> None:
        example_services.run_example_work()
        return self.render_json({})
```

### 3. Register the URL route in `main.py`

In the cron URL section of `main.py`, add a route for the handler.

Important: cron URLs must start with `/cron/...`.

### 4. Add the schedule in `cron.yaml`

Add a new entry with:

* a clear `description`;
* the cron endpoint `url`;
* a `schedule` string (for example, "every day 16:00").

### 5. Add/update tests

Add tests in `core/controllers/cron_test.py` (or related test modules) for:

* expected behavior when the endpoint runs;
* the correct service/job call being triggered;
* output or side effects for success/failure paths.

### 6. Add rollout/testing documentation for production

For production-facing cron changes, follow the process in [[Testing jobs and other features on production|Testing-jobs-and-other-features-on-production]].

## How to test cron jobs locally

This is a practical local test loop for contributors.

### 1. Run Oppia locally and log in as super admin

Set up and start Oppia using [[Installing Oppia|Installing-Oppia]], then sign in with super-admin privileges.

### 2. Trigger the cron endpoint

You can trigger a cron handler in either of these ways:

* open the endpoint in your browser while logged in as super admin; or
* call it directly:

```bash
curl -X GET http://localhost:8181/cron/your/endpoint
```

If needed, you can emulate a cron-originated request by setting the cron header:

```bash
curl -X GET \
  -H "X-Appengine-Cron: true" \
  http://localhost:8181/cron/your/endpoint
```

### 3. Verify the result

Check:

* server logs;
* datastore/model changes;
* emitted job output (if the handler triggered Beam/deferred work);
* user-visible effects (for example, email scheduling or updated indexes).

### 4. Run automated tests

Run cron controller tests and any service tests your change touches:

```bash
python -m scripts.run_backend_tests --test_targets=core.controllers.cron_test
```

For broader confidence, also run the specific module tests related to your new logic.

## How cron jobs work in production

At a high level, production execution looks like this:

1. App Engine cron reads schedules from `cron.yaml`.
2. At scheduled times, App Engine sends HTTP requests to the configured `/cron/...` URLs.
3. `main.py` routes each request to the matching handler in `core/controllers/cron.py`.
4. `@acl_decorators.can_perform_cron_tasks` protects the endpoint (cron header-based access; super admin access is useful for controlled manual runs).
5. The handler executes lightweight orchestration code and delegates real work to services, deferred tasks, or Beam jobs.
6. Results are visible through logs and downstream effects (model updates, emails, indexes, and so on).

For jobs/features that need production approval and backup-server validation, follow [[Testing jobs and other features on production|Testing-jobs-and-other-features-on-production]].

## References

* [`cron.yaml` (Oppia)](https://github.com/oppia/oppia/blob/develop/cron.yaml)
* [`main.py` cron routes (Oppia)](https://github.com/oppia/oppia/blob/develop/main.py)
* [`core/controllers/cron.py` (Oppia)](https://github.com/oppia/oppia/blob/develop/core/controllers/cron.py)
* [`core/controllers/cron_test.py` (Oppia)](https://github.com/oppia/oppia/blob/develop/core/controllers/cron_test.py)
* [[Apache Beam Jobs|Apache-Beam-Jobs]]
* [[Running Jobs on Dev Server|Running-Jobs-on-Dev-Server]]
* [[Backend tests|Backend-tests]]
