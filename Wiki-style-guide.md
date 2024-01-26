## Text markup

* Use markdown headers since we can create links to headers in the wiki. This is not possible with long lists or "headers" that are just bold.
* Use quotation marks (`""`) for single-line quotes. This includes button names. Only use inline code markup when readers might have trouble distinguishing similar-looking characters.
  * Do this:

    ```md
    Type in an email address and click "Log in."
    ```

    Rendered:

    Type in an email address and click "Log in."

  * Do not do this:

    ```md
    Type in an email address and click `Log in.`
    ```

    Rendered:

    Type in an email address and click `Log in.`

  * Why: "Log in" is the text on a button, and it is clear without being in a monospaced font..

* Use markdown block quotes for large quotations.

  * Do this:

    ```md
    The Oppia website says:

    > Educators and community members around the world use Oppia's lesson creation platform as a way to create and share lessons. You can find over 20,000 lessons for 17 different subjects in our Exploration library, and maybe you'll be inspired to create your own!
    ```

    Rendered:

    The Oppia website says:

    > Educators and community members around the world use Oppia's lesson creation platform as a way to create and share lessons. You can find over 20,000 lessons for 17 different subjects in our Exploration library, and maybe you'll be inspired to create your own!

  * Do not do this:

    ```md
    The Oppia website says, "Educators and community members around the world use Oppia's lesson creation platform as a way to create and share lessons. You can find over 20,000 lessons for 17 different subjects in our Exploration library, and maybe you'll be inspired to create your own!"
    ```

    Rendered:

    The Oppia website says, "Educators and community members around the world use Oppia's lesson creation platform as a way to create and share lessons. You can find over 20,000 lessons for 17 different subjects in our Exploration library, and maybe you'll be inspired to create your own!"

  * Why: This quote is long, so we should make it a code block instead of surrounding it with quotation marks.


* Use inline code and code block markup (backticks in markdown) only for code, where the text needs to be monospaced (e.g. ASCII art), or where the user needs to be able to distinguish individual characters (e.g. exploration IDs). Don't use backticks when quotes will do.

  * Do this:

    ```md
    Use the exploration ID `YBQ642xYk_4x`.
    ```

    Rendered:

    Use the exploration ID `YBQ642xYk_4x`.

  * Do not do this:

    ```md
    Look for the exploration titled `Quadratic Equations.`
    ```

    Rendered:

    Look for the exploration titled `Quadratic Equations.`

  * Why: Readers might have a hard time distinguishing between similar-looking characters in the exploration ID, so we use inline code markup. The exploration title is clear without markup because readers know how to spell "quadratic equations."

* Use MediaWiki links for internal links (i.e. links from one wiki page to another wiki page).

  * Do this:

    ```md
    See our [[contribution guide|Contributing-code-to-Oppia]] for details.
    ```

    Rendered:

    See our [[contribution guide|Contributing-code-to-Oppia]] for details.

  * Do not do this:

    ```md
    See our [contribution guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) for details.
    ```

    Rendered:

    See our [contribution guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) for details.

  * Why: These links don't include `https://github.com/oppia/oppia/wiki`, so they will still work if we move the wiki to another site, which makes them more robust. The links render exactly the same way as normal Markdown links, so from the reader's perspective there's no difference.

*

## Writing style

* Use sentence case (e.g. "My favorite heading") for headings instead of title case (e.g. "My Favorite Heading").

* Write in complete sentences. However, this rule can be relaxed in lists. For example, this is okay even though "An interactive lesson on Oppia" isn't a sentence:

  > * **Exploration:** An interactive lesson on Oppia.

* Include punctuation at the ends of sentences. Also include punctuation at the ends of phrases that are exceptions to the "Write in complete sentences" rule above. For example, notice the period at the end of the example above.

* Start each page with a bulleted table of contents that follows these rules:

  * The bullets must exactly match the structure of headings in the rest of the file.
  * Each bullet point must be a clickable link that leads to the described heading. The link text must exactly match the text of the heading.
  * Each bullet point link must begin with `#`. In other words, the link must not include the URL protocol, domain, nor file path. This ensures that if the filename changes, the links don't need to be updated.
  * The table of contents must start with a top-level header that reads "Table of contents". This header must not appear in the table of contents.
  * The table of contents may optionally be preceded by some introductory text. This text must not include any headers and should be short.

  You can also use https://ecotrust-canada.github.io/markdown-toc/ to generate a table of contents in this format automatically.

* The top-level headers of your document should be level 2 (i.e. `<h2>` tags created by `##` in Markdown) because GitHub will automatically generate a level 1 heading (i.e. a title) based on the name of the file.
