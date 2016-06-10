Oppia supports internationalization (i18n) for most of the student-facing pages. The library used for translations is [angular-translate](http://angular-translate.github.io/), you can find more information in the [docs](https://angular-translate.github.io/docs/#/guide). We encourage developers to add new translations of correct existing ones to make the platform available in different languages.

## How to add a new language

To add a new language to the Oppia codebase you just need to:

1. Copy the file [i18n/en.json](https://github.com/oppia/oppia/blob/develop/i18n/en.json) into a new file called xx.json. Replace xx with the language code, you can find the appropriate language code [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Save the file in the same i18n/ directory.
2. Replace all the English translations for the translations in the new language. Is OK if you don't add them all at the same time, but please erase all the English translations from the file. If a translation key is missing, the English translation will be used.
3. In the file [feconf.py](https://github.com/oppia/oppia/blob/develop/feconf.py) locate the variable SUPPORTED_SITE_LANGUAGES. Add a new entry to SUPPORTED_SITE_LANGUAGES using the language code and the language name.

After this, you should be able to see the new language in the Oppia page and translate the site.