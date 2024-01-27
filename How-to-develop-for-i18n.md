## Quick overview

In order to ensure that the Oppia website is understandable to learners around the world, we provide internationalization (i18n) support on Oppia. This enables learners to view the site in different languages using the language-selector dropdown in the navbar.

Our i18n support is based on the JavaScript library [angular-translate](https://angular-translate.github.io/). At the moment, only the learner-facing pages of Oppia are internationalized.

The [i18n directory](https://github.com/oppia/oppia/tree/develop/assets/i18n) contains one translation file in JSON format for each supported language. Each of these files is a map from translation keys like `I18N_MODULE_STRING_NAME` to the translated strings. When a page is loaded, angular-translate traverses the page's html code and changes the translation key to the appropriate translated string.

## Good i18n practices

We encourage you to think about i18n while developing, and not defer it as something to handle later on. Not all languages are the same: words have different lengths, pluralization rules differ, sentences have different structures and the direction of writing can be from right to left. As a result, sometimes development practices that are generally good (like code reuse) turn out to be less than ideal for i18n. Here are some important points to take into account:
- Do not include raw strings, always use a translation key. Even if it is just an exclamation mark (!)
- When designing a page, plan for the case where strings are twice the length in other languages. Also, think about how the page would look like if the language is written from right to left.
- Try to include as much text as you can in a single key, so that the translator can provide a more coherent translation. Do not divide a paragraph into multiple keys unless you cannot avoid it. Don't split strings up and concatenate them, since different languages will use a different grammatical order.
- If you need to include html in your string, such as `<a></a>` tags, try and pass the code as an argument to the translation service.
- Take into account that other languages may have more plural forms or genres than English. For example, if you include a sentence that is always going to be plural in English, add pluralization support regardless in your translation.

## Giving context to translators

We have a file at `assets/i18n/qqq.json` for providing translators with context -- if you add new strings to be translated, you should also add them to this file. Please see [this page](https://www.mediawiki.org/wiki/Localisation#Message_documentation) for more information on what goes into these descriptions.

## Adding new translation keys

When adding a new translation key, add it to both the `assets/i18n/en.json` and `assets/i18n/qqq.json` files. You do not need to modify the other JSON files; translatewiki will do that after you merge the PR.

To choose a translation key name, bear in mind that these key names are always written in uppercase, with the following parts:

1. Prefix: the key MUST start with `I18N_` (otherwise some tests will break).
2. Module name: such as `SIGN_UP_`. Be consistent with existing names, and keep the keys grouped by the module name.
3. String name: a meaningful name representing the function of the string in the page, like `PAGE_TITLE`.

Concatenating these parts gives the final result: `I18N_SIGNUP_PAGE_TITLE`. Note that long translation keys are fine -- the key objective is that the role of the string is well described.

## Updating the English value for a translation key

When updating the English text for a translation key, first determine whether the new English text has a significantly different meaning to the previous English text.

- If the new text conveys a different meaning from the previous text: do not reuse the translation key. Create a new translation key instead, and delete the previous one.
- If the new text is similar to the previous text, and previous translations are probably still valid: just update the English value directly in `assets/i18n/en.json`. Translatewiki will pick up the updates and push new translations in due course.

## Deleting removed translation keys

If a translation key is not used any more, you must delete it from `assets/i18n/en.json` **and all other translation JSON files**. This is to preserve the property that the keys in other JSON files are a subset of those in `en.json`.

## Verifying changes to translation files

To verify your changes to translation files locally, run the following command in a terminal:

Python:
```
    python -m scripts.run_backend_tests --test_target=core.controllers.base_test.I18nDictsTests
```

Docker:
```
    make run_backend_tests PYTHON_ARGS="--test_target=core.controllers.base_test.I18nDictsTests"
```

This validates the translation JSON files by verifying that the keys are correctly sorted, that the keys in en.json and qqq.json match, that every other translation JSON file has a subset of the keys in en.json, and so on.


## Flash of Untranslated Content

Sometimes, the page is rendered in the browser before the locale file with the translations is loaded. As a result, the user can see the translation keys briefly before they're replaced with the corresponding translations, which is not a good user experience. This problem is known as the "Flash of Untranslated Content", or FoUC.

When adding a new string to Oppia's HTML code, please take into account the following tips to prevent FoUC:
- The FoUC behaves differently in the preferred language (English) and all the other languages. Please manually check that there is no FoUC in both cases.
- Add the translation key inside the html tag as the value of the translate attribute. This will prevent the key from being shown briefly -- instead, the location of the string will remain empty in the interim.
- If the string is in a very visible location and there is FoUC in the preferred language, add the key and the translation into the `DEFAULT_TRANSLATIONS` constant defined in the file [i18n.js](https://github.com/oppia/oppia/blob/develop/core/templates/i18n.js).

## Titles

To add a title to the window, replace the block maintitle for a translation key:

    {% block maintitle %}TRANSLATE_KEY{% endblock maintitle %}

and add the translation into the corresponding json files. Titles should always be translated, but this is not mandatory. If you replace this block with a common string, it will be shown as the title instead.

## Placeholders and tooltips

Remember to translate placeholders and tooltips! For tooltips, use the translate filter on the tooltip attribute value. For example:

    tooltip="<['I18N_GALLERY_VIEWS_TOOLTIP' | translate]>"

For placeholders, use the attribute `ng-attr-placeholder` instead of `placeholder`. As a value for this attribute, apply a translate filter to the key. For example:

    ng-attr-placeholder="<['I18N_FORMS_TYPE_NUMBER' | translate]>"

## Plurals and gender

Angular translate supports pluralization and representation of different genders using the [messageformat library](https://github.com/SlexAxton/messageformat.js/). For example, if you need to translate the html code

    <span ng-if="choices > 1">Select <[choices]> choices.</span>
    <span ng-if="choices == 1">Select one choice.</span>
    <span ng-if="choices == 0">Select no choice.</span>

you must replace this code with:

    <span translate=”TRANSLATION_KEY” translate-values=”{choicesValue:<[choices]>}” translate-interpolation="messageformat"></span>

and add the translation into the [en.json file](https://github.com/oppia/oppia/blob/develop/assets/i18n/en.json) with the following format:

    “TRANSLATION_KEY”: “{choicesValue, plural, =0{Select no choice.} one{Select one choice.} other{Select # choices.}}”

For a more complete tutorial, refer to the [angular translate guide](http://angular-translate.github.io/docs/#/guide/14_pluralization) and the [messageformat documentation](https://github.com/SlexAxton/messageformat.js/).

## Testing

In e2e tests, to check that a page has no untranslated keys: call the helper function  `ensurePageHasNoTranslationIds`, which is located in [webdriverio_utils/general.js](https://github.com/oppia/oppia/blob/develop/core/tests/webdriverio_utils/general.js).

Also, Karma tests may generate 404 warnings, as the required locale files aren't available in the Karma test environment. To overcome this, add the following line in the first part of your Karma test:

    beforeEach(module('oppia', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));
