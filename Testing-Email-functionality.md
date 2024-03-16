To test the email functionality of Oppia, you can follow these steps:

## Testing with App Engine Deployment

1. **Deploy Oppia on Google App Engine**: You can test email functionality by deploying Oppia on your own Google App Engine instance.

2. **Enable Email Flags**: In the `feconf.py` file, ensure that the email-related flags, e.g `CAN_SEND_EMAILS` are set to `True`.

## Workaround: Using Logs for Testing

If you're unable to deploy Oppia or prefer a simpler method, you can use the following workaround:

1. **Enable Email Functionality**: Set `feconf.CAN_SEND_EMAILS` and other email-related flags to `True` in the `feconf.py` file.

2. **Modify the Send Mail Function**: In the file `core/platform/email/gae_email_service.py`, locate the `send_mail` function. Modify it to print messages instead of sending emails.

3. **Manual Testing**: Perform actions in Oppia that trigger email notifications. If emails are sent via a cron job, manually trigger the corresponding endpoint.

4. **Check Logs**: Monitor the terminal or logs to observe the messages that would have been sent via email.
