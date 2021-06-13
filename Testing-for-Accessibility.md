# General Good Practices
* **Every image needs an alt attribute, even if it’s empty:** When you add an image (that is, an img tag) you should consider whether or not an alt description is appropriate. Alt descriptions are useful when the image has important content that isn't described in surrounding text. If an alt description is not appropriate, note that all images must still have an alt attribute. Learn more about determining when an alt description is appropriate through WebAIM: [http://webaim.org/techniques/alttext/#context](http://webaim.org/techniques/alttext/#context)
* **Heading order should make sense:** Every page should have an H1, and the rest of the headings should be in order. We should not use a smaller heading size (e.g. h4) in order to get the font size we want. We should use CSS for that.
* **Every video/audio needs captions or a transcript**
* **Icons that display important information should be read to the user:** In many contemporary web apps, including Oppia, icons and icon fonts are used to denote some important information (such as number of views or dates or something). Unless these icons are accompanied with text (for example, a ratings icon that has a visible label of "Ratings" somewhere), such icons are not read by screenreaders and can leave people feeling confused about what they are listening to. We’ve implemented a fix that uses hidden text to label such icons. These should be used wherever there is iconography (that delivers important content) that is not labeled by visible text. For example:

`<span class="oppia-icon-accessibility-label">Ratings</span>`
* **Consider the implications of dynamic pages:** In Oppia, there are some pages that change their contents dynamically based on an action (e.g. the explorations). This is a feature of many contemporary web apps, however, screenreader users are not able to tell that the page has changed which can lead to confusion and frustration. The accessibility team is working to implement a focus management approach, such that, on change, a screenreader will reread the content. Any other pages and/or new features that include dynamic content changes will need to implement the same approach. 
A focus management approach is described well in this article: [http://simplyaccessible.com/article/spangular-accessibility/ ](http://simplyaccessible.com/article/spangular-accessibility/ )
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
* **Keep focus styles:** Discussed a bit more below, under [Physical Disabilities](#physical-disabilities), but you should generally leave focus styles alone.

You can learn more in our [accessibility talk slides](https://docs.google.com/presentation/d/1Vf_S4Q78Aj_O4t92viCrgX1rkQ0kbMgw4SWcXrnzjDQ/edit#slide=id.p)
# Visual Disabilities
## Test using WAVE Plugin and/or WorldSpace Plugin
The WAVE plugin from WebAIM, a leading accessibility organization, allows you to test a document’s structure, media, and colors to ensure, as much as possible, that it will meet web accessibility standards.
Simply install the plugin in your browser and click it when you have navigated to a page that you want to test.
Generally, it’s a good workflow to use WAVE to fix any structural issues with the site, before moving on to testing with screenreaders. You can find this plugin here: [http://wave.webaim.org/extension/](http://wave.webaim.org/extension/)

The WorldSpace plugin is very similar, but offers even more detailed feedback about the structure of your pages. The WorldSpace plugin is very helpful in discerning whether or not ARIA attributes are being used according to spec. You can find this plugin here: [WorldSpace Attest Documentation](https://dequeuniversity.com/guide/attest-extension/1.1/using/) | [WorldSpace Attest Plugin](https://chrome.google.com/webstore/detail/worldspace-attest-devtool/lfmcehohgifnaodaogknapedjiaoebgo?hl=en-US&gl=US)
## Test using Screenreaders
On a Mac, it’s recommended to use Mac’s built in VoiceOver tool with Safari (this is the combination most blind Mac users use). 

On PC, you may want to use the free and open source NVDA. Good, detailed instructions on how to use these tools are available in this free course from accessibility expert Marcy Sutton on Egghead.io: [https://egghead.io/courses/start-building-accessible-web-applications-today](https://egghead.io/courses/start-building-accessible-web-applications-today).
### What You’re Listening For
**Highly recommend going through the course linked above before attempting**
* Dim the screen of your computer completely and try to navigate the site using only what you can hear. 
* Does the site information read in the correct order?
* Do you know where you are? 
* Does the information you hear make sense?
* Do you know how to get to where you want to go?
## Special Issues for Dynamic Sites/Interactions
Many sites these days or dynamic, or even one page applications. The page content changes, based on user input. The issue with this is that screenreaders don’t necessarily know that the page has been altered. To tackle this problem, there is a general need to manage screenreader focus and, on page change, have the screenreader re-read the content. This kind of focus management also applies to keyboard users.

This focus management approach is well described (focuses on a one-page Angular JS site) in this article: [http://simplyaccessible.com/article/spangular-accessibility/ ](http://simplyaccessible.com/article/spangular-accessibility/ )
 
The Egghead.io course from Marcy Sutton mentioned above also has a video on focus management which may be a helpful resource.
# Physical Disabilities
## Test using keyboard navigation
Some people may not need a screenreader but need to use their keyboard to navigate the page. Test the page using the keyboard.
Typically:
* **Use tab to tab through all of the interactive elements on the screen (and elements that have been pushed into the tab order):** Note that you will not tab through text. Generally, only elements such as links and buttons are accessible via tab.
* **Use enter or space to interact with elements:** A user should be able to expand a dropdown or click on a link or button with their keyboard.
* **Where you are on the page should be visible:** Some sites like to hide the built-in browser focus styles, but it’s important that keyboard users be able to see where they’re focus is on the page.
# Hearing Disabilities
* Auditory media, such as videos, podcasts, etc, should have appropriate alternatives, such as transcripts (which is a full-text representation of what was said) and/or captions (for video, which shows what is being said currently).