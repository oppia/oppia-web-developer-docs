# Tutorial: Making a Simple UI Change

## Introduction

This tutorial guides you through making a simple UI change on the Oppia website. Specifically, we'll update the text on the top of the About page from "Get Started with Oppia" to "Introducing Oppia."

## Skills Covered

1. Figuring out which file(s) in the codebase to modify.
2. Understanding how to work with internationalization (i18n) keys.
3. Manually testing changes in both English and another language.

## Scenario

The UX writing team has filed a request on GitHub asking to update the text on the top of the About page. Let's proceed step by step.

## Procedure

### Stage 1: Figure out the root cause of the issue and which files are affected.

**Setup:**
Start your local Oppia server. If you haven’t installed Oppia on your local machine, please follow the steps in [this wiki page](link-to-installation-wiki).

**Identify the Element:**
Load the /about page on your machine. Can you find the “Get Started with Oppia” text that needs to be changed? Take a moment to locate it before moving forward.

<details>
  <summary>Practice 1</summary>
  <img src="image-link-1" alt="Practice 1 Image">
  The About page opens up. Locate the text (“Get Started with Oppia”) in the first banner on the right.
</details>

<details>
  <summary>Practice 2</summary>
  <img src="image-link-2" alt="Practice 2 Image">
  On the About page, right-click on the "Get Started With Oppia" text and select "Inspect." Can you find the HTML code that corresponds to this text? Look for “Get Started with Oppia” in the HTML code.
</details>

<details>
  <summary>Practice 3</summary>
  <img src="image-link-3" alt="Practice 3 Image">
  Now, open your code editor (such as VS Code). Search for the file that contains the class name "oppia-about-title". Can you identify the specific file where this text is stored? You’ll likely find it in a file named something like `about-page.component.html`.
</details>

### Stage 2: Make the changes

**Understanding i18n Keys:**
In the code file you found, look for a line similar to `<h2 class="oppia-about-title oppia-about-section-title" [innerHTML]="'I18N_ABOUT_PAGE_TITLE_SECTION_ONE' | translate"></h2>`. This line indicates that the text is fetched from an internationalization (i18n) key named `I18N_ABOUT_PAGE_TITLE_SECTION_ONE`.

**Making Changes:**
Search for the `I18N_ABOUT_PAGE_TITLE_SECTION_ONE` key. You’ll get a lot of results for this. Can you find the file which contains the English translations?

<details>
  <summary>Practice 4</summary>
  <img src="image-link-4" alt="Practice 4 Image">
  Open the `en.json` file. Inside, you’ll see multiple i18n keys and their respective translated strings. Look for the key `I18N_ABOUT_PAGE_TITLE_SECTION_ONE`. Currently, it should be assigned to the text "Get Started with Oppia".
</details>

<details>
  <summary>Practice 5</summary>
  <img src="image-link-5" alt="Practice 5 Image">
  Now that you know which key-value pair needs to be altered to get the result, can you change the text from "Get Started with Oppia" to “Introducing Oppia”? Change the value of the key `I18N_ABOUT_PAGE_TITLE_SECTION_ONE` from "Get Started with Oppia" to “Introducing Oppia”. Ensure that the syntax and formatting in the file remain intact while making this change.
</details>

*Note: This tutorial concentrates on modifying the English text, affecting solely the English language version of Oppia.*

**Effect on Other Languages:**
Other language versions will maintain the original text, "Get Started with Oppia", until updated translations are integrated through Translatewiki.

**Translation Integration:**
Translatewiki administrators incorporate modifications made in the English file into other language versions of Oppia.

Refer to the following Oppia Wiki pages to understand I18N development at Oppia:
- [Adding new translations for i18n](link-to-i18n-wiki)
- [How to develop for i18n](link-to-develop-i18n-wiki)

### Stage 3: Verify that your changes are correct

**Testing:**
Open your local Oppia instance and go to the About page. Check that the text now displays as “Introducing Oppia” instead of the original text, when the selected language is English.

<details>
  <summary>Practice 6</summary>
  <img src="image-link-6" alt="Practice 6 Image">
  Try changing the value for the key `I18N_ABOUT_PAGE_TITLE_SECTION_ONE` in some other language file, say Hindi. Change the value to anything, for instance `Getting Started in Hindi`. Now, navigate to the ‘/about’ page in your local server. Change the language of the website from English to Hindi. Do you see the text `Getting Started in Hindi`?
</details>

Remember, take your time with each step, and don’t hesitate to ask for help on [GitHub Discussions](link-to-github-discussions) if something isn’t clear. These changes might seem small, but they’re a great way to start getting comfortable with Oppia’s codebase!
