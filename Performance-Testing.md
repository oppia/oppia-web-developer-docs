### Running tests.

To run performance tests for all pages:
``
python -m scripts.run_performance_tests
``

To run test for a specific page:
``
python -m scripts.run_performance_tests --test_name=page_test
``

page_test is the name of the file containing that test eg. splash_test. Refer to `core/tests/performance_tests` directory for the files containing these tests.

### The Framework.

The framework has two major components to it:

1. Performance Data Fetcher:
We use selenium and browsermob-proxy to fetch performance data for the different Oppia pages.
Selenium helps in programmatically interacting with a browser and browsermob-proxy is used to capture HTTP Archive (referred to as HAR) data by recording the communication between the client and server.
The **HTTP Archive** format is a JSON-formatted archive file format used for logging a web browser's interaction with a site. It contains detailed performance data, including information about page loading and displaying and per-resource statistics. Each entry contains the URL requested and request and response headers. For additional details, please see: https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/HAR/Overview.html

2. Performance Metrics Provider:
Refer to: `PageSessionMetrics` and `MultiplePageSessionMetrics` objects in `perf_domain.py`.

### Metrics that we consider.

We consider the following metrics for the first time a user opens a page as well as for a return user (to test caching of various resources).

1. Total page size.
2. Total page load time.
3. Dom ready time.
4. Request time.

**What to do if tests fails?**

If it is something like:
```
self.page_metrics.get_page_load_time_millisecs(), 3000)
AssertionError: 3715 not less than or equal to 3000
```
This means that the threshold set for this metric is not met. This could happen due to:

1. You introduced a change which alters the value of the metric. In this case, there is an increase in the total page load time.
2. This could also happen due to variability in timings from machine to machine. Make sure that these tests are the **only** (major) active process running.

### Writing tests.

To write tests for a new Oppia page:

1. Create a new file in `core/tests/performance_tests/` following similar name conventions to the existing test files there, i.e it should be something like `pagename_test.py`.
2. This folder also contains `test_config.py`, config file for performance tests. Add a unique key for the new page and add a dictionary entry containing thresholds for different metrics to the `TEST_DATA` object. Also, add corresponding `preload_options`.
3. `base.py` has some utility functions for tests which should be used to record page metrics.
4. `core/tests/performance_framework/perf_domain.py` has functions starting with `get_metric_name` that give us the quantitative value for that metric. In case you require any other metric, add it to the same file. Also, refer to description regarding the raw stats that we have.

#### Raw stats that we have.

1. Page session statistics.
2. Page session load timings.

### Issues

* `WebDriverException: Message: chrome not reachable`:
    Try setting bypass proxy for local addresses if you are behind a proxy server.
