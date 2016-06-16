To execute tests:

1. Start the oppia server: `bash scripts/start.sh`.
2. Run: `bash scripts/run_backend_tests.sh --test_target=core.tests.performance_tests.splash_test` from the parent oppia folder.


### Issues

* `WebDriverException: Message: chrome not reachable`:
    Try setting bypass proxy for local addresses if you are behind a proxy server.