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

## Writing style

* Use sentence case (e.g. "My favorite heading") for headings instead of title case (e.g. "My Favorite Heading").

* Write in complete sentences. However, this rule can be relaxed in lists. For example, this is okay even though "An interactive lesson on Oppia" isn't a sentence:

  > * **Exploration:** An interactive lesson on Oppia.

* Include punctuation at the ends of sentences. Also include punctuation at the ends of phrases that are exceptions to the "Write in complete sentences" rule above. For example, notice the period at the end of the example above.
