## Quick overview

Internationalization (i18n) support for Oppia is based on the JavaScript library [angular-translate](https://angular-translate.github.io/). At the moment, only the learner view of Oppia is internationalized. The editor will remain in English until the design refactor takes place.

The [i18n directory](https://github.com/oppia/oppia/tree/develop/assets/i18n) contains one translation file in JSON format for each supported language. Each of these files is a map from translation keys like `I18N_MODULE_STRING_NAME` to the translated strings. When a page is loaded, angular-translate traverses through the page's html code and changes the translation key to the appropriate translated string.

## Good practices in i18n

We encourage you to think about i18n while developing, and not defer it as something to handle later on. Not all languages are the same: words have different lengths, pluralization rules differ, sentences have different structures and the direction of writing can be from right to left. As a result, sometimes development practices that are generally good (like code reuse) turn out to be less than ideal for i18n. Here are some important points to take into account:
- Do not include raw strings, always use a translation key. Even if it is just an exclamation mark (!)
- When designing a page, plan for the case where strings are twice the length in other languages. Also, think about how the page would look like if the language is written from right to left.
- Avoid the concatenation of strings to form phrases like `<[subject]><[verb]><[object]>` to obtain the phrase “She plays the piano”. Different languages will use a different grammatical order.
- Try to include as much text as you can in a single key, so that the translator can provide a more coherent translation. Do not divide a paragraph into multiple keys unless you cannnot avoid it.
- If you need to include html in your string, such as `<a></a>` tags, try and pass the code as an argument to the translation service.
- Take into account that other languages may have more plural forms or genres than English. For example, if you include a sentence that is always going to be plural in English, add pluralization support regardless in your translation.

## How to name new keys

Translation key names are always written using uppercase and have some defined parts:

1. Prefix: the key MUST start with `I18N_` (otherwise some tests will break).
2. Module name: such as `SIGN_UP_`. Be consistent with existing names, and keep the keys grouped by the module name.
3. String name: a meaningful name representing the function of the string in the page, like `PAGE_TITLE`.

The final result would be `I18N_SIGNUP_PAGE_TITLE`. Long translation keys are fine -- the key objective is that the role of the string is well described.

## Giving context to translators

We have a file at `assets/i18n/qqq.json` for providing translators with context -- if you add new strings to be translated, you should also add them to this file. Please see [this page](https://www.mediawiki.org/wiki/Localisation#Message_documentation) for more information on what goes into these descriptions.

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

In e2e tests, to check that a page has no untranslated keys: call the helper function  `ensurePageHasNoTranslationIds`, which is located in [protractor_utils/general.js](https://github.com/oppia/oppia/blob/develop/core/tests/protractor_utils/general.js).

Also, Karma tests may generate 404 warnings, as the required locale files aren't available in the Karma test environment. To overcome this, add the following line in the first part of your Karma test:

    beforeEach(module('oppia', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));
