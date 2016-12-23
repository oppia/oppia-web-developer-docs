Oppia supports internationalization (i18n) for most learner-facing pages using the [angular-translate](http://angular-translate.github.io/) library, documentation for which can be found [here](https://angular-translate.github.io/docs/#/guide). Anyone is welcome to add new translations, or correct existing ones. For more information about developing for i18n, please see our [i18n developer guide](https://github.com/oppia/oppia/wiki/How-to-develop-for-i18n).

## Contributing translations to Oppia

Thanks to translatewiki.net, it's easy to add or update translations for Oppia! To do so, just follow these steps:

1. Visit the [Oppia Translatewiki](https://translatewiki.net/wiki/Translating:Oppia) page.
2. Click "Translate this project".
3. Select a language to contribute translations for. (Also, read the [notes](https://github.com/oppia/oppia/wiki/Adding-new-translations-for-i18n#note-1-variable-replacement) below describing the translation formats used for variables and plurals.)

Changes will then be pushed to Oppia automatically by the translatewiki admins (**@Nikerabbit** and **@siebrand**), and they will show up in future Oppia releases.

### Note 1: Variable replacement

Within translations, you could add variables that would be later replaced with personalized content. For example, in the text

    You have 3 new notifications.

the number of notifications is a variable, and thus cannot be included directly in the translation. Angular translate solves this problem by using an interpolation service. Your translated phrase should look like:

    You have <[notification_number]> new notifications.

In the html page, the value of `notification_number` will be substituted accordingly by angular-translate. For more details, please refer to the [angular-translate documentation](https://angular-translate.github.io/docs/#/guide/06_variable-replacement). IMPORTANT: the default mechanism of indicating an expression in Angular is using the symbols {{ and }}, however in Oppia these symbols have been replaced by <[ and ]>.

### Note 2: Pluralization

In the example above, if there is only one notification, then we should change "notifications" for "notification". Furthermore, some languages may have more plural forms than English. To handle this, we use a different interpolation service, called [messageformat](https://github.com/SlexAxton/messageformat.js/). In this case, the translation should look like this:

```
{notification_number, plural, =0{You have no notifications.} one{You have one notification.} other{You have # notifications.}}
```

In this example, the # symbol will be replaced by the value of the `notification_number` variable. For a more elaborate tutorial, please refer to the [angular-translate guide for pluralization](http://angular-translate.github.io/docs/#/guide/14_pluralization). 


## Manually adding translations

In general, it is better to add translations via the translatewiki UI where possible. However, in exceptional cases, you can manually add a language to the Oppia codebase in three simple steps:

1. Copy [assets/i18n/en.json file](https://github.com/oppia/oppia/blob/develop/assets/i18n/en.json) into a new file called `xx.json`, where xx is the language code for the new language. You can find this code [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Save the resulting file in the same `i18n/` directory.
2. Replace all occurrences of English with the translated phrase in the target language. It's OK if you omit some translations, but please ensure to remove all occurrences of English translations from the file as when a translation key is missing, the English variant will be used as a fall-back. Please refer to the notes below on how to handle variables and pluralization during translation. Please also see [qqq.json](https://github.com/oppia/oppia/blob/develop/assets/i18n/qqq.json) for important contextual information about what is being translated, and feel free to ask questions on oppia-dev@ or gitter chat if anything is unclear!
3. In [feconf.py](https://github.com/oppia/oppia/blob/develop/feconf.py), add a new entry to the variable  `SUPPORTED_SITE_LANGUAGES` representing the language code and the language name.

After this, you should be able to see the new language listen in the Oppia splash page and translate the site  using the language dropdown in the footer.