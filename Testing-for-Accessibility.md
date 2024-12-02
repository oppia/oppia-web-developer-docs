This page details how to develop and test Oppia web pages for accessibility.

As you manually audit each page, please follow the guidelines below, which list the most critical accessibility features we want to ensure Oppia has. Without them, people who rely on screen readers and other aids might not be able to fully navigate the Oppia website. We also recommend reading through [this page](https://www.w3.org/WAI/people-use-web/) by the Web Accessibility Initiative (WAI), and the pages linked from it, to learn more about how people with disabilities use the Web.

## Before you begin

To simulate how low-vision users interact with the website, you will need a screen reader.

- If you're on a Mac, check out [this video on using VoiceOver](https://www.youtube.com/watch?v=5R-6WvAihms&list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g&index=6), the screen reader that comes with Mac OS. You can use this with Safari (this is the combination that most blind Mac users use).
- If you're on a PC, check out [this video on using NVDA](https://www.youtube.com/watch?v=Jao3s_CwdRU&list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g&index=4), a donation-supported, free and open-source screen reader for Windows. 
- If you're on Linux, you can use [ChromeVox](https://chrome.google.com/webstore/detail/chromevox-classic-extensi/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en), a Chrome extension, or [ORCA](https://help.gnome.org/users/orca/stable/introduction.html.en).

Good, detailed instructions on how to use these tools are available in this [free accessibility course](https://egghead.io/courses/start-building-accessible-web-applications-today) by Marcy Sutton on Egghead.io. For more information on accessibility practices, check out this [article on accessibility testing](http://accessibility.voxmedia.com/). 


## Vision Disabilities

### General testing using a screen reader

Follow these steps:
* Dim the screen of your computer completely and try to navigate the site using only what you can hear. 
* Does the site information read in the correct order?
* Do you know where you are? 
* Does the information you hear make sense?
* Do you know how to get to where you want to go?

### Specific test: Interactive elements should indicate their purpose and state
* Interactive elements should indicate their state and be distinguishable from non-interactive elements. 
  * Interactive HTML elements indicate controls in the user interface.
    * Examples of Interactive elements include `<a href>, <button>, <input>, <select>, <textarea>.`
  * Non-interactive HTML elements and non-interactive ARIA roles indicate content and containers in the user interface. 
    * Non-interactive elements include `<main>, <area>, <h1> (<h2>, etc), <img>, <li>, <ul>, <ol>.`
* Screen Reader Test:
  * Navigate to the page and check that screen reader is able to
    * announce the name of each interactive control
    * announce the role of that control
    * announce the current interactive role
    * If it can’t do these things, appropriate ARIA roles need to be added
* **Use ARIA appropriately:** ARIA attributes allows us to label some elements to screenreaders. Screenreader implementation is still a bit spotty, but it’s best to include these, as appropriate, to future proof the design.
  * Note that ARIA attributes have proper hierarchies. The WorldSpace Attest checker is a good resource for checking that your ARIA attributes are used properly.
  * Elements where ARIA attributes are helpful:
    * Modals
    * Navigation menus
    * Footers (if they contain meta info about the site; also note that footers should use the semantic footer tag)
    * Dropdowns
    * Inputs and Forms
    * Buttons
    * Icons that are purely decorative
* **Icons that display important information should be read to the user:** In many contemporary web apps, including Oppia, icons and icon fonts are used to denote some important information (such as number of views or dates or something). Unless these icons are accompanied with text (for example, a ratings icon that has a visible label of "Ratings" somewhere), such icons are not read by screenreaders and can leave people feeling confused about what they are listening to. We’ve implemented a fix that uses hidden text to label such icons. These should be used wherever there is iconography (that delivers important content) that is not labeled by visible text. For example:

`<span class="oppia-icon-accessibility-label">Ratings</span>`

### Specific test: Every image should have an alt attribute, even if it's empty: 
* When you add an image (that is, an img tag) you should consider whether or not an alt description is appropriate. Learn more about determining when an alt description is appropriate through [WebAIM: http://webaim.org/techniques/alttext/#context](http://webaim.org/techniques/alttext/#context). In general, alt descriptions are useful when the image has important content that isn't described in surrounding text.
* If an alt description is not appropriate, note that all images must still have an alt attribute. 

### Specific test: Dynamic pages
* For some Oppia pages (such as the exploration player), the page content changes based on user input. If screenreaders don't know that the page has been altered, this can confuse or frustrate the user. 
* It is important to implement a focus management approach, such that, on a content change, a screenreader will reread the content. An example is described in [Single page applications, Angular.js and accessibility](https://web.archive.org/web/20220206112133/http://simplyaccessible.com/article/spangular-accessibility/ ). The Egghead.io course from Marcy Sutton mentioned above also has a video on focus management which may be a helpful resource. 
* Note that this kind of focus management also applies to keyboard users.


## Keyboard Navigation

Some people may not need a screenreader, but need to use their keyboard to navigate the page. 

To test the page using the keyboard:
* **Use tab to tab through all of the interactive elements on the screen (and elements that have been pushed into the tab order):** Note that you will not tab through text. Generally, only elements such as links and buttons are accessible via tab. Make sure that each interactive element is reachable, and that it has a visual cue that shows it is interactable.
  - It is important that the user can tab through **all** of the features -- if a keyboard user gets trapped on a particular element, they have no way of interacting with the page. Common focus traps include modals, autocomplete widgets, or other widgets. (For modals, users should not be able to leave it just through tabbing, but there should be a way to exit the modal without refreshing the page.)
* **Check that the tab order is logical:** The order in which elements are focused should aim to follow the DOM order. Focus should generally be left to right, top to bottom on the page. If the focus order seems wrong, rearrange the DOM order or change their tabindex to make tab order more natural.
* **Use enter or space to interact with elements:** A user should be able to expand a dropdown or click on a link or button with their keyboard. All interactive controls should be keyboard-focusable. If not reachable, a common fix is to replace custom controls with built-in HTML elements or add the attribute `tabindex=0`.
* **Where you are on the page should be visible:** Some sites like to hide the built-in browser focus styles, but it’s important that keyboard users are able to see where their focus is on the page. When developing, keep existing CSS focus styles as-is (don't remove them).
* **Check that the heading order makes sense.** The heading order should make sense. Every page should have an H1, and the rest of the headings should be in order with no gaps in the hierarchy. When developing, do not use a smaller heading (like h4) in order to get a desired font size; use CSS instead.


## Page Structure Tests

The [WAVE plugin](http://wave.webaim.org/extension/) from WebAIM, a leading accessibility organization, allows you to test a document's structure, media, and colors to ensure, as much as possible, that it will meet web accessibility standards. Simply install the plugin in your browser and click it when you have navigated to a page that you want to test. Generally, it’s a good workflow to use WAVE to fix any structural issues with the site, before moving on to testing with screenreaders. 

The WorldSpace plugin is very similar, but offers even more detailed feedback about the structure of your pages. The WorldSpace plugin is very helpful in discerning whether or not ARIA attributes are being used according to spec. You can find this plugin here: [WorldSpace Attest Documentation](https://dequeuniversity.com/guide/attest-extension/1.1/using/) | [WorldSpace Attest Plugin](https://chrome.google.com/webstore/detail/worldspace-attest-devtool/lfmcehohgifnaodaogknapedjiaoebgo?hl=en-US&gl=US)


## Hearing Disabilities
* To support users with hearing disabilities, any auditory media (videos, audios, podcasts, etc.) should have appropriate alternatives, such as:
  - Transcripts (which is a full-text representation of what was said), and/or
  - Captions (for video, which shows what is being said currently).
