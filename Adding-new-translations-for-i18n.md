## Quick overview

In order to ensure that the Oppia website is understandable to learners around the world, we provide internationalization (i18n) support on Oppia for learner-facing pages. This enables learners to view the site in different languages using the language-selector dropdown in the navbar.

Our i18n support uses the [angular-translate](http://angular-translate.github.io/) library, documentation for which can be found [here](https://angular-translate.github.io/docs/#/guide). All platform string translations are provided through our partner, [translatewiki.net](https://translatewiki.net/wiki/Translating:Oppia).

This wiki page explains how to:
- [Fill in missing platform translations](#how-to-fill-in-missing-platform-translations)
- [Translate lessons and other dynamic text](#how-to-translate-lessons-and-other-dynamic-text)
- [Create an i18n-compliant PR](#how-to-create-an-i18n-compliant-pr)
- [Fetch new translations from translatewiki](#how-to-fetch-new-translations-from-translatewiki)
- [Add a new translation language](#how-to-add-a-new-translation-language)

## How to fill in missing platform translations

All our translations are contributed through translatewiki.net. If you see missing translations in a language you're familiar with, please follow these steps to help fix the gap (do not create a PR):

1. Visit the [Oppia Translatewiki](https://translatewiki.net/wiki/Translating:Oppia) page. Read the notes on that page regarding plural rules and special markup syntax.
2. Click "Translate this project".
3. Select a language to contribute translations for. (Also, read the [notes](https://github.com/oppia/oppia/wiki/Adding-new-translations-for-i18n#note-1-variable-replacement) below describing the translation formats used for variables and plurals.)

Changes will then be pushed to Oppia automatically by the Translatewiki admins, and they will show up in future Oppia releases. We typically update new translations to the Oppia.org website on a monthly cadence.

### Important: Don't rely on machine translation

The translatewiki admins have requested that translators do not rely on machine auto-translation, especially if they don't know the language and cannot fix its mistakes. 

In cases where fixing a translation is absolutely necessary for technical reasons (e.g. if a translatewiki string has errors and it's breaking the tests), they recommend doing the following:
- Add the string `!!FUZZY!!` to the beginning of the machine-translated string. This will update the translation in Oppia's source tree, and also mark it as "needing update" for the translators on translatewiki.
- Ask a translator for that language to fix the translation. You can find active translators by going to [Special:ActiveLanguages](https://translatewiki.net/wiki/Special:ActiveLanguages) and clicking on a language name.

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


## How to translate lessons and other dynamic text

If you'd like to help translate Oppia's lessons, please get in touch via our [volunteer form](https://forms.gle/BK99fdqBShY7BPKC8). Successful applicants will be invited to join one of Oppia's translation teams.

We really appreciate help with translations to make the lessons accessible for students whose first language isn't English. Thank you for helping out!


## How to create an i18n-compliant PR

When developing learner-facing functionality, you must use `I18N_...` strings as placeholders for text content. This enables such strings to be translated. You can see the translations in the [i18n directory](https://github.com/oppia/oppia/tree/develop/assets/i18n), which map translation keys like `I18N_MODULE_STRING_NAME` to the translated strings. When a page is loaded, angular-translate traverses the page's html code and changes the translation key to the appropriate translated string.

### Good i18n practices

Please consider i18n while developing. Not all languages are the same: words have different lengths, pluralization rules differ, sentences have different structures and the direction of writing can be from right to left. As a result, sometimes development practices that are generally good (like code reuse) turn out to be less than ideal for i18n. Here are some important points to take into account:
- Do not include raw strings, always use a translation key. Even if it is just an exclamation mark (!)
- When designing a page, plan for the case where strings are twice the length in other languages. Also, think about how the page would look like if the language is written from right to left.
- Try to include as much text as you can in a single key, so that the translator can provide a more coherent translation. Do not divide a paragraph into multiple keys unless you cannot avoid it. Don't split strings up and concatenate them, since different languages will use a different grammatical order.
- If you need to include html in your string, such as `<a></a>` tags, try and pass the code as an argument to the translation service.
- Note that other languages may have more plural forms or genres than English. So, for example, if you include a sentence that is always going to be plural in English, add pluralization support regardless in your translation (see [Note 2 on pluralization](#note-2-pluralization] above).

### Adding a new translation key

To add a new translation key:

1. Choose a translation key name. These key names are always written in uppercase, with the following parts:

   - Prefix: the key MUST start with `I18N_` (otherwise some tests will break).
   - Module name: such as `SIGN_UP_`. Be consistent with existing names, and keep the keys grouped by the module name.
   - String name: a meaningful name representing the function of the string in the page, like `PAGE_TITLE`.

   Note that long translation keys are fine -- the key objective is that the role of the string is well described.

2. Add the new translation key to both the `assets/i18n/en.json` and `assets/i18n/qqq.json` files. In `qqq.json` you should provide translators with a descriptive context for the string. Please see [this page](https://www.mediawiki.org/wiki/Localisation#Message_documentation) for more information on what goes into these descriptions.

You do not need to modify the other JSON files. Translatewiki will do that after you merge the PR.

### Updating the English text for a translation key

When updating the English text for a translation key, first determine whether the new English text has a significantly different meaning to the previous English text.

- If the new text conveys a different meaning from the previous text: do not reuse the translation key. Create a new translation key instead, and delete the previous one.
- If the new text is similar to the previous text, and previous translations are probably still valid: just update the English value directly in `assets/i18n/en.json`. Translatewiki will pick up the updates and push new translations in due course.

### Deleting removed translation keys

If a translation key is not used any more, you must delete it from `assets/i18n/en.json` **and all other translation JSON files**. This is to preserve the property that the keys in other JSON files are a subset of those in `en.json`.

### Verifying changes to translation files

To verify your changes to translation files locally, run the following command in a terminal:

Python:
```
python -m scripts.run_backend_tests --test_targets=core.controllers.base_test.I18nDictsTests
```

Docker:
```
make run_tests.backend PYTHON_ARGS="--test_targets=core.controllers.base_test.I18nDictsTests"
```

This validates the translation JSON files by verifying that the keys are correctly sorted, that the keys in en.json and qqq.json match, that every other translation JSON file has a subset of the keys in en.json, and so on.


### Flash of Untranslated Content

Sometimes, the page is rendered in the browser before the locale file with the translations is loaded. As a result, the user can see the translation keys briefly before they're replaced with the corresponding translations, which is not a good user experience. This problem is known as the "Flash of Untranslated Content", or FoUC.

When adding a new string to Oppia's HTML code, please take into account the following tips to prevent FoUC:
- The FoUC behaves differently in the preferred language (English) and all the other languages. Please manually check that there is no FoUC in both cases.
- Add the translation key inside the html tag as the value of the translate attribute. This will prevent the key from being shown briefly -- instead, the location of the string will remain empty in the interim.
- If the string is in a very visible location and there is FoUC in the preferred language, add the key and the translation into the `DEFAULT_TRANSLATIONS` constant defined in the file [i18n.js](https://github.com/oppia/oppia/blob/develop/core/templates/i18n.js).

### Placeholders and tooltips

Remember to translate placeholders and tooltips! For tooltips, use the translate filter on the tooltip attribute value. For example:

    tooltip="<['I18N_GALLERY_VIEWS_TOOLTIP' | translate]>"

For placeholders, use the attribute `ng-attr-placeholder` instead of `placeholder`. As a value for this attribute, apply a translate filter to the key. For example:

    ng-attr-placeholder="<['I18N_FORMS_TYPE_NUMBER' | translate]>"

### Plurals and gender

Angular translate supports pluralization and representation of different genders using the [messageformat library](https://github.com/SlexAxton/messageformat.js/). For example, if you need to translate the html code

    <span ng-if="choices > 1">Select <[choices]> choices.</span>
    <span ng-if="choices == 1">Select one choice.</span>
    <span ng-if="choices == 0">Select no choice.</span>

you must replace this code with:

    <span translate=”TRANSLATION_KEY” translate-values=”{choicesValue:<[choices]>}” translate-interpolation="messageformat"></span>

and add the translation into the [en.json file](https://github.com/oppia/oppia/blob/develop/assets/i18n/en.json) with the following format:

    “TRANSLATION_KEY”: “{choicesValue, plural, =0{Select no choice.} one{Select one choice.} other{Select # choices.}}”

For a more complete tutorial, refer to the [angular translate guide](http://angular-translate.github.io/docs/#/guide/14_pluralization) and the [messageformat documentation](https://github.com/SlexAxton/messageformat.js/).

### Testing

In e2e tests, to check that a page has no untranslated keys: call the helper function  `ensurePageHasNoTranslationIds`, which is located in [webdriverio_utils/general.js](https://github.com/oppia/oppia/blob/develop/core/tests/webdriverio_utils/general.js).

Also, Karma tests may generate 404 warnings, as the required locale files aren't available in the Karma test environment. To overcome this, add the following line in the first part of your Karma test:

    beforeEach(module('oppia', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));

## How to fetch new translations from translatewiki

Note that we generally do this on a monthly basis. Here are the steps that we follow:

1. Checkout the `translatewiki-prs` branch.
2. Merge `develop` into `translatewiki-prs` and resolve all conflicts (usually by accepting the changes from `translatewiki-prs`).
3. Run `python -m scripts.run_backend_tests --test_target=core.controllers.base_test` on that branch. This will validate the I18n files. If any errors arise, they need to be fixed.
4. Create a PR (similar to [this one](https://github.com/oppia/oppia/pull/20706)) that brings the new translations from translatewiki into develop.

The reason we cannot fully automate this yet is because of step 3. Sometimes, the crowdsourced translations on translatewiki incorrectly handle syntax (e.g. HTML tags in the original strings do not show up in the translated text) and this is an issue that needs to be fixed manually.

## How to add a new translation language

When a language has reached 90+% completion on [translatewiki](https://translatewiki.net/w/i.php?title=Special:MessageGroupStats&group=oppia), we can add it to the website. 

To do this: in [feconf.py](https://github.com/oppia/oppia/blob/develop/feconf.py), add a new entry to the variable  `SUPPORTED_SITE_LANGUAGES` representing the language code and the language name.

After this, you should be able to see the new language listed in the Oppia splash page and translate the site using the language dropdown in the footer.
