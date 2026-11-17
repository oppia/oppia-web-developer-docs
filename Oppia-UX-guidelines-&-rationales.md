## Oppia Design Guidelines

Oppia’s design guidelines are maintained by the UX team and can be found here:
[Oppia Design Guide](https://xd.adobe.com/view/e54eaf14-243c-4cf4-8b9e-d8ff8c6933cc-b01d/grid/).

This is a living document and may be updated over time as design patterns evolve.  
Some sections may be incomplete or subject to change based on ongoing UX discussions.

---

## Guidelines for Modals

Across Oppia, modal dialogs follow consistent closing behaviors to ensure
clarity, accessibility, and a predictable user experience. There are three
main modal patterns:

### 1. Modals with forms
These modals contain user input (for example, text fields or configuration
settings).

- The modal **must only be closed** using:
  - The dedicated close button, or
  - The `ESC` key
- Clicking outside the modal **must not** close it, to avoid accidental data
  loss.

**Example:**

![Form modal example](https://user-images.githubusercontent.com/16653571/52317691-164f7100-29e7-11e9-8da3-7a512e227183.png)

---

### 2. Modals with warnings or suggestions
These modals present information, confirmations, or suggestions to the user.

- The modal **may be closed** by:
  - The dedicated close button
  - Clicking outside the modal (background)
  - Pressing the `ESC` key

This provides flexibility while maintaining user control.

**Example:**

![Warning modal example](https://user-images.githubusercontent.com/16653571/52317811-983f9a00-29e7-11e9-9422-bbc56d7aa4e6.png)

---

### 3. Blocking modals (no close button)
These modals require the user to complete an action before proceeding.

- The modal **cannot be closed manually**
- No close button, background click, or `ESC` key dismissal is allowed

These are used only when an explicit user action is required.

**Example:**

![Blocking modal example](https://user-images.githubusercontent.com/16653571/52318097-dbe6d380-29e8-11e9-95d7-b2ebea58362a.png)
