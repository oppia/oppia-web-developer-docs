Oppia currently supports internationalization (i18n) for most learner-facing pages. We use the [angular-translate](http://angular-translate.github.io/) library -- here are the [docs](https://angular-translate.github.io/docs/#/guide). Developers are welcome to add new translations, or correct existing ones. If you'd like to know more about how to use the i18n platform, please see our [i18n developer guide](https://github.com/oppia/oppia/wiki/How-to-develop-for-i18n).

## Adding a new language to Oppia

To add a new language to the Oppia codebase:

1. Copy the [i18n/en.json file](https://github.com/oppia/oppia/blob/develop/i18n/en.json) into a new file called `xx.json`, where xx is the language code for the new language. You can find this code [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Save the resulting file in the same `i18n/` directory.
2. Replace all the English translations with the translations in the new language. It's OK if you omit some translations, but in that case, please erase all the English translations from the file. If a translation key is missing, the English translation will be used as a fallback. Please also see the notes below about how to handle variables and pluralization when translating.
3. In [feconf.py](https://github.com/oppia/oppia/blob/develop/feconf.py), locate the `SUPPORTED_SITE_LANGUAGES` variable and add a new entry to it using the language code and the language name.

After this, you should be able to see the new language in the Oppia page and translate the site by using the language dropdown in the footer.

### Note 1: Variable replacement

Inside the translations, you can add variables that are going to be replaced with personalized content. For example, in the text

    You have 3 new notifications.

the number of notifications is a variable, and thus can't be included directly in the translation. Angular translate solves this problem by using an interpolation service. Now, your translation is going to look like this:

    You have <[notification_number]> new notifications.

In the html page, the value of `notification_number` will be substituted accordingly by angular-translate. For more detail, please see the [angular-translate docs](https://angular-translate.github.io/docs/#/guide/06_variable-replacement). Incidentally, note that the default way of indicating an expression in Angular is with the symbols {{ and }}, but in Oppia's codebase these symbols have been replaced by <[ and ]>.

### Note 2: Pluralization

In the example above, if there is only one notification, then we should change the word "notifications" for "notification". Furthermore, some languages may have more plural forms than English. To handle this, we use a different interpolation service, called [messageformat](https://github.com/SlexAxton/messageformat.js/). In this case, the translation looks like this:

```
{notification_number, plural, =0{You have no notifications.} one{You have one notification.} other{You have # notifications.}}
```

In this example, the # symbol will be replaced by the value of the `notification_number` variable. For a more complete tutorial, please see the [angular-translate guide for pluralization](http://angular-translate.github.io/docs/#/guide/14_pluralization). 
