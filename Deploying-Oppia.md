These instructions explain how to deploy an instance of Oppia to Google App Engine.

1. Create a [new App Engine instance](https://appengine.google.com/). When you do this, you will be asked to pick a name for your application. In the following, we will refer to this name as APP_NAME.

2. To start a deployment, navigate to the `oppia/` directory and run:
  ```
      python scripts/experimental_deploy.py --app_name={{APP_NAME}}
  ```

3. Check that your deployment has succeeded by visiting your instance on the Web at:
  ```
      https://[APP_NAME].appspot.com
  ```
Logging in from the Google account hosting the app will allow you to access the admin page at   
  ```
      https://[APP_NAME].appspot.com/admin
  ``` 
but you will have to wait for app engine to finish building datastore indexes before this page will load.

### Google analytics

To link your instance of oppia to a Google analytics account, after deploying go to the admin page, select the config tab, and in the "Code to insert just before the closing </head> tag in all pages." field enter:
```
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'TRACKING_ID', 'auto');
  ga('send', 'pageview');
</script>
```
where TRACKING_ID is your tracking ID. It can be found in Google analytics by going to the Admin tab, selecting the relevant account and property, clicking "Tracking info" and then clicking "Tracking Code". Do not use the tracking ID from oppia.org.