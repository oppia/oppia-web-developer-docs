## Quick overview

The internationalization (i18n) support for Oppia is based on the JavaScript library [angular-translate](https://angular-translate.github.io/). At the moment, only the student view of Oppia is internationalized. The editor remains only in English until the design refactoring takes place.
The [i18n directory](https://github.com/oppia/oppia/tree/develop/i18n) contains one translation file in JSON format for each supported language. Each of these files is a map from translation keys like `I18N_MODULE_STRING_NAME` to the translated strings. When a page is loaded, the angular translate searches through the html code and inserts the translated strings wherever the key is present, according to the selected language.

## Good practices in i18n

We encourage you to think about i18n while you are developing, not just as a post process of the code. Not all languages are the same: words have different lengths, the pluralization is different, sentences have a different structure and writing can be from left to right. As a result, sometimes what is a good criteria for development (like code reusing) is not so good for i18n. Here are some important points to have into account:
- Do not include raw strings, always use a translation key. Yes, even if it is a exclamation point.
- When designing a page, plan for the case where strings have twice the length in other languages. Also, try to think how the page would look if the language is written from right to left.
- Avoid the concatenation of string to form phrases like `<[subject]><[action]><[object]>` to obtain the phrase “She plays the piano”. Different languages will use a different order.
- Try to include as much text as you can in a single key, so the translator can give better coherence to the phrase. Do not divide a paragraph in several keys if you can avoid it.
- If you need to include html in your string like an `<a></a>` tag, try to pass the code as an argument to the translation service.
- Have into account that other languages may have more plural forms or genres than English. For example, if you include a sentence that it is always plural in English, add pluralization support anyway.

##How to name new keys

Translation key names are always written in capital letter and have some defined parts:

1. Prefix: the key MUST start with `I18N_` (otherwise some test will be broken).
2. Module name: for example `SIGN_UP_`. Please be consistent with previous names and keep the keys grouped by module name.
3. String name: some words to describe the function of the string in the page, like `PAGE_TITLE`.

The final result is `I18N_SIGNUP_PAGE_TITLE`. Do not be afraid of overly long translation keys, they should be descriptive of the role of the string.

## Flash of Untranslated Content

Sometimes, the page is displayed in the browser before the locale file with the translations is loaded. As a result, the user can see the translation keys for a breve moment before they are replaced with the corresponding translations, which is not a good experience. This problem is known as Flash of Untranslated Content or FoUC.

When adding new string to the html code in Oppia, please have into account the following tips to prevent FoUC:
- The FoUC behaves differently in the preferred language (English) and all the other languages. Please be sure to manually check there is no FoUC in both cases.
- Add the translation key inside the html tag as value of the translate attribute. This will prevent the key from showing for a moment, instead, the place for the string will appear empty.
- If the string is in a very visible place and there is FoUC in the preferred language, add the key and the translation into the constant `DEFAULT_TRANSLATIONS` defined in the file [i18n.js](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/i18n.js)

## Titles

To add a title to the window, replace the block maintitle for a translation key:

    {% block maintitle %}TRANSLATE_KEY{% endblock maintitle %}

and add the translation into the corresponding json files. Titles should be always translated, but this is not mandatory. If you replace this block with a common string, it will be shown as title. 

## Placeholders and tooltips

Don’t forget to translate your placeholders and tooltips! For tooltips, use the translate filter into the tooltip attribute value. For example:

    tooltip="<['I18N_GALLERY_VIEWS_TOOLTIP' | translate]>"

For placeholders, use the `ng-attr-placeholder` attribute instead of just the attribute `placeholder`. As value for this attribute, apply a translate filter to the key. For example:

    ng-attr-placeholder="<['I18N_FORMS_TYPE_NUMBER' | translate]>"

## Plurals and gender

Angular translate supports pluralization and different genders using the library [messageformat](https://github.com/SlexAxton/messageformat.js/). For example, if you need to translate the html code

    <span ng-if="choices > 1">Select <[choices]> choices.</span>
    <span ng-if="choices == 1">Select one choice.</span>
    <span ng-if="choices == 0">Select no choice.</span>

you have to replace this code for:

    <span translate=”TRANSLATION_KEY” translate-values=”{choicesValue:<[choices]>}” translate-interpolation="messageformat"></span>

and add the translation into the [en.json](https://github.com/oppia/oppia/blob/develop/i18n/en.json) file with the following format:

    “TRANSLATION_KEY”: “{choicesValue, plural, =0{Select no choice.} one{Select one choice.} other{Select # choices.}}”

You can read a more complete tutorial in the [angular translate guide](http://angular-translate.github.io/docs/#/guide/14_pluralization) and the [messageformat documentation](https://github.com/SlexAxton/messageformat.js/). 

## Testing

On an end2end or integration test you can check the page has no untranslated keys. Call the helper function `ensurePageHasNoTranslationIds` in located in the file [general.js](https://github.com/oppia/oppia/blob/develop/core/tests/protractor_utils/general.js).

Also, Karma tests may generate 404 warnings. When the page is loading, the client makes a request for the locale files and, in a test environment, they are not found. To solve this problem add the following line in the first part of your Karma test:

    beforeEach(module('oppia', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));