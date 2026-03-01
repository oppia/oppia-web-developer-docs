This page explains how to connect a personal Google Analytics account to a local Oppia dev server and verify analytics events without relying only on "window.dataLayer".

## Table of contents
* [Overview](#overview)
* [Set up a personal Google Analytics property](#set-up-a-personal-google-analytics-property)
* [Connect Google Analytics to local Oppia](#connect-google-analytics-to-local-oppia)
* [Verify events locally](#verify-events-locally)
* [Troubleshooting and tips](#troubleshooting-and-tips)

## Overview
Oppia sends frontend analytics through `gtag.js`. On a local dev server, these events are controlled by analytics constants that are compiled into the frontend. By pointing those constants to your own Google Analytics property, you can use the Google Analytics UI to confirm whether events are being registered.

This guide assumes you are running Oppia locally and want to keep analytics traffic private to your own account.

## Set up a personal Google Analytics property
1. Go to Google Analytics and create a new account (or use an existing one).
2. Create a new property and choose a "Web" data stream.
3. Copy the "Measurement ID" for the web stream. It looks like `G-XXXXXXXXXX`.
4. If you want Google Tag Manager support, create a new Tag Manager container and copy its container ID. It looks like `GTM-XXXXXXX`.

## Connect Google Analytics to local Oppia
1. Open `assets/analytics-constants.json` in your local Oppia repo.
2. Update the fields below to use your own IDs.
3. Set `GA_ANALYTICS_ID` to your measurement ID (the `G-...` value).
4. Set `GTM_ANALYTICS_ID` to your Tag Manager container ID (the `GTM-...` value). If you are not using Tag Manager, create a container and use its ID since the GTM script is loaded whenever analytics are enabled.
5. Ensure `CAN_SEND_ANALYTICS_EVENTS` is `true`.
6. If you are not serving Oppia on `localhost`, update `SITE_NAME_FOR_ANALYTICS` to the hostname you are using (for example `127.0.0.1`).
7. Restart the dev server so the frontend rebuilds with the new constants.

If analytics events are still not reaching your Google Analytics property, verify that the webpack template parameters are wired through to the HTML templates.

In `webpack.common.config.ts`, confirm the helper below exists and that it is passed to both HtmlWebpackPlugin instances (for `oppia_root` and `lightweight_oppia_root`):

```ts
// webpack.common.config.ts
// Helper function to provide analytics constants to HTML templates
function getTemplateParameters() {
  return {
    CAN_SEND_ANALYTICS_EVENTS:
      analyticsConstants.CAN_SEND_ANALYTICS_EVENTS || false,
    GA_ANALYTICS_ID: analyticsConstants.GA_ANALYTICS_ID || '',
    GTM_ANALYTICS_ID: analyticsConstants.GTM_ANALYTICS_ID || '',
    SITE_NAME_FOR_ANALYTICS: analyticsConstants.SITE_NAME_FOR_ANALYTICS || '',
  };
}
```

And ensure it is referenced in both plugin configs:

```ts
templateParameters: getTemplateParameters(),
```

To avoid accidentally committing your local IDs, you can mark the file as unchanged in git:

```bash
git update-index --assume-unchanged assets/analytics-constants.json
```

To undo that later:

```bash
git update-index --no-assume-unchanged assets/analytics-constants.json
```

## Verify events locally
1. Open Oppia in your browser and reproduce the user action that should fire the event.
2. In your browser devtools, verify that `window.gtag` exists and that `window.dataLayer` receives the event payload.
3. In the Network tab, filter for Google Analytics requests and confirm that `https://www.googletagmanager.com/gtag/js?id=G-...` is loaded and that event payloads are sent to Google Analytics endpoints (for GA4 this is often `https://www.google-analytics.com/g/collect` or a regional `https://region1.google-analytics.com/g/collect`).
4. In Google Analytics, open "Reports" then "Realtime" to see events appear within seconds.

## Troubleshooting and tips
1. If `window.gtag` is undefined, make sure `CAN_SEND_ANALYTICS_EVENTS` is `true` and restart the dev server.
2. If you do not see any network requests, disable ad blockers or privacy extensions for `localhost`.
3. If Realtime does not show events, confirm that the measurement ID in `assets/analytics-constants.json` matches your property.
4. If events show in `window.dataLayer` but not in GA, double check that `gtag.js` was downloaded and that requests to Google Analytics are not blocked by the browser or network.
