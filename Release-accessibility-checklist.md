# Accessibility Manual Tests
## Software Required
### Screen Readers
If you’re on a Mac check out this [this video on using VoiceOver](https://www.youtube.com/watch?v=5R-6WvAihms&list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g&index=6) the screen reader that comes with Mac OS. If you’re on a PC [this video on using NVDA](https://www.youtube.com/watch?v=Jao3s_CwdRU&list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g&index=4), a donation-supported, open-source screen reader for Windows. If you’re on Linux, you can use [ChromeVox](https://chrome.google.com/webstore/detail/chromevox-classic-extensi/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en), a Chrome extension, or [ORCA](https://help.gnome.org/users/orca/stable/introduction.html.en).
## Accessibility Checklist
These are general guidelines you should follow as you manually audit each page.
### 1. Check that the page has a logical tab order
* Tab through the page, the order in which elements are focused should aim to follow the DOM Order
  * If focus order seems wrong, rearrange DOM order or change their tabindex to make tab order more natural
  * Focus should generally be left to right, top to bottom on the page
* Check if all interactive controls are keyboard focusable
  * any control that a user can interact with should be focusable
  * If not reachable, a common fix is to replace custom controls with built-in HTML elements or add the attribute `tabindex=0`

### 2. Check that interactive elements indicate their purpose and state
* Interactive elements should indicate their state and be distinguishable from non-interactive elements. 
  * Interactive HTML elements indicate controls in the user interface.
    * Examples of Interactive elements include `<a href>, <button>, <input>, <select>, <textarea>.`
  * Non-interactive HTML elements and non-interactive ARIA roles indicate content and containers in the user interface.	
    * Non-interactive elements include `<main>, <area>, <h1> (<h2>, etc), <img>, <li>, <ul>, <ol>.`
* A visual and screen reader test should be conducted
* Visual Test:
  * Tab through the page and make sure each interactive element 
    * is reachable
    * has a visual cue that shows it is interactable
* Screen Reader Test:
  * Navigate to the page and check that screen reader is able to
    * announce the name of each interactive control
    * announce the role of that control
    * announce the current interactive role
    * If it can’t do these things, appropriate ARIA roles need to be added
### 3. Check that focus does not get trapped
* If a keyboard user gets trapped on a particular element, they have no way of interacting with the page
* Test it by attempting to navigate through the page with only the keyboard. If you can’t tab through all of the features you fail the test
* Common focus traps are pages that have modals, autocomplete widgets, or other widgets. 
   * For modals these users should not be able to escape it by design, however having a way to escape a modal without refreshing the page should be made. 

### 4. Check that every image has an alt attribute, even if it’s empty: 
* When you add an image (that is, an img tag) you should consider whether or not an alt description is appropriate. 
* Alt descriptions are useful when the image has important content that isn't described in surrounding text. 
* If an alt description is not appropriate, note that all images must still have an alt attribute. Learn more about determining when an alt description is appropriate through [WebAIM: http://webaim.org/techniques/alttext/#context](http://webaim.org/techniques/alttext/#context)

## Additional Accessibility Features
The four points above are the most critical accessibility features we want to ensure Oppia has. Without them, people who rely on screen readers may not be able to fully navigate the Oppia website. For more information on accessibility practices checkout this [article on accessibility testing](http://accessibility.voxmedia.com/) 
