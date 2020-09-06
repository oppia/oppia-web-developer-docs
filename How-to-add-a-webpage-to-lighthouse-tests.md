# Lighthouse CI Automated Tests
Lighthouse CI is a suite of tools that make continuously running, saving, retrieving, and asserting against Lighthouse results as easy as possible. Lighthouse has tests for performance, best practices, and accessibility. 

To run the automated tests on Oppia. Type the command 
“python -m scripts.run_lighthouse_tests” in the terminal.

The script will run the Oppia server, and then run Lighthouse checks on all the webpages outlined in the lighthouserc.json config. The Lighthouse tests also automatically test against any PR with Github Actions. 

If you have recently created a new webpage on Oppia, it should be covered by lighthouse tests to ensure that your page is accessible.

