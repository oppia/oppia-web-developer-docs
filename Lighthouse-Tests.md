# Lighthouse CI Automated Tests
Lighthouse CI is a suite of tools that make continuously running, saving, retrieving, and asserting against Lighthouse results as easy as possible. Lighthouse has tests for performance, best practices, and accessibility. 

To run the automated tests on Oppia. Type the commands
"python -m scripts.run_lighthouse_tests"
or
“python -m scripts.run_lighthouse_accessibility_tests” in the terminal.

The script will run the Oppia server, and then run Lighthouse checks on all the webpages outlined in the lighthouserc.js config. The Lighthouse tests also automatically test against any PR with Github Actions. The accessibility tests run only accessibility audits while the general lighthouse test audits best practices and performance

For further information about lighthouse [checkout this page](https://developers.google.com/web/tools/lighthouse)

# How to add new pages to lighthouse tests

If you have recently created a new webpage on Oppia, it should be covered by lighthouse tests to ensure that your page is accessible.

## Add a static webpage
If your webpage URL is static and doesn't require any id generation. Then the only thing you need to do is add your webpage to the lighthouserc.js and lighthouserc-accessibility.js config. 

For example, if your webpage is on the URL: `http://127.0.0.1:8181/your/static/webpage`
Just add the URL to the `'url'` list in the config

      'url': [
        'http://127.0.0.1:8181/admin',
        'http://127.0.0.1:8181/your/static/webpage'
      ]

## Add a dynamic webpage
If your webpage URL is dynamic and requires id generation. You will need to generate the id in lighthouse_setup.js and export the id to the lighthouse configs. As an example, we will show how we add the exploration editor to the lighthouse tests. 

### 1. Get the URL

```
const getExplorationEditorUrl = async function(browser, page) {
  try {
    // eslint-disable-next-line dot-notation
    await page.goto(
      CREATOR_DASHBOARD_URL, { waitUntil: networkIdle });

    await page.waitForSelector(createButtonSelector, {visible: true});
    await page.click(createButtonSelector);
    await page.waitForSelector(
      dismissCreateModalSelector, {visible: true});
    explorationEditorUrl = await page.url();
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log(e);
  }
};
```

## 2. Write the URL to stdout

```
  await getExplorationEditorUrl(browser, page);
  await process.stdout.write(
    [
      explorationEditorUrl,
    ].join('\n')
  );
```

## 3. Export the URL to an environment variable

```
def export_url(url):
    """Exports the url to an environmental variable."""
    url_list = url.split('/')
    if 'create' in url:
        os.environ['exploration_editor'] = url_list[4]

```
## 4. Call the environment variable in the lighthouse config
```
      'url': [
        'http://127.0.0.1:8181/admin',
        `http://127.0.0.1:8181/create/${process.env.exploration_editor}`,
      ]
    },
```

# Debugging Lighthouse Tests