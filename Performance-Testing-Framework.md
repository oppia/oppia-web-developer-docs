You can run performance tests using

```
    bash scripts/run_performance_tests.sh
```

### Metrics that we consider.

We consider the following metrics for the first time a user opens a page as well as for a return user (to test caching of various resources).

1. Total page size.
2. Total page load time.
3. Dom ready time.
4. Request time.

** What to do if tests fails? **

If it is something like:
```
self.page_metrics.get_page_load_time_millisecs(), 3000)
AssertionError: 3715 not less than or equal to 3000
```
This means that the threshold set for this metric is not met. This could happen due to:

1. You introduced a change which increases the total page load time.
2. This could also happen due to variability in timings from machine to machine. Make sure that these tests are the **only** (major) active process running.

### Issues

* `WebDriverException: Message: chrome not reachable`:
    Try setting bypass proxy for local addresses if you are behind a proxy server.