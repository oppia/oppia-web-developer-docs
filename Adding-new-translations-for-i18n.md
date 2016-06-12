Oppia supports internationalization (i18n) for most of the student-facing pages. The library used for translations is [angular-translate](http://angular-translate.github.io/), you can find more information in the [docs](https://angular-translate.github.io/docs/#/guide). We encourage developers to add new translations of correct existing ones to make the platform available in different languages.

## How to add a new language

To add a new language to the Oppia codebase you just need to:

1. Copy the file [i18n/en.json](https://github.com/oppia/oppia/blob/develop/i18n/en.json) into a new file called xx.json. Replace xx with the language code, you can find the appropriate language code [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Save the file in the same i18n/ directory.
2. Replace all the English translations for the translations in the new language. Is OK if you don't add them all at the same time, but please erase all the English translations from the file. If a translation key is missing, the English translation will be used.
3. In the file [feconf.py](https://github.com/oppia/oppia/blob/develop/feconf.py) locate the variable SUPPORTED_SITE_LANGUAGES. Add a new entry to SUPPORTED_SITE_LANGUAGES using the language code and the language name.

After this, you should be able to see the new language in the Oppia page and translate the site.

## Variable replacement

Inside the translations you can add variables that are going to be replaced for personalized content. For example, in the text

    You have 3 new notifications.

The number of notifications change for each user, and so it can't be included directly in the translation. Angular translate solves this problem by using an interpolation service. Now, you translation is going to look like this:

    You have <[notification_number]> new notifications.

In the html page, the value of the variable notification_number is going to be filled accordingly, and angular translate is going to fill the correct value for you. You can find a more extensive explanation [here](https://angular-translate.github.io/docs/#/guide/06_variable-replacement).

Note that the angular way of marking a variable is with the symbols {{ and }}, but in Oppia's codebase this symbols have been replaced by <[ and ]>.

However, there are some cases when this is not enough. In the example above, if there is only one notification, then we should change the word "notifications" for "notification". Even more, different languages may have more plural forms than English. The solution is to use a different interpolation service, called [messageformat](https://github.com/SlexAxton/messageformat.js/). In this case, the translation is going to look like:

    {notification_number, plural, =0{You have no notifications.} one{You have one notification.} other{You have # notifications.}}

In this example, the # symbol is going to be replaced by the value of the variable notification_number. Both interpolation formats are used inside Oppia. You can read a more complete tutorial in the angular translate [guide for pluralization](http://angular-translate.github.io/docs/#/guide/14_pluralization). 
