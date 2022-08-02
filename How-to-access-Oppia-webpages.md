## Table of Contents

* [Overview of entities](#overview-of-entities)
* [User account pages](#user-account-pages)
  * [Log in or create account](#log-in-or-create-account)
  * [Log in as a super-administrator](#log-in-as-a-super-administrator)
    * [Using an email with implicit super-admin privileges](#using-an-email-with-implicit-super-admin-privileges)
    * [Grant super-admin privileges after account creation](#grant-super-admin-privileges-after-account-creation)
  * [Delete account page](#delete-account-page)
  * [Preferences page](#preferences-page)
  * [Profile page](#profile-page)
* [Admin pages](#admin-pages)
  * [Super admin page](#super-admin-page)
    * [Assign roles](#assign-roles)
  * [Email dashboard page](#email-dashboard-page)
  * [Release coordinator page](#release-coordinator-page)
* [Static pages](#static-pages)
  * [About page](#about-page)
  * [Donate page](#donate-page)
  * [Contact Page](#contact-page)
  * [Get started page](#get-started-page)
  * [Landing pages](#landing-pages)
  * [Thanks page](#thanks-page)
  * [Terms page](#terms-page)
* [Collection pages](#collection-pages)
  * [Collection editor page](#collection-editor-page)
  * [Collection player page](#collection-player-page)
* [Exploration pages](#exploration-pages)
  * [Community library page](#community-library-page)
  * [Creator dashboard page](#creator-dashboard-page)
  * [Exploration editor page](#exploration-editor-page)
  * [Exploration player page](#exploration-player-page)
* [Topics and skills pages](#topics-and-skills-pages)
  * [Topics and skills dashboard page](#topics-and-skills-dashboard-page)
  * [Topic editor (including preview tab)](#topic-editor-including-preview-tab)
  * [Skill editor page](#skill-editor-page)
  * [Story editor page](#story-editor-page)
  * [Story player page](#story-player-page)
* [Contributor pages](#contributor-pages)
  * [Contributor dashboard page](#contributor-dashboard-page)
  * [Contributor dashboard admin page](#contributor-dashboard-admin-page)

Oppia has many webpages and this is a comprehensive guide on how to access all those pages. Before a contributor makes a PR, we expect that the contributor has thoroughly tested the changes made in the PR for functional correctness. Part of this process is manually testing any pages that are affected by their code.

## Overview of entities

This diagram outlines the various entities in Oppia and how they relate
to each other:

![Flowchart of Oppia entities](images/Webpage-Guide/entitiesHierarchy.png)

As you go through https://www.oppia.org/, you will find these entities.

### Key terms

1. **Topic**: A topic is a broad term that refers to the subject content being taught (e.g. Addition/Subtraction). For example, https://www.oppia.org/learn/math displays a list of math topics. A single topic can be described through multiple stories.
2. **Story**: Stories are situations/scenarios that are meant to help users understand the topic. For example, if the topic is addition, then one of the stories could be about where a kid goes to a shop and buys 3 pens and 4 pencils. The lesson could then explain explain the concept of addition while discussing the total number of items bought. As another example, https://www.oppia.org/learn/math/place-values/story talks about Jaime’s adventures for learning about place values. A single story can be referenced in multiple chapters and is essentially a collection of chapters.
3. **Chapter**: A chapter corresponds to different lessons through which we aim to teach the topic to the users. Each chapter has an associated exploration, and this exploration may have several cards. For example, https://www.oppia.org/learn/math/place-values/story shows a bunch of chapters to learn the place values topic.
4. **Card**: A card is the primary component of an exploration where each card consists of:

   * **Content**: This refers to the tutor’s question to the learner.
   * **Interaction**: Interactions refer to the type of question the users are shown (e.g. multiple-choice, image selection, fraction input, etc.)
   * **Response**: Feedback from Oppia to the learner based on the learner's answer to the interaction.

   For example, [this card](https://www.oppia.org/explore/K645IfRNzpKy?story_url_fragment=jaimes-adventures-in-arcade&topic_url_fragment=place-values&classroom_url_fragment=math&node_id=node_1) shows a card in one of the place values chapters.

### Other terms

1. **Collection**: A group of explorations.
2. **Community**: Anyone who teaches, learns, and contributes to any content on Oppia.
3. **Opportunity**: An opportunity is specific to an exploration, and it refers to a way any contributor can contribute content to Oppia.
4. **Suggestion**: Any time any user contributes to Oppia, their contribution is added as a request which is known as a suggestion. There are two types of suggestions:

   * **Translation suggestion**: A suggested translation of content into another language.
   * **Question suggestion**: A suggested question for a skill.

## User account pages

### Log in or create account

Many Oppia Pages require authentication to access. In order to sign in:

1. Click the sign-in button on the top left navigation bar.

   ![Sign-In Button](images/Webpage-Guide/signInButton.png)

2. Once redirected to the login page, choose an email address and sign in. If you have used this email address before, you will be signed in to the existing account. Otherwise, a new account will be created for you.

   ![Sign-in page](images/Webpage-Guide/nonAdminSignUp.png)

### Log in as a super-administrator

Super-administrators have access to the admin page, where they can set the role of any user. Some of these roles (e.g. "Topic admin") give the user access to privileged pages (e.g. the topics and skills dashboard).

There are two ways to become a super-administrator: use an email address with implicit super-admin privileges, or use the Firebase emulator interface to grant super-admin privileges after the account has been created.

#### Using an email with implicit super-admin privileges

1. Use the email address `testadmin@example.com`. As soon as you type it in, a message should appear saying "This email address has implicit super-admin privileges!".

   ![Sign-in page with implicit super-admin email address](images/Webpage-Guide/implicitSuperAdmin.png)

#### Grant super-admin privileges after account creation

1. Sign in with any email address.

   ![Signing in as a@a.com](images/Webpage-Guide/nonAdminSignUp.png)

2. Go to the Firebase Emulator UI: http://localhost:4000/auth.

   ![Firebase emulator UI](images/Webpage-Guide/firebaseEmulatorUI.png)

3. Find the corresponding Firebase account, click on the "3 dots" button, then click on "Edit user".

   ![Finding the Edit user button](images/Webpage-Guide/firebaseEditUser.png)

4. Set the Custom Claims value to `{"role":"super_admin"}`, then click on the "Save" button.

   ![Setting custom claims](images/Webpage-Guide/firebaseCustomClaims.png)

5. Log out and sign back in to refresh the session cookie.

### Delete account page

The delete account page allows users to delete their accounts. Currently, it is deactivated and certain code needs to be changed to access it.

1. Go to constants.ts and change `ENABLE_ACCOUNT_DELETION` from `false` to `true`.

2. Navigate to http://localhost:8181/delete-account.

### Preferences page

The preferences page allows users to change their settings on oppia.

1. Log in.

2. Go to http://localhost:8181/preferences.

### Profile page

The profile page allows users to view and change their profile on Oppia.

1. Log in.

2. Click on the profile menu and click your username to go to the profile page.

## Admin pages

### Super admin page

The admin page is a page accessible only to super-administrators. It has many functionalities including changing permissions, configuration values, and running jobs. Certain webpages cannot be accessed unless the current user has the required permissions.

1. Log in as a super-admin.

2. Go to the profile menu and click on the "Admin Page" link.

   ![Admin Panel Link](https://user-images.githubusercontent.com/16653571/41501009-e04e9a76-71b9-11e8-958e-985f5bc7122a.png)

#### Assign roles

1. Navigate to the Admin page.

2. Click the "ROLES" tab and enter the username of the user whose roles
   you want to edit.

   ![Admin Role Tab](images/Webpage-Guide/assignRolesEnterUsername.png)

3. Assign the desired role, "Question Admin" in this screenshot:

   ![Assigning role](images/Webpage-Guide/assignRolesAddRole.png)

### Email dashboard page

1. Log in as a super-admin.

2. Navigate to http://localhost:8181/emaildashboard.

### Release coordinator page

1. Log in as a super-admin and assign to your user the "release-coordinator" role.

2. Navigate to http://localhost:8181/release-coordinator.

## Static pages

### About page

The About page provides a brief overview of Oppia. It details the goals of the Oppia organization, credits its contributors, and provides links to guides and tutorials on how to further explore Oppia.

1. Click the "About Menu" button on the top right navigation bar.

2. Click on the "About Oppia" link.

   ![AboutPageLink](images/Webpage-Guide/aboutPageLink.png)

### Donate page

The donate page provides a way for people to donate to the Oppia organization.

1. Go to http://localhost:8181/donate or click on the donate button in the navigation bar.

### Contact Page

The contact page details the ways to communicate with the Oppia team and get involved.

1. Click on the "About" menu at the top navigation bar.

2. Click on the "Contact Us" link.

### Get started page

The get started page provides information for people new to Oppia.

1. Navigate to http://localhost:8181/get-started.

### Landing pages

The landing pages are a series of pages that provide information for people who want to help contribute to Oppia.

1. Navigate to http://localhost:8181/teachers.

### Thanks page

The Thanks page acknowledges people who support Oppia.

1. Go to http://localhost:8181/thanks.

### Terms page

The Terms page addresses the terms and conditions of Oppia.

1. Go to http://localhost:8181/terms.

## Collection pages

### Collection editor page

The Collection editor page allows users to create collections, which group explorations together. The collection editor page can only be accessed by users with the "collection editor" role.

1. Log in as a super-admin and assign yourself the "collection editor" role.

2. Navigate to the splash page (http://localhost:8181/splash).

3. Click on the "Create" button in the top navigation bar.

   ![Create Button](https://user-images.githubusercontent.com/16653571/41504441-a7f60512-720c-11e8-85c2-8fee5f55a42c.png)

4. Select "Create Collection."

   ![CREATE COLLECTION button](https://user-images.githubusercontent.com/16653571/41504483-d946fd3c-720d-11e8-997d-943cd8703e57.png)

### Collection player page

The collection player page allows users to explore collections in Oppia.

1. Log in as a super-admin and assign yourself the "collection editor" role.

2. Go to the admin activities tab and reload the collection "welcome_to_collections.yaml"

   ![Reload Collections](images/Webpage-Guide/reloadCollections.png)

3. Navigate back to the community library page and type in the search bar "collections."

4. Click on the card titled "Introduction to collections in Oppia."

## Exploration pages

### Community library page

The community library page allows users to view and search for explorations on Oppia. "Community" here refers to the Oppia community of teachers, learners, and contributors.

1. Log in.

2. Go to http://localhost:8181/community-library.

The library page has a search bar that lets you search for explorations:

![Library page search bar](images/Webpage-Guide/librarySearch.png)

You can search the library, which consists of all of Oppia's explorations, by entering text, and you can filter by category (also called subject) and language.

### Creator dashboard page

The creator dashboard page allows users to view all explorations they have created, or are currently creating.

1. Log in.

2. Navigate to the creator dashboard page at http://localhost:8181/creator-dashboard.

### Exploration editor page

The exploration editor page allows users to create explorations, or lessons, in Oppia.

1. Log in.

2. Click the "Create" button on the top right to open the exploration editor.

### Exploration player page

The exploration player page allows users to play explorations in Oppia.

1. Navigate to http://localhost:8181/community-library.

2. Enter "fractions" into the search bar.

3. Click on the exploration titled "Fractions 1 - What is the Fraction?"

The exploration will launch in a new tab, where you will see the first card. As you progress through the exploration, you will see subsequent cards, each of which has some content (text, images, videos, or other rich text components). Some will also have interactions like multiple choice questions. A user's answer to these interactions are called "responses."

## Topics and skills pages

### Topics and skills dashboard page

The topics and skills dashboard page allows users to view their created topics and skills, and to create new ones.

1. To access this page, log in as a super-admin and assign yourself the "Curriculum admin" role from the admin page.

2. Go to http://localhost:8181/topics-and-skills-dashboard or click the topic and skills dashboard link on the profile menu.

   ![Topics and skills dashboard link](images/Webpage-Guide/topicAndSkillDashboardLink.png)

### Topic editor (including preview tab)

To access the topic editor/to create new topics, go to the TOPICS tab of topics-and-skills-dashboard page, and click on the "Create New Topic" button.

1. Log in as a super-admin and assign yourself the "Curriculum admin" role.

2. Go to the TOPICS tab of the topics-and-skills-dashboard (http://localhost:8181/topics-and-skills-dashboard) and click on the "Create New Topic" button.

   ![Create button](images/Webpage-Guide/createNewTopic.png)

   The following modal should appear:

   ![Create topic modal](images/Webpage-Guide/createTopicModal.png)

3. After creating a topic, create some skills and assign them to the topic (Note: This step is not necessary for the topic to be published).

4. Edit the topic as required (add subtopics, add a story with a few chapters, etc.) and save the draft when you're satisfied. This will then enable the "Publish topic" button, which you can then use to publish your topic!

5. To preview your topic before publishing, use the preview button on the navbar at the top.

6. To view your published topic on the math classroom page, head to the admin page, and switch to the config tab. Under the **\[topic_ids\]** section of the "The details for each classroom page." property, add the topic id of the topic you just published.

   ![Add topic to classroom](images/Webpage-Guide/addTopicToClassroom.png)

7. Scroll down to the bottom of the page and click on the "Save" button.

8. Go to the math classroom page (http://localhost:8181/learn/math) to find your newly created topic.

### Skill editor page

The skill editor allows the creation of skills in Oppia. You can access the skill editor under the SKILLS tab of the topics-and-skills-dashboard page.

1. Log in as a super-admin and assign yourself the "Curriculum admin" role.

2. Go to http://localhost:8181/topics-and-skills-dashboard and switch to the SKILLS tab.

3. Click on the "Create New Skill" button.

   ![Create new skill button](images/Webpage-Guide/createNewSkill.png)

4. Enter the skill description, save it and wait for the skill editor tab to open.

5. After creating a skill, you can find it in the list of skills under the SKILLS tab. From here, you can also assign it to a topic.

### Story editor page

The story editor page allows users to create stories in Oppia. 

1. Log in as a super-admin and assign yourself the "Curriculum admin" role.

2. Go to http://localhost:8181/topics-and-skills-dashboard and create a topic.

   ![Create topic modal](images/Webpage-Guide/createTopicModal.png)

3. Go to the topic editor and click on the Add Story button.

   ![Add story button](images/Webpage-Guide/addStoryButton.png)

4. Complete the "New story" modal, and wait for the story editor page to load.

   ![Add story modal](images/Webpage-Guide/addStoryModal.png)

### Story player page

The story player allows people to play stories. To access it:

1. Follow the steps to access the story editor page as described above.

2. Add an exploration as a chapter to the story using the add chapter button.
   ![Add chapter button](images/Webpage-Guide/addChapterButton.png)

3. Go to the Preview tab of the Story player using the preview button at the top.

## Contributor pages

### Contributor dashboard page

The contributor dashboard page allows users to translate existing explorations into a different language, or create questions for existing Oppia explorations. This lets more people become "contributors" by helping create Oppia content.

1. Log in.

2. Navigate to the contributor dashboard page at http://localhost:8181/contributor-dashboard.

### Contributor dashboard admin page

1. Log in as a super-admin and assign to your user the "Question admin" role.

2. Navigate to http://localhost:8181/contributor-dashboard-admin.
