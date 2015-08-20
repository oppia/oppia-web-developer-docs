These instructions explain how to deploy an instance of Oppia to Google App Engine.

1. Create a [new App Engine instance](https://appengine.google.com/). When you do this, you will be asked to pick a name for your application. In the following, we will refer to this name as [APP\_NAME](APP_NAME.md).

2. To start a deployment, navigate to the `oppia/` directory and run:
  ```
      python scripts/experimental_deploy.py --app_name={{APP_NAME}}
  ```

3. Check that your deployment has succeeded by visiting your instance on the Web at:
  ```
      https://[APP_NAME].appspot.com
  ```
