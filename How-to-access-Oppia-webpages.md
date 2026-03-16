## Table of Contents
- [Overview of entities](#overview-of-entities)
  * [Key terms](#key-terms)
  * [Other terms](#other-terms)
- [User account pages](#user-account-pages)
  * [Log in or create account](#log-in-or-create-account)
  * [Log in as a super-administrator](#log-in-as-a-super-administrator)
    + [Method A — Implicit super admin email (fast):](#method-a---implicit-super-admin-email--fast--)
    + [Method B — Grant super admin via Firebase emulator (explicit):](#method-b---grant-super-admin-via-firebase-emulator--explicit--)
- [Oppia Webpages](#oppia-webpages)
  * [Admin pages](#admin-pages)
    + [Important admin page tabs](#important-admin-page-tabs)
  * [Classroom admin page](#classroom-admin-page)
  * [Collection editor page:](#collection-editor-page-)
    + [Ways to generate collections:](#ways-to-generate-collections-)
  * [Collection player](#collection-player)
  * [Community library](#community-library)
  * [Contributor admin dashboard](#contributor-admin-dashboard)
  * [Contributor dashboard](#contributor-dashboard)
    + [Tabs on the Contributor dashboard page:](#tabs-on-the-contributor-dashboard-page-)
    + [Ways to Generate Contributions](#ways-to-generate-contributions)
  * [Creator dashboard](#creator-dashboard)
  * [Delete account page](#delete-account-page)
  * [Preferences Page](#preferences-page)
  * [Profile page](#profile-page)
  * [Release Coordinator Page](#release-coordinator-page)
    + [Tabs on the release coordinator page:](#tabs-on-the-release-coordinator-page-)
  * [Skill editor page](#skill-editor-page)
  * [Story editor page](#story-editor-page)
  * [Story player page](#story-player-page)
  * [Topics & skills dashboard](#topics---skills-dashboard)
- [Public informational pages](#public-informational-pages)
  * [About](#about)
  * [Android](#android)
  * [Contact](#contact)
  * [Creator Guidelines](#creator-guidelines)
  * [Diagnostic Test Player](#diagnostic-test-player)
  * [Donate](#donate)
  * [Get Started](#get-started)
  * [License](#license)
  * [Maintenance Page](#maintenance-page)
  * [Partnerships](#partnerships)
  * [Privacy Policy](#privacy-policy)
  * [Teach](#teach)
  * [Terms of Use](#terms-of-use)
  * [Thank You](#thank-you)
  * [Volunteer](#volunteer)
- [Authentication pages](#authentication-pages)
  * [Signup](#signup)
- [Dashboard pages](#dashboard-pages)
  * [Blog Dashboard](#blog-dashboard)
  * [Facilitator Dashboard](#facilitator-dashboard)
  * [Learner Dashboard](#learner-dashboard)
- [Admin & Moderation routes](#admin---moderation-routes)
  * [Blog Admin](#blog-admin)
  * [Email Dashboard](#email-dashboard)
  * [Moderator](#moderator)
  * [Voiceover Admin](#voiceover-admin)
- [Editor routes](#editor-routes)
  * [Exploration Editor](#exploration-editor)
  * [Topic Editor](#topic-editor)
- [Topics, practice & Learning pages](#topics--practice---learning-pages)
  * [Practice Session](#practice-session)
  * [Review Test](#review-test)
  * [Study Guide](#study-guide)
  * [Topic Viewer](#topic-viewer)
- [Classrooms & Learning paths](#classrooms---learning-paths)
  * [All Classrooms](#all-classrooms)
  * [Classroom Page](#classroom-page)
- [Exploration & Lesson players](#exploration---lesson-players)
  * [Embedded Exploration Player](#embedded-exploration-player)
  * [New Lesson Player](#new-lesson-player)
  * [Old Exploration Player](#old-exploration-player)
- [Library & Collections](#library---collections)
  * [Library Search](#library-search)
  * [Recently Published](#recently-published)
  * [Top Rated](#top-rated)
- [Blog routes](#blog-routes)
  * [Blog Homepage](#blog-homepage)
  * [Blog Search](#blog-search)
  * [Blog Author Profile](#blog-author-profile)
  * [Individual Blog Post](#individual-blog-post)
- [Learner group routes](#learner-group-routes)
  * [Create Learner Group](#create-learner-group)
  * [Edit Learner Group](#edit-learner-group)
    + [Tabs on edit learner group:](#tabs-on-edit-learner-group-)
  * [View Learner Group](#view-learner-group)
- [Account & Profile routes](#account---profile-routes)
  * [Feedback Updates](#feedback-updates)
  * [Pending Account Deletion](#pending-account-deletion)
- [Error handling routes](#error-handling-routes)
  * [Custom Error Pages](#custom-error-pages)
  * [Iframe Error Page](#iframe-error-page)
  * [404 Not Found](#404-not-found)
- [Populating Data on Local Server](#populating-data-on-local-server)
  * [1. Admin Activities Tab (Dummy/Test Data)](#1-admin-activities-tab--dummy-test-data-)
    + [Generate Dummy Explorations](#generate-dummy-explorations)
    + [Reload a Single Exploration](#reload-a-single-exploration)
    + [Reload a Single Collection](#reload-a-single-collection)
    + [Load Dummy New Structures Data](#load-dummy-new-structures-data)
  * [2. Creating Explorations](#2-creating-explorations)
  * [3. Creating a Skill](#3-creating-a-skill)
  * [4. Creating a topic](#4-creating-a-topic)
  * [5. Generating Data For Contributor Dashboard](#5-generating-data-for-contributor-dashboard)
  * [6. Creating collections](#6-creating-collections)
    + [Using the collection editor:](#using-the-collection-editor-)
    + [Using activities tab](#using-activities-tab)
  * [7. Creating a classroom](#7-creating-a-classroom)
    + [Creating a custom classroom](#creating-a-custom-classroom)
    + [Creating a dummy math classroom](#creating-a-dummy-math-classroom)
  * [8. Community library](#8-community-library)
  * [9. Collection player](#9-collection-player)
  * [10. Story player](#10-story-player)
  * [11. Fixing this common error](#11-fixing-this-common-error)
- [Oppia Routing Guide for Contributors](#oppia-routing-guide-for-contributors)
  * [1. What Is Routing in Oppia?](#1-what-is-routing-in-oppia-)
  * [2. Route Protection (Guards)](#2-route-protection--guards-)
    + [2.1 IsLoggedInGuard](#21-isloggedinguard)
    + [2.2 LessonPlayerPageAuthGuard](#22-lessonplayerpageauthguard)
    + [2.3 NormalizeUrlCaseGuard](#23-normalizeurlcaseguard)
  * [3. Public Pages (No Login Required)](#3-public-pages--no-login-required-)
  * [4. Authentication pages](#4-authentication-pages)
  * [5. Dashboard pages (Require Login)](#5-dashboard-pages--require-login-)
  * [6. Admin & Moderation routes (Require Login)](#6-admin---moderation-routes--require-login-)
  * [7. Editor routes (Require Login)](#7-editor-routes--require-login-)
  * [8. Topics, practice & Learning pages (Public)](#8-topics--practice---learning-pages--public-)
  * [9. Classrooms & Learning paths](#9-classrooms---learning-paths)
  * [10. Exploration & Lesson players](#10-exploration---lesson-players)
  * [11. Library & Collections](#11-library---collections)
  * [12. Blog routes](#12-blog-routes)
  * [13. Learner group routes](#13-learner-group-routes)
  * [14. Account & Profile routes](#14-account---profile-routes)
  * [15. Special dynamic routes](#15-special-dynamic-routes)
    + [15.1 Stewards Landing Pages](#151-stewards-landing-pages)
    + [15.2 Topic Landing Pages](#152-topic-landing-pages)
  * [16. Error handling routes](#16-error-handling-routes)
  * [17. Why this routing file Is critical](#17-why-this-routing-file-is-critical)
  * [18. Role-based access control](#18-role-based-access-control)
  * [19. Troubleshooting tips](#19-troubleshooting-tips)
  * [20. Quick reference for contributors](#20-quick-reference-for-contributors)
  * [21. Contributor Checklist](#21-contributor-checklist)
  * [22. Summary](#22-summary)

  
## Overview of entities

This diagram outlines the various entities in Oppia and how they relate
to each other:

```mermaid
flowchart TD
C("Classroom") --> T1("Topic-1")
C --> T2("Topic-2")
C --> T3("Topic-3")
T1 --> S1("Story-1")
T1 --> S2("Story-2")
S1 --> C1("Chapter-1/Exploration")
C1 --> c1("Card-1")
C1 --> c2("card-2")
S1 --> C2("chapter-2")
C2 --> c3("Card-3")
c3 --> co("Content")
c3 --> in("Interaction")
in --> mc("Multiple-choice")
in --> is("Image Selection")
in --> fi("Fraction-input")
in --> oqt("other question types")
S2 --> C3("Chapter-3")
S2 --> C4("Chapter-4")
C3 --> c4("Card-4")
C4 --> c5("Card-5")
C4 --> c6("Card-6")
```
As you go through https://www.oppia.org/, you will find these entities.

### Key terms

1. **Classroom**: A Classroom in Oppia is a collection of topics grouped under a single subject. For example: https://www.oppia.org/learn/math this displays a Maths classroom.
2. **Topic**: A topic is a broad term that refers to the subject content being taught. For example: https://www.oppia.org/learn/math displays a list of math topics.A single topic can be described through multiple stories.
3. **Story**: Stories are situations/scenarios that are meant to help users understand the topic. For example, if the topic is addition, then one of the stories could be about where a kid goes to a shop and buys 3 pens and 4 pencils. The lesson could then explain the concept of addition while discussing the total number of items bought. As another example, https://www.oppia.org/learn/math/place-values/story talks about Jaime’s adventures for learning about place values. A single story can be referenced in multiple chapters and is essentially a collection of chapters.
4. **Chapter**: A chapter corresponds to different lessons through which we aim to teach the topic to the users. Each chapter has an associated exploration, and this exploration may have several cards. For example, https://www.oppia.org/learn/math/place-values/story shows a bunch of chapters to learn the place values topic.
5. **Card**:
A card is the primary component of lesson where each card consists of:

   - **Content**: This refers to the tutor’s question to the learner.
   - **Interaction**: Interactions refer to the type of question the users are shown (e.g. multiple-choice, image selection, fraction input, etc.)
   - **Response**: Feedback from Oppia to the learner based on the learner's answer to the interaction.

   For example, [this card](https://www.oppia.org/explore/K645IfRNzpKy?story_url_fragment=jaimes-adventures-in-arcade&topic_url_fragment=place-values&classroom_url_fragment=math&node_id=node_1) shows a card in one of the place values chapters.

### Other terms

1. **Collection**: A collection is a group of related lessons arranged in a sequence. They don’t appear inside classrooms — instead, learners usually find them in the Community Library. For Example: https://www.oppia.org/collection/4UgTQUc1tala A Fractions collection with lessons like “What are Fractions?” and “Comparing Fractions.”
2. **Opportunity**: An opportunity is specific to an exploration, and it refers to a way any contributor can contribute content to Oppia.
3. **Suggestion**: Any time any user contributes to Oppia, their contribution is added as a request which is known as a suggestion. There are two types of suggestions:
   * **Translation suggestion**: A suggested translation of content into another language.
   * **Question suggestion**: A suggested question for a skill.
4. **Contributor** Anyone who pitches in content for an exploration/lesson. One way that Oppia is more of a collaborative learning space, in contrast to more traditional online learning platforms.
5. **Exploration** The fundamental unit of learning on Oppia. This is an interactive activity built by a creator, and consumed by a learner. 
6. **Library** The page where all explorations and collections on Oppia are displayed.
7. **Interaction** The interactive component of a card; this is the medium through which a learner communicates to a student by asking various types of questions and through which student can answer these question.
8. **Learner** A user who engages in an exploration or lesson.
9. **Response** Feedback and/or a new card that the learner is directed to based on their answer. A response can’t be empty; if a response doesn’t direct the learner to a new card, then feedback must be provided.
10. **Rule** A condition that triggers a response. Different interactions have different rule options. Multiple rules can be grouped together in a single answer group.
11. **Tags** Additional labels that can be added to an exploration in order to make it more findable in the community library.
   
## User account pages

### Log in or create account

Many Oppia Pages require authentication to access. In order to sign in:

1. Click the sign-in button on the top left navigation bar.

   ![Sign-In Button](images/Webpage-Guide/signInButton.png)

2. Once redirected to the login page, choose an email address and sign in. If you have used this email address before, you will be signed in to the existing account. Otherwise, a new account will be created for you.
   
   ![Sign-in page](images/Webpage-Guide/nonAdminSignUp.png)

### Log in as a super-administrator

Super Admin can:
- Access the Admin page
- Assign roles to users
- Run dummy data generation jobs
  
Some of these roles (e.g. "Topic admin") give the user access to privileged pages (e.g. the topics and skills dashboard).

There are two ways to become a super admin on the local server.

#### Method A — Implicit super admin email (fast):
1. On the sign-in page, enter testadmin@example.com.
2. A message will appear: "This email address has implicit Super Admin privileges!" — you now have Super Admin access.

   ![Sign-in page with implicit super-admin email address](images/Webpage-Guide/implicitSuperAdmin.png)

#### Method B — Grant super admin via Firebase emulator (explicit):

1. Sign in with any email address.

   ![Signing in as a@a.com](images/Webpage-Guide/nonAdminSignUp.png)

2. Go to the Firebase Emulator UI: http://localhost:4000/auth.

   ![Firebase emulator UI](images/Webpage-Guide/firebaseEmulatorUI.png)

3. Find the corresponding Firebase account, click on the "3 dots" button, then click on "Edit user".

   ![Finding the Edit user button](images/Webpage-Guide/firebaseEditUser.png)

4. Set the Custom Claims value to `{"role":"super_admin"}`, then click on the "Save" button.

   ![Setting custom claims](images/Webpage-Guide/firebaseCustomClaims.png)

5. Log out and sign back in to refresh the session cookie.

## Oppia Webpages 

### Admin pages

- **Description:**
The Admin page is where Super Admin manage roles, run dummy data generation jobs and reload prebuilt content.

- **Url:** 
http://localhost:8181/admin

- **Permissions Required:**
Super Admin only.

- **Steps to Access:**
1. Log in as a super-admin.
2. Go to the profile menu and click on the "Admin Page" link.

   ![Admin Panel Link](https://user-images.githubusercontent.com/16653571/41501009-e04e9a76-71b9-11e8-958e-985f5bc7122a.png)

#### Important admin page tabs
**Assign roles** 

- **Description:** 
Allows Super Admin to assign roles such as Curriculum Admin, Question Admin, or Release Coordinator.

- **Url:**
http://localhost:8181/admin (Roles tab)

- **Permissions Required:**
Super Admin only.

- **Steps to Access:**
1. Navigate to the Admin page.
2. Click the "ROLES" tab and enter the username of the user whose roles
   you want to edit.

   ![Admin Role Tab](images/Webpage-Guide/assignRolesEnterUsername.png)

3. Assign the desired role, "Question Admin" in this screenshot:

   ![Assigning role](images/Webpage-Guide/assignRolesAddRole.png)

**Activities**

- **Description:**
This page allows Super Admin to generate, reload, or seed data on the local  development server, such as explorations, collections, skills, topics, and  classrooms.

- **Url:**
http://localhost:8181/admin (ACTIVITIES tab)

- **Permissions Required:**
Super Admin

- **Steps to Access:** 
1. Log in as a super-admin.
2. Navigate to /admin.
3. Click on the ACTIVITIES tab.
4. Choose the required data generation or reload action.

![Activities](images/Webpage-Guide/adminactivities.png)

**Platform Parameters** 

- **Description:**
This page displays platform-level configuration parameters that control feature flags and site behavior across Oppia. Admins can view platform configuration parameters. Some values may be editable depending on the environment.

- **Url:**
http://localhost:8181/admin (PLATFORM PARAMETERS tab)

- **Permissions Required:**
Super Admin

- **Steps to Access:**
1. Log in as a super-admin.
2. Open /admin.
3. Navigate to the PLATFORM PARAMETERS tab.
4. Review or update configuration values as required.

![Platform Parameters](images/Webpage-Guide/adminplatform.png)

**Misc Tab**

- **Description:**
This page contains advanced admin tools used to maintain, debug, and manage Oppia’s internal data.
These tools are mainly for super-admins and developers, and are usually used during development, testing, data fixes, or emergency maintenance.
Most learners and creators will never need to use this page.

- **Url:**
http://localhost:8181/admin → MISC tab

- **Permissions Required:**
Super Admin

- **Steps to Access:**
1. Log in as a super-admin
2. Navigate to /admin
3. Open the MISC tab

![Misc tab](images/Webpage-Guide/adminmisc.png)

### Classroom admin page

- **Description:**
This page allows Curriculum Admins to create and manage classrooms, assign  topics, and configure classroom content displayed to learners.

- **Url:**
http://localhost:8181/classroom-admin

- **Permissions Required:**
Curriculum Admin role

- **Steps to Access:**

1. Log in as a super-admin.
2. Assign yourself the Curriculum Admin role.
3. Navigate to /classroom-admin.
4. Create or edit classrooms and assign topics.

![Classroom admin](images/Webpage-Guide/classroomadmin.png)

### Collection editor page:

- **Description:**
This page allows creators to create and edit collections, which are ordered groups of explorations designed to guide learners through a learning path.

- **Url**: 
http://localhost:8181/collection_editor/create/<collection_id>

- **Permissions Required:**
Collection Editor 

- **Steps to Access:**
1. Log in to Oppia.
2. Navigate to /creator-dashboard.
3. Click Create New Collection.
4. You will be redirected to the Collection Editor page.

![Collection editor](images/Webpage-Guide/collectioneditor.png)

#### Ways to generate collections:
See [Populating Data on Local Server](#populating-data-on-local-server).

### Collection player
- **Description:**
This page displays a learner-facing view of a collection, allowing learners to play explorations in sequence.

- **Url:**
http://localhost:8181/collection/<collection_id>

- **Permissions Required:**
Public (no login required)

- **Steps to Access:**
1. Ensure a collection is published.
2. Navigate to /community-library.
3. Search for the collection.
4. Open the collection to start learning.

![Collection player](images/Webpage-Guide/collections.png)

### Community library

- **Description:**
The Community Library allows users to browse, search, and filter explorations and collections available on Oppia.

- **Url:**
http://localhost:8181/community-library

- **Permissions Required:**
Public (no login required)

- **Steps to Access:**
1. Open Oppia in a browser.
2. Navigate to /community-library.
3. Use filters or search to find learning content.
   
![Community library](images/Webpage-Guide/communitylibrary.png)

### Contributor admin dashboard

- **Description:**
This is used to manage community reviewer permissions. It allows administrators to grant or revoke question review and translation review rights to trusted contributors.

- **Url:**
http://localhost:8181/contributor-admin-dashboard

- **Permissions Required:**
Question Admin or Translation Admin.

- **Steps to Access:**
1. Assign yourself the Question Admin role/Translation Admin.
2. Navigate to /contributor-admin-dashboard

![Contributor admin dashboard](images/Webpage-Guide/contributordashboardadmin.png)

### Contributor dashboard

- **Description:**
Allows contributors to submit translation suggestions and questions.

- **Url:**
http://localhost:8181/contributor-dashboard

- **Permissions Required:**
Logged-in users.

- **Steps to Access:**
1. Log in to Oppia.
2. Navigate to /contributor-dashboard.

![Contributor dashboard](images/Webpage-Guide/mycontributions.png)

#### Tabs on the Contributor dashboard page:

- **My Contributions** 
This is your personal dashboard where you can track your history and impact. It is divided into three sections (visible in the side-nav):

1. **Contributions:** 
Shows the status of everything you have submitted (e.g., translations or 
questions). You can see if they are "Accepted," "Rejected," or "In Review."
![translations](images/Webpage-Guide/translations.png)
2. **Available Tasks:** 
If you have been granted "Reviewer" rights by an admin, this section shows you a list of other people's contributions that need your approval.                                   
- Question Review Rights
This permission allows users to review question suggestions submitted by other contributors.
- Translation Review Rights
This permission allows users to review translation suggestions in specific languages.    
![translations](images/Webpage-Guide/reviewtranslations.png)

3. **Accomplishments:** 
Displays your overall contribution Stats and any Badges you have earned for your work.
![Badges](images/Webpage-Guide/Badges.png)
- **⁠⁠Translate Text**
This is where the actual work happens for translators.
It shows a list of Opportunities (lessons that need to be translated into your chosen language).
You can use the Language and Topic filters at the top to find specific lessons you want to work on.
Clicking Translate on any item will open the translation editor for that lesson.

Note: The "Available Tasks" section in the Contributor Dashboard becomes visible when a user has reviewer permissions. 
![Translate Text](images/Webpage-Guide/translatetext2.png)
#### Ways to Generate Contributions
 See [Populating Data on Local Server](#populating-data-on-local-server).

### Creator dashboard
- **Description:**
This dashboard allows creators to manage explorations and collections they have created, including drafts and published content.

- **Url:**
http://localhost:8181/creator-dashboard

- **Permissions Required:**
Logged-in users

- **Steps to Access:**
1. Log in to Oppia.
2. Navigate to /creator-dashboard.
   - Create, edit, or manage your explorations and collections.

 ![Creator dashboard](images/Webpage-Guide/creatordashboard.png)

### Delete account page

- **Description:** 
This page allows signed-in learners to request deletion of their account.
In local development, the account may be deleted immediately. On production, the deletion request can be marked as pending and processed later.

- **Url:** 
http://localhost:8181/delete-account

- **Permissions Required:**
Learners must be signed in.

- **Steps to Access:** 
1. Log in to Oppia.
2. Navigate to /preferences.(Preferences page)
3. On that page there is Delete button.
   
When the user clicks this button, they are taken to the Delete Account page, where they can confirm the deletion.
Follow the on-screen confirmation steps.

**Note**:
On local servers, deletion may happen immediately.
On production, deletion requests may remain pending.

![Delete account page](images/Webpage-Guide/deleteaccount.png)

### Preferences Page

- **Description:**
This page allows learners to change their settings on Oppia, such as language preference and email preferences.

- **Url:**
http://localhost:8181/preferences

- **Permissions Required:**
No special permissions. Any signed-in learner can access it.

- **Steps to Access:**
1. Log in to Oppia.
2. Open the top-right profile menu
3. Click Preferences.

![Preferences page](images/Webpage-Guide/preferences.png)

### Profile page

- **Description:** 
This page displays a learner’s profile. It shows their username, bio, badges, and created lessons.

- **Url:** 
http://localhost:8181/profile/<username>

- **Permissions Required:** 
No special permissions. Public profiles are viewable by anyone.

- **Steps to Access:** 
1. Log in to Oppia
2. Click your username in the top-right menu

![Profile page](images/Webpage-Guide/profilepage.png)

### Release Coordinator Page

- **Description:**
This page helps admins manage important release-related tasks in Oppia.
It is used to clear caches, manage features, and make sure everything works properly after new changes. Admins mostly use it during development, testing, and when releasing updates.

- **Url:**
http://localhost:8181/release-coordinator

- **Permissions Required:**
Release Coordinator role

- **Steps to Access:**
1. Log in as a Super Admin.
2. Assign yourself the Release Coordinator role via Admin → Roles.
3. Navigate to /release-coordinator.
4. Use tools such as Flush Cache under the MISC tab.

#### Tabs on the release coordinator page:

1. **Features Tab**
It is used to enable, disable, and control feature flags.
It helps roll out new features gradually using:
- rollout percentage
- user groups
- force-enable options
It prevents breaking the site by testing features on limited users first


Example:
 Enable a new UI feature only for 10% of users before full release.

![Features](images/Webpage-Guide/releasefeatures.png)

2. **Beam Jobs tab**
It is used to start and monitor background jobs.
These jobs run long tasks like:
- Data migrations
- Batch updates
- Cleanup tasks           

It shows job status such as:
- Running
- Completed
- Failed
Example:
 Run a migration job after changing the database structure.

![Beam jobs](images/Webpage-Guide/beamjobs.png)

3. **Misc tab**
   
It contains release utility tools
It is used mainly for maintenance and debugging
Includes:
- Flush Memory Cache – clears cached data so new changes take effect
- Get Memory Cache Profile – shows what data is stored in cache
- Promo Bar controls – display site-wide announcements
- Manage User Groups – create groups used by feature flags

Example:
 Flush cache when local server shows outdated data.

![Misc tab](images/Webpage-Guide/releasecoordinator.png)

### Skill editor page
- **Description:** 
The skill editor allows the creation of skills in Oppia. You can access the Skills editor under the skills tab of topics-and-skills-dashboard page.

- **Url:**
http://localhost:8181/skill_editor/<skill_id>

- **Permissions Required:**
Curriculum Admin role.

- **Steps to Access:**
1. Open the Topics & Skills Dashboard.
2. Go to the ADD SKILL .
   ![ADD SKILL](images/Webpage-Guide/skilleditor1.png)
3. New Skill modal will pop up.
4. Once you click on Save button of the modal,a new tab will be opened.
5. That will be Skill Editor page.
   
![Skill editor](images/Webpage-Guide/skilleditor2.png)

### Story editor page

- **Description:**
This allows the user to create stories in Oppia.

- **Url:**
http://localhost:8181/story_editor/<story_id>

- **Permissions Required:**
Curriculum Admin role

- **Steps to access:** 
1. Navigate to /topics-and-skills-dashboard.
2. Create a topic.
   ![createTopicModal](images/Webpage-Guide/createTopicModal.png)

3. Go to the topic editor and click on the add story button.
   ![canonicalstories](images/Webpage-Guide/canonicalstories.png)
4. Complete the “New story” modal and wait for the story editor page to load.

![New story](images/Webpage-Guide/storyeditor3.png)

### Story player page

- **Description:** 
Displays the learner-facing view of a story and its chapters.

- **Url:**
/learn/<classroom_url_fragment>/<topic_url_fragment>/story/<story_url_fragment>

- **Permissions Required:**
Public (no login required)

- **Steps to Access:**
1. Navigate to the Learn page.
2. Click on a Classroom (for example, "Math").
3. Click on a Topic (for example, "Multiplication").
4. Click "Continue" on a Story.
5. The Story Player page opens.
![Story player page](images/Webpage-Guide/storyplayer.png)

### Topics & skills dashboard 

- **Description:** 
The central hub for Curriculum Admins to create and manage Topics (and their stories) and Skills.

- **Url:**
http://localhost:8181/topics-and-skills-dashboard

- **Permissions Required:**
Curriculum Admin role.

- **Steps to Access:**
1. Log in as a Super Admin.
2. Assign yourself the Curriculum Admin role.
3. Navigate to /topics-and-skills-dashboard.


![Topics & skills dashboard](images/Webpage-Guide/topicsandskillsdashboard.png)

## Public informational pages

### About

- **Description:** 
Provides information about the Oppia Foundation, its mission, team, and Impact.  

- **Url:** 
/about

- **Permissions Required:** 
None

- **Steps to Access:** 
 1. Click About in the Navbar.

![About page](images/Webpage-Guide/about.png)

### Android

- **Description:** 
Landing page for the Oppia Android app, allowing users to download the app and view its features.

- **Url:** 
/android

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click LEARN in the navbar.
2. Click try it today.
   
![Android page](images/Webpage-Guide/android.png)

### Contact

- **Description:** 
Allows users to contact the Oppia team, submit feedback, and learn how to get involved with the Oppia project.

- **Url:** 
/contact

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Get Involved in the navbar.
2. Then click on Contact Us.

![Contact page](images/Webpage-Guide/contact.png)

### Creator Guidelines

- **Description:** 
Provides instructions and best practices for participating in the community and creating explorations.

- **Url:** 
 /creator-guidelines

- **Permissions Required:** 
 None

- **Steps to Access:** 
1. Click Creator-guidelines in the footer.

![Creator Guidelines](images/Webpage-Guide/creatorguidelines.png)

### Diagnostic Test Player

- **Description:** 
An interactive interface where learners take diagnostic tests to assess their knowledge of prerequisite skills before starting a topic. The test results determine which topics are recommended.

- **Url:**
/diagnostic-test-player?classroom=<classroom_url>

- **Permissions Required:**
None (Public route)

​​However, the Diagnostic Test will only function properly if:
- Diagnostic Test is enabled in the Classroom Admin page
- The topic is published
- Skills are assigned under the Diagnostic Tests section
- Each skill has at least 3 questions
- Topic is added to the classroom

If any of these are missing, the page may load but not behave correctly.

- **Steps to Access:**

1. Navigate to the classroom page.
2. On the classroom page, click Take quiz.
   ![classroom page](images/Webpage-Guide/diagnostic1.png)
   
3. The Diagnostic Test Player will open.
   ![Diagnostic Test Player](images/Webpage-Guide/diagnosticplayer.png)

How to Enable Diagnostic Test
1. Go to /classroom-admin.
2. Click on the classroom tile (e.g., Math)
3. Click the pencil icon to enter Edit Mode
4. Scroll to Diagnostic Test Status
5. Toggle from Disabled → Public
6. Click Save
   
![Enable Diagnostic Test](images/Webpage-Guide/diagnosticenable.png)

### Donate

- **Description:** 
Explains how community can support or align with Oppia Foundation's mission. 

- **Url:**   
/donate

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Donate in the Navbar.

![ Donate page](images/Webpage-Guide/donate.png)

### Get Started

- **Description:** 
Provides guidance on how to begin using Oppia as a contributor.

- **Url:** 
/get-started

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Get Started in the footer

![Get Started page](images/Webpage-Guide/getstarted.png)

### License

- **Description:** 
Details the licenses under which Oppia’s content and software are released.

- **Url:** 
/license

- **Permissions Required:** 
None

- **Steps to Access:** 
 1. Linked from the image receiver or audio uploader components during the creation process.

![License page](images/Webpage-Guide/license.png)

### Maintenance Page

- **Description:**
Displayed when Oppia is in maintenance mode. Shows a message that the site is temporarily unavailable.

- **Url:**
/maintenance

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. This page is automatically displayed when the server is in maintenance mode
2. For testing, admins can start the server with python -m scripts.start --prod_env --maintenance_mode.
3. OR directly visit http://localhost:8181/maintenance

**NOTE:** Maintenance mode only works with --prod_env flag. That's why the server is started with python -m scripts.start --prod_env --maintenance_mode.
![Maintenance Page](images/Webpage-Guide/maintenance.png)

### Partnerships

- **Description:** 
Provides information for organizations interested in partnering with Oppia to help students access education.

- **Url:** 
/partnerships

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Get Involved in the navbar.
2. Then click on the Schools and Organizations.
![Partnerships page](images/Webpage-Guide/partnerships.png)

### Privacy Policy

- **Description:** 
Explains how Oppia collects, uses, and protects user data.

- **Url:** 
/privacy-policy

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Privacy Policy in the footer.

![Privacy Policy page](images/Webpage-Guide/privacypolicy.png)

### Teach

- **Description:** 
Provides resources and guidance for teachers who want to use Oppia in their classrooms or create educational content.

- **Url:** 
/teach

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click For Parents/Teachers in the footer.
![Teach](images/Webpage-Guide/teach.png)

### Terms of Use

- **Description:** 
Defines the legal terms and conditions for using the Oppia platform.

- **Url:**
/terms

- **Permissions Required:** 
None

- **Steps to Access:** 
 1. Click Terms of Service in the footer.

![Terms of Use](images/Webpage-Guide/terms.png)

### Thank You

- **Description:** 
Confirmation page displayed after a successful donation.

- **Url:**
/thanks

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Users are redirected automatically after completing a donation.

![Thank You page](images/Webpage-Guide/thankyou.png)

### Volunteer

- **Description:** 
Provides information on how to join the Oppia community as a volunteer and contribute in various roles.

- **Url:** 
/volunteer

- **Permissions Required:** 
None

- **Steps to Access:** 
1. Click Get Involved in the navbar.
2. Then click on the Volunteer.

![Volunteer page](images/Webpage-Guide/volunteer.png)


## Authentication pages

### Signup

- **Description:**
Account creation page where new users can register for an Oppia account.

- **Url:**
/signup

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Click "Sign In" button
2. On the login page, enter a new email address
3. Complete the signup flow (username selection, terms acceptance)

![Signup Page](images/Webpage-Guide/signup.png)

## Dashboard pages 

### Blog Dashboard

- **Description:**
Management interface for blog authors to create, edit, and publish blog posts.

- **Url:**
/blog-dashboard

- **Permissions Required:**
Blog Editor role

- **Steps to Access:**
1. Log in as a Super Admin
2. Assign yourself the Blog Editor role via /admin → Roles
3. Navigate to http://localhost:8181/blog-dashboard

![Blog Dashboard](images/Webpage-Guide/blogdashboard.png)

### Facilitator Dashboard

- **Description:**
A dashboard for classroom facilitators to manage learner groups, track student progress, and assign lessons.

- **Url:**
/facilitator-dashboard

- **Permissions Required:**
Logged-in users with Full User Role.

- **Steps to Access:**
1. Log in as a Super Admin, navigate to /release-coordinator -> Features tab, and enable the Learner Groups flag (internally learner_groups_are_enabled).
2. Ensure your user account has the Full User role (assigned via the Admin -> Roles tab).
3. Navigate to http://localhost:8181/facilitator-dashboard
(Requires facilitator role to access full features)

![Facilitator Dashboard](images/Webpage-Guide/Facilatordashboard.png)

### Learner Dashboard

- **Description:**
The learner's personal homepage showing their learning progress, goals, ongoing lessons, recommended topics, and achievements.

- **Url:**
/learner-dashboard

- **Permissions Required:**
Logged-in users

- **Steps to Access:**
1. Log in to Oppia
2. Click the Oppia logo or "Home" link
OR directly visit http://localhost:8181/learner-dashboard

![Learner Dashboard](images/Webpage-Guide/leanerdashboard.png)

## Admin & Moderation routes

### Blog Admin

- **Description:**
Administrative dashboard for managing blog settings, categories, featured posts, and blog-wide configurations.

- **Url:**
/blog-admin

- **Permissions Required:**
Blog Admin role

- **Steps to Access:**
1. Log in as a Super Admin
2. Assign yourself the Blog Admin role via /admin → Roles
3. Navigate to http://localhost:8181/blog-admin

![Blog Admin](images/Webpage-Guide/blogadmin.png)

### Email Dashboard

- **Description:**
Interface for managing and sending bulk emails to specific user groups or the entire Oppia community.

- **Url:**
/emaildashboard

- **Permissions Required:**
Admin privileges

- **Steps to Access:**
1. Log in as a Super Admin
2. Navigate to http://localhost:8181/emaildashboard

![Email Dashboard](images/Webpage-Guide/emaildashboard.png)

### Moderator

- **Description:**
Page for moderators to manage explorations and user feedback.

- **Url:** 
/moderator

- **Permissions Required:**
Moderator

- **Steps to Access:** 
1. Click Moderator Page in the side navigation bar.

![Moderator](images/Webpage-Guide/moderator.png)

### Voiceover Admin

- **Description:**
Administrative tool for managing voiceover recordings, reviewing submitted voiceovers, and assigning voiceover tasks.

- **Url:**
/voiceover-admin

- **Permissions Required:**
Voiceover Admin role

- **Steps to Access:**
1. Log in as a Super Admin
2. Assign yourself the Voiceover Admin role via /admin → Roles
3. Navigate to http://localhost:8181/voiceover-admin

![Voiceover Admin](images/Webpage-Guide/voiceoveradmin.png)

## Editor routes

### Exploration Editor

- **Description:**
The exploration editor is where creators build interactive lessons. It includes a card-based interface for adding content, interactions, and feedback paths.

- **Url:**
/create/<exploration_id>

- **Permissions Required:**
Logged-in users (exploration owner or collaborators)

- **Steps to Access:**
1. Log in to Oppia
2. Navigate to Creator Dashboard (/creator-dashboard)
3. Click "Create Exploration"
4. OR open an existing exploration from your dashboard

![Exploration Editor](images/Webpage-Guide/explorationeditor.png)

### Topic Editor

- **Description:**
Interface for creating and managing topics, including subtopics, stories, skills, and diagnostic test configuration.

- **Url:**
/topic_editor/<topic_id>

- **Permissions Required:**
Curriculum Admin role

- **Steps to Access:**
1. Log in as a Super Admin
2. Assign yourself the Curriculum Admin role
3. Navigate to Topics and Skills Dashboard
4. Click on an existing topic OR create a new one
5. The Topic Editor page will open

![Topic Editor](images/Webpage-Guide/topiceditor1.png)

## Topics, practice & Learning pages

### Practice Session

- **Description:**
An interactive practice session where learners answer practice questions to reinforce their understanding of a topic's skills.

- **Url:**
/learn/<classroom_url>/<topic_url>/practice

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to a Topic Viewer page
2. Go to Practice Tab
3. Click "Start"
4. Answer questions related to the topic

Example:
 http://localhost:8181/learn/math/fractions/practice

![Practice Session](images/Webpage-Guide/practicesession.png)

### Review Test

- **Description:**
A test that learners can take after completing a story to review what they've learned.

- **Url:**
/learn/<classroom_url>/<topic_url>/review-test/<story_url>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Complete a story
2. Click "Take Review Test" at the end of the story
3. The review test player will load

Example:
http://localhost:8181/learn/math/fractions/review-test/introduction-to-fractions

### Study Guide

- **Description:**
Displays detailed study materials, explanations, and worked examples for a specific subtopic.

- **Url:**
/learn/:classroom_url_fragment/:topic_url_fragment/studyguide/:subtopic_url_fragment

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to a Topic Viewer page
2. Click on a subtopic from the list
3. The study guide for that subtopic will load

Example:
 http://localhost:8181/learn/math/fractions/studyguide

 ![Study Guide](images/Webpage-Guide/studyguide.png)

### Topic Viewer

- **Description:**
Displays a topic's details, stories, practice sessions, and study materials for learners.

- **Url:**
/learn/<classroom_url>/<topic_url>/story

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to /learn (Classrooms page)
2. Click on a classroom (e.g., "Math")
3. Click on a topic (e.g., "Fractions")

Example:
http://localhost:8181/learn/math/fractions/story

![Topic Viewer](images/Webpage-Guide/topicviewer.png)
 
## Classrooms & Learning paths

### All Classrooms

- **Description:**
Landing page showing all available classrooms (Math, Science, etc.) that learners can explore.

- **Url:**
/classrooms

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Click "Learn" in the navigation bar
2. OR directly visit http://localhost:8181/classrooms

![All Classrooms](images/Webpage-Guide/allclassrooms.png)

### Classroom Page

- **Description:**
Individual classroom landing page displaying all topics within that classroom, along with the classroom description and learning path.

- **Url:**
/learn/<classroom_url>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to /classrooms
2. Click on a classroom card (e.g., "Math")

Example:
 http://localhost:8181/learn/math

![Classroom Page](images/Webpage-Guide/learn:math.png)

## Exploration & Lesson players

### Embedded Exploration Player

- **Description:**
A stripped-down version of the exploration player designed to be embedded in external websites via iframe.

- **Url:**
/embed/exploration/<exploration_id>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Directly visit http://localhost:8181/embed/exploration/<exploration_id>
2. OR embed in an iframe:

![Embedded Exploration Player](images/Webpage-Guide/embedexploration.png)

### New Lesson Player

- **Description:**
The modern lesson player interface with improved UX for playing explorations.

- **Url:**
/lesson/<exploration_id>

- **Permissions Required:**
Public (with authorization check)

- **Steps to Access:**
1. Navigate through a classroom → topic → story → chapter
2. Click on a chapter to launch the lesson player

![New Lesson Player](images/Webpage-Guide/newlessonplayer.png)

### Old Exploration Player

- **Description:**
The legacy exploration player interface for playing individual explorations (lessons).

- **Url:**
/explore/<exploration_id>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Find an exploration in the Community Library
2. Click "Play" on the exploration
3. OR directly visit http://localhost:8181/explore/<exploration_id>

![Old Exploration Player](images/Webpage-Guide/oldexploration.png)

## Library & Collections

### Library Search

- **Description:**
Search interface for finding specific explorations in the Oppia library by keywords, categories, or language.

- **Url:**
/search/find

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to Community Library (/community-library)
2. Use the search bar at the top
3. OR directly visit http://localhost:8181/search/find?q=<search_term>

![Library Search](images/Webpage-Guide/explorationsearch.png)

### Recently Published

- **Description:**
Shows a list of explorations that have been recently published to the community library.

- **Url:**
/community-library/recently-published

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to Community Library
2. Click "Recently Published" tab or filter
3. OR directly visit http://localhost:8181/community-library/recently-published
   ![Recently Published](images/Webpage-Guide/recentlypublished.png)
   
### Top Rated

- **Description:**
Displays the highest-rated explorations based on learner feedback and ratings.

- **Url:**
/community-library/top-rated

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to Community Library
2. Click "Top Rated" tab or filter
3. OR directly visit http://localhost:8181/community-library/top-rated
   
## Blog routes

### Blog Homepage

- **Description:**
The main blog page displaying recent blog posts, featured articles, and blog categories.

- **Url:**
/blog

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Click "Blog" in the navigation bar
2. OR directly visit http://localhost:8181/blog
   
![Blog Homepage](images/Webpage-Guide/bloghomepage.png)

### Blog Search

- **Description:**
Search interface for finding blog posts by keywords, tags, or author.

- **Url:**
/blog/search/find

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to Blog homepage (/blog)
2. Use the search bar
3. Enter search terms and submit

![Blog Search](images/Webpage-Guide/blogsearch.png)

### Blog Author Profile

- **Description:**
Displays a blog author's profile, including their bio, published posts, and author information.

- **Url:**
/blog/author/<author_username>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to any blog post
2. Click on the author's name
3. OR directly visit http://localhost:8181/blog/author/<username>

![Blog Author Profile](images/Webpage-Guide/blogauthor.png)

### Individual Blog Post

- **Description:**
Displays a single blog post with its full content, images, and comments.

- **Url:**
/blog/<blog_post_slug>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Navigate to Blog homepage
2. Click on a blog post title
3. OR directly visit http://localhost:8181/blog/<slug>

![Individual Blog Post](images/Webpage-Guide/individualblog.png)

## Learner group routes

### Create Learner Group

- **Description:**
Interface for facilitators to create a new learner group, add members, and assign lessons.

- **Url:**
/create-learner-group

- **Permissions Required:**
Logged-in users with the Full User role.

- **Steps to Access:**
1. Log in to Oppia
2. Navigate to Facilitator Dashboard
3. Click "Create Learner Group"
4. OR directly visit http://localhost:8181/create-learner-group

![Create Learner Group](images/Webpage-Guide/createlearnergroup.png)

### Edit Learner Group

- **Description:**
Allows facilitators to edit learner group details, manage members, and update assigned lessons.

- **Url:**
/edit-learner-group/<group_id>

- **Permissions Required:**
The user must be the Facilitator of that specific group.

- **Steps to Access:**
1. Navigate to Facilitator Dashboard
2. Click on a learner group
3. Click "Edit Group"
   
![Edit Learner Group](images/Webpage-Guide/editleanergroup.png) 

#### Tabs on edit learner group:

1. Overview (currently active)
Shows a high-level summary of the group with two sub-tabs:
      - Skills Analysis — Shows common skills that learners in this group           are struggling with. Helps facilitators identify weak areas.
      - Progress in Stories — Shows how learners are progressing through            the assigned stories/chapters.
2. Learners' Progress
Tracks individual learner progress. You can see:
 - Which stories each learner has completed
 - Which skills they've mastered or are struggling with
 - Overall completion percentages

   ![Learners' Progress](images/Webpage-Guide/leanergroupprogress.png)
   
 3. Syllabus
Manage the group's learning content:
 - Add/remove stories — Assign stories from topics for learners to work through
 - Add/remove skills — Assign specific skills for practice

![Syllabus](images/Webpage-Guide/leaenergroupsyllabus.png)

4. Preferences
Group settings including:
 - Edit the group title and description
 - Invite learners by username
 - Remove learners from the group
 - Delete the group entirely

![Preferences](images/Webpage-Guide/learnergrouppreferences.png)

### View Learner Group

- **Description:**
Displays learner group information, member progress, and group activities.

- **Url:**
/learner-group/<group_id>

- **Permissions Required:**
Group members or facilitators

- **Steps to Access:**
1. Navigate to Facilitator Dashboard (for facilitators)
2. OR access via shared group link (for members)
3. Click on the group to view details

![View Learner Group](images/Webpage-Guide/viewgroup.png)

## Account & Profile routes

### Feedback Updates

- **Description:**
Shows a history of feedback the user has received on their explorations, questions, or translations.

- **Url:**
/feedback-updates

- **Permissions Required:**
Logged-in users

- **Steps to Access:**
1. Log in to Oppia
2. Click the notification bell icon
3. Click "View All Feedback"
4. OR directly visit http://localhost:8181/feedback-updates

![Feedback Updates](images/Webpage-Guide/feedback.png)

### Pending Account Deletion

- **Description:**
Displayed after a user requests account deletion. Shows the deletion status and estimated completion time.

- **Url:**
/pending-account-deletion

- **Permissions Required:**
None (Public - shown after deletion request)

- **Steps to Access:**
1. User is automatically redirected here after requesting account deletion
2. OR directly visit http://localhost:8181/pending-account-deletion

![Pending Account Deletion](images/Webpage-Guide/pendingaccountdeletion.png)

## Error handling routes

### Custom Error Pages

- **Description:**
Custom error pages for specific HTTP error codes (400, 401, 500, etc.) with helpful messages and recovery options.

- **Url:**
/error/<status_code>

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. These pages are automatically displayed when the corresponding error occurs
2. For testing, visit http://localhost:8181/error/404 or /error/500

![Custom Error Pages](images/Webpage-Guide/404error.png)

### Iframe Error Page

- **Description:**
A special error page designed to display within iframes without breaking the parent page.

- **Url:**
/error/iframed

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. This page is automatically shown when an error occurs within an embedded Oppia iframe
2. OR directly visit http://localhost:8181/error/iframed

![Iframe Error Page](images/Webpage-Guide/iframeerror.png)

### 404 Not Found

- **Description:**
The default 404 page shown when a user navigates to a non-existent URL.

- **Url:**
** (Wildcard route – catches all undefined paths)

- **Permissions Required:**
None (Public)

- **Steps to Access:**
1. Visit any non-existent URL
2. Example: http://localhost:8181/this-page-does-not-exist

## Populating Data on Local Server

This section explains all the ways data can be created, loaded, or generated on the Oppia local development server.

### 1. Admin Activities Tab (Dummy/Test Data)
The Activities tab is ONLY for local testing and development.
It does not create real, customizable content.

**Access:**
Visit [Activities](#activities).

#### Generate Dummy Explorations
- Creates random, empty explorations
- Optional auto-publish

**Use case:** Quick testing of dashboards and flows

#### Reload a Single Exploration

- Reloads predefined YAML explorations
- Example: welcome.yaml

**Use case:** Restore known test content

#### Reload a Single Collection
- Loads predefined collections from YAML
- Example: welcome_to_collections.yaml

**Limitations:**
- Cannot edit structure
- Cannot choose explorations
- Cannot create new collections

#### Load Dummy New Structures Data
Loads a complete dataset, including:
- Topics
- Skills
- Stories
- Explorations
- Questions

**Use case:** Populate everything in one click for local testing

**Prerequisite: Assign Required Roles**

Most data population actions require specific roles.
 To assign roles, see [Assign roles](#important-admin-page-tabs).

### 2. Creating Explorations

An Exploration is the actual lesson that learners play. Stories, chapters, and practice sessions all depend on explorations.

**Step 1:** Open Creator Dashboard
Go to:
http://localhost:8181/creator-dashboard
Click:
“Create Exploration”

**Step 2:** Choose Interaction Type
You will be asked to select:

- Multiple Choice
- Text Input
- Fraction Input
- Drag & Drop
- Image Selection, etc.

Click Create
 **Step 3:** Add Content to the Card
 Each card contains:
 
- Content → The question shown to the learner
- Interaction → How the learner answers
- Response → Feedback after submission

You must:

1. Enter the question
2. Configure learner answer input
3. Add feedback response

Click Save Draft

**Step 4:** Add More Cards (Optional)
Click:
“Add New Card”

Repeat the process to create multi-step lessons.

**Step 5:** Preview the Exploration
Click the Preview button to test like a learner.

**Step 6:** Publish the Exploration
Click:
Publish
If it is not published:
- It will NOT appear in stories
- It will NOT be visible to learners

**Step 7:** Use Exploration in a Story
Once published:

1. Go to Topic Editor
2. Open a Story
3. Add a Chapter
4. Select your published Exploration
5. Save draft → Publish topic again if needed

### 3. Creating a Skill
                NOTE - A skill must have:
- At least **3 questions** to appear in the **Diagnostic Test**
- At least **10 questions** to appear in **Practice Sessions**

**Note**
Even after adding 10 questions to the skills in a topic, the Practice Session route will return a 404 until you open the Topic Editor and explicitly check the "Show Practice Tab to learners" checkbox. This checkbox remains disabled until the 10-question minimum is met.

There are two ways to create a skill:

**Method 1: From Topic Editor**
1. Open any Topic Editor
2. Click ADD SKILL under the Subtopics section
3. The skill will be automatically assigned to the topic

**Method 2: From Topics and Skills Dashboard**
1. Go to the dashboard
2. Click ADD SKILL
3. This skill will not be assigned to any topic automatically
   ![ADD SKILL](images/Webpage-Guide/newskill.png)
4. After saving, you will be taken to the Skill Editor page.
5. Sections Inside the Skill Editor:
- Details
  ![Details](images/Webpage-Guide/populatingdetails.png)
- Worked Example
![Worked Example](images/Webpage-Guide/workedexample.png)

- Misconceptions
These are common mistakes learners make.
You can force these misconceptions to appear in all questions.

![Misconceptions](images/Webpage-Guide/misconception.png)

- Pre-requisite Skills
These are skills learners should complete first.
You can filter by:
- Topic
- Subtopic
- Skill name

![Pre-requisite Skills](images/Webpage-Guide/prerequisiteskills.png)

- Rubrics
Helps question creators follow defined standards.

![Rubrics](images/Webpage-Guide/rubrics.png)

**Adding Questions to a Skill**
1. Scroll to the Questions section
2. Click ADD QUESTION
3. Inside the Question Editor, fill these 5 parts:
- Difficulty
                        
![Difficulty](images/Webpage-Guide/difficulty.png)

- Problem

![Problem](images/Webpage-Guide/skilleditor.png)

- Interaction
![Interaction](images/Webpage-Guide/interaction.png)

- Answers and Responses
  Hints
![ADD Hints](images/Webpage-Guide/addhint.png)

- After filling everything, click Save

![Save](images/Webpage-Guide/creatingtopicsave.png)

### 4. Creating a topic
1. Open the Topics and Skills Dashboard.
2. Click on CREATE TOPIC.
3. A form will open where you need to fill:
- Topic name
- Topic thumbnail
- Other required details.
  ![create topic](images/Webpage-Guide/createtopic.png)
4. After saving, you will be redirected to the Topic Editor page.    

![Topic Editor page](images/Webpage-Guide/topiceditor.png)

5. In the main editor tab, you will see validation errors that must be fixed before publishing.

![warnings](images/Webpage-Guide/warnings.png)
     
Sections in the Topic Editor:
- **Details** – Basic information about the topic
- **Subtopics** – Lists subtopics and the skills linked to them
![Subtopics](images/Webpage-Guide/subtopics.png)
- **Diagnostic Tests-**
Add skills that will be used to test learners before recommending this topic.
A skill must have at least 3 questions and be assigned to the topic to be used here.
![Diagnostic Tests](images/Webpage-Guide/diagnostictest.png)
-**Canonical Stories**-
This section lists all stories that belong to this topic.

![Canonical Stories](images/Webpage-Guide/canonicalstories.png)

- Preview the Topic
  
1. Click the Preview button in the top navigation bar
2. This shows exactly how learners will see your topic before publishing.
![Preview the Topic](images/Webpage-Guide/topicpreview.png)
- Publish the Topic
Once all validation errors are resolved:
1. Click Publish Topic
2. Your Topic is now live in the system.

- Add the Published Topic to the Math Classroom
To make your topic visible on the Math Classroom page:

1. Go to http://localhost:8181/classroom-admin
2. Select the classroom (e.g. Math)
3. Click edit (pencil icon)
4. Add the published Topic ID
5.Save changes

- Verify on the Math Classroom Page
 Go to:
http://localhost:8181/learn/math

 You should now see your newly created topic listed on the classroom page.

### 5. Generating Data For Contributor Dashboard

- My Contributions
**Steps to generate data:**
1. Log in to Oppia.
2. Navigate to the Contributor Dashboard
3. Open the Translate Text tab.
4. Select:
- A Topic
- A Target Language (for example, Hindi).
  ![Translate Text tab](images/Webpage-Guide/translatetext.png)
5. Choose an Opportunity (an exploration lesson that requires translation).
6. Enter a translation for the text.
7. Click Save and Close.
![Translate Text tab](images/Webpage-Guide/hinditranslatetext.png)

**Available Tasks (Reviewer Rights Required)**
The Available Tasks section displays suggestions submitted by other users that require review.
This section is visible only to users with Reviewer Rights.

1. Navigate to the Admin page
2. Open the Roles tab.
3. Enter your username.
4. Select one of the following roles:
      - Translation Admin
      - Question Admin
5. Click Update.
6. Navigate to the Contributor Admin Dashboard
7. In Manage Contributor Rights:

Enter your username.
Select a category:
     - Translation Reviewer
     - Question Reviewer
     Select a language (for example, Hindi).
     Click Add Rights.
 ![Contributor Rights](images/Webpage-Guide/contributorhindireview.png)
8. Log in with a different account(or open an incognito window).
9. Submit a translation or question suggestion using the steps described in Populating My Contributions.
 ![Contributor Rights](images/Webpage-Guide/acceptedtranslation.png)
10. Log back in with the reviewer account.
11. Open the Available Tasks tab.
12. You should now see the submitted suggestion available for review.

 ![reviewtranslations](images/Webpage-Guide/reviewtranslations.png)
 
**Accomplishments**

The Accomplishments tab tracks contributor statistics and badges based on accepted contributions.

Steps to generate data:
1. Log in as a user with Reviewer Rights.
2. Navigate to Available Tasks on the Contributor Dashboard.
3. Review a submitted suggestion.
4. Click Accept.

Result:
- The contributor’s statistics will update in the Accomplishments tab.
- Badges will be awarded automatically when contribution milestones are reached (for example, 50 accepted translations).

**Note**
The Available Tasks section remains hidden until reviewer permissions are granted through the Contributor Admin Dashboard.

### 6. Creating collections
 #### Using the collection editor:
1. Log in to Oppia
2. ⁠Navigate to /creator-dashboard
3. ⁠Click the "+ CREATE EXPLORATION" button
4. ⁠A modal appears: "Create an Activity"
5. Select "New Collection"
6. Click "CREATE COLLECTION"
7. You will be redirected to the Collection Editor page
   
**Note:** Despite the button saying "Create Exploration", it opens a modal where you can choose to create either an Exploration OR a Collection 
                     
  #### Using activities tab
     This is NOT used to create new collections manually.
1. Log in to Oppia
2. Navigate to /admin
3. The Activities tab is only for loading or reloading predefined (dummy) collections from YAML files
4. These collections are meant for testing, demos, or local development.
What you can do here:
- Reload an existing test collection (e.g. welcome_to_collections.yaml)

 ![collection](images/Webpage-Guide/activitiescollection.png)
 
### 7. Creating a classroom
Step 1: Assign Role
1. Go to /admin
2. Assign yourself the Curriculum Admin role
#### Creating a custom classroom
1. Open /classroom-admin
2. Click Add New Classroom
  ![Add New Classroom](images/Webpage-Guide/creatingclassroom1.png)
   **Enter:**
     - Classroom name
     - URL fragment
 ![Classroom name](images/Webpage-Guide/creatingclassroomaddnew.png)
     - Click on the classroom title
     - Click the pencil icon to edit details
 ![classroom title](images/Webpage-Guide/creatingclassroommath1.png)
**Add:**
- Course details
- Topic introduction
- Topic IDs
 ![creating classroom math](images/Webpage-Guide/creatingclassroommath.png)
####  Creating a dummy math classroom
1. Go to /admin → ACTIVITIES
2. Click Load Dummy Classroom Data

 ![Dummy math classroom](images/Webpage-Guide/generatingdummymath.png)

The classroom will be visible on:
- The Learner Dashboard Home Tab
- OR directly at:
http://localhost:8181/learn/<classroom_url_fragment>

**NOTE:** Learner-facing pages do not create data themselves.
They display data created via creator or admin flows.

### 8. Community library
Populated when:
- Explorations are published
- Collections are published

### 9. Collection player
Populated when:
- A published collection exists
- Created via Collection Editor or Activities (dummy)

### 10. Story player
Populated when:
- Topic is published
- Story and chapters are added
- Explorations are linked

### 11. Fixing this common error
**Error:**
Server error: 'NoneType' object has no attribute 'version'

**Fix:**
1. Go to /admin → Roles
2. Assign yourself the release-coordinator role
3. Open /release-coordinator
4. Under the MISC tab, click Flush Cache.
   
 ![Flush Cache](images/Webpage-Guide/flushcache.png)

## Oppia Routing Guide for Contributors

This guide explains how routing works in Oppia and documents all available routes in the application.

### 1. What Is Routing in Oppia?

Routing in Oppia determines:
- What page opens when you visit a URL
- Whether login is required to access the page
- Which Angular module is loaded for that route
  
**Lazy Loading** 
Oppia uses lazy loading, which means:
- A page module is only loaded when it is actually visited
- This improves performance and reduces initial memory usage
- Each route uses loadChildren to dynamically import its module
  
### 2. Route Protection (Guards)
Oppia uses three main guards to control access:

#### 2.1 IsLoggedInGuard

**Purpose:** Blocks the page unless the user is logged in. If not logged in, redirects to /login.

**Used for:**
- Admin pages (/admin)
- Creator dashboard (/creator-dashboard)
- Topic / Skill / Story editors
- Blog management pages
- Learner dashboard
- Most contributor tools

#### 2.2 LessonPlayerPageAuthGuard

**Purpose:** Ensures only authorized access to lesson playback.

**Used for:**
- New lesson player (/lesson/<id>)
- Embedded lesson player (/embed/lesson/<id>)

#### 2.3 NormalizeUrlCaseGuard

**Purpose:** Ensures URL casing is correct to prevent routing bugs.
**Used for:**

- Classroom route (/learn/<classroom_url>)

### 3. Public Pages (No Login Required)
These pages are accessible to everyone without authentication:
| Route | Purpose |
|------|---------|
| /about | About Oppia |
| /contact | Contact page |
| /donate | Donation page |
| /get-started | New user onboarding |
| /teach | Teaching resources |
| /thanks | Thank-you page |
| /terms | Legal terms |
| /privacy-policy | Privacy policy |
| /license | Open-source license |
| /volunteer | Volunteer portal |
| /creator-guidelines | Participation playbook |
| /android | Android app info |
| /partnerships | Partnerships information |
| /contributor-dashboard | Contributor dashboard (no router guard)\* |
| /diagnostic-test-player | Diagnostic test player |
| /maintenance | Maintenance page |

**Note:** /contributor-dashboard does not have IsLoggedInGuard at the routing level, though it may check login status internally.

### 4. Authentication pages
         
| Route | Purpose |
|------|---------|
| /signup | Account creation |

### 5. Dashboard pages (Require Login)
  
| Route | Purpose | Guard |
|------|---------|-------|
| /creator-dashboard | For exploration creators | IsLoggedInGuard |
| /learner-dashboard | Learner homepage | IsLoggedInGuard |
| /facilitator-dashboard | Classroom facilitators | IsLoggedInGuard |
| /blog-dashboard | Blog post management | IsLoggedInGuard |

### 6. Admin & Moderation routes (Require Login)
     All of these require IsLoggedInGuard:         
| Route | Purpose |
|------|---------|
| /admin | Main admin panel |
| /moderator | Content moderation |
| /emaildashboard | Email management |
| /voiceover-admin | Voiceover management |
| /topics-and-skills-dashboard | Topic & skill management (Curriculum Admin only) |
| /classroom-admin | Classroom management (Curriculum Admin only) |
| /contributor-admin-dashboard | Admin control of contributors |
| /blog-admin | Blog administration |

**Note:** /release-coordinator does not have IsLoggedInGuard at the routing level.

### 7. Editor routes (Require Login)
All editor routes require IsLoggedInGuard:

| Route | Editor Type |
|------|-------------|
| /exploration_editor/create/<id> | Exploration editor |
| /collection_editor/create/<id> | Collection editor |
| /story_editor/<id> | Story editor |
| /topic_editor/<id> | Topic editor |
| /skill_editor/<id> | Skill editor |

### 8. Topics, practice & Learning pages (Public)
These learning pages are public and do not require login:
         
| Route | Purpose |
|------|---------|
| `/learn/<classroom_url>/<topic_url>` | Topic viewer |
| `/learn/<classroom_url>/<topic_url>/story/<story_url>` | Story viewer |
| `/learn/<classroom_url>/<topic_url>/practice` | Practice session |
| `/learn/<classroom_url>/<topic_url>/review-test/<story_url>` | Review test |
| `/learn/<classroom_url>/<topic_url>/studyguide/<subtopic_url>` | Subtopic viewer (study guide) |

Example:
/learn/math/fractions shows the Fractions topic in the Math classroom.

### 9. Classrooms & Learning paths
        
| Route | Purpose | Guard |
|------|---------|-------|
| `/classrooms` | All classrooms | Public |
| `/learn/<classroom_url>` | Classroom landing page | Public (NormalizeUrlCaseGuard) |
| `/classroom-admin` | Classroom management | IsLoggedInGuard |

### 10. Exploration & Lesson players

| Route | Purpose | Guard |
|------|---------|-------|
| `/explore/<id>` | Old exploration player | Public |
| `/embed/exploration/<id>` | Embedded exploration player | Public |
| `/lesson/<id>` | New lesson player | LessonPlayerPageAuthGuard |

### 11. Library & Collections

| Route | Purpose |
|------|---------|
| `/community-library` | Exploration library |
| `/search/find` | Library search |
| `/community-library/recently-published` | Recently published explorations |
| `/community-library/top-rated` | Top rated explorations |
| `/collection/<id>` | Collection player |

### 12. Blog routes  
        
| Route | Purpose |
|------|---------|
| `/blog` | Blog homepage |
| `/blog/search/find` | Blog search |
| `/blog/author/:author_username` | Author profile |
| `/blog/<slug>` | Individual blog post |

### 13. Learner group routes

| Route | Purpose | Guard |
|------|---------|-------|
| `/create-learner-group` | Create group | IsLoggedInGuard |
| `/edit-learner-group/<id>` | Edit group | IsLoggedInGuard |
| `/view-learner-group/<id>` | View group | No guard* |

**Note:** /view-learner-group does not have IsLoggedInGuard at the routing level.

### 14. Account & Profile routes

| Route | Purpose | Guard |
|------|---------|-------|
| `/preferences` | Account preferences | No guard* |
| `/profile/<username>` | User profile | Public |
| `/delete-account` | Delete account | IsLoggedInGuard |
| `/pending-account-deletion` | Deletion waiting page | Public |
| `/feedback-updates` | Feedback history | IsLoggedInGuard |

**Note:** /preferences does not have IsLoggedInGuard at the routing level, though it typically requires login to function.

### 15. Special dynamic routes

#### 15.1 Stewards Landing Pages

Old volunteer URLs are automatically redirected to /volunteer. This includes:
- /parents
- /partners
- /nonprofits
- /teachers
- /volunteers
This redirection happens through a loop in the routing configuration.

#### 15.2 Topic Landing Pages

Routes are auto-generated from AppConstants.AVAILABLE_LANDING_PAGES.
Currently available:

- /math/fractions
- /math/negative-numbers
- /maths/ratios
New subject landing pages can be added to the constants file and will automatically work without manual routing changes.

### 16. Error handling routes
     
| Route | Purpose |
|------|---------|
| `/error/iframed` | Iframe-safe error page |
| `/error/<status_code>` | Custom error page |
| `**` | Wildcard for broken URLs (404 page) |

**Critical:** The wildcard route (**) must always stay last in the routes array, or it will capture all routes and break navigation.

### 17. Why this routing file Is critical

- Every valid Oppia URL is registered here
- Every permission rule starts here
- Every editor, admin page, and learner view depends on this configuration
- If a route breaks or shows a false 404,check this file first
- All paths must be defined in constants.ts, otherwise pages will have false 404 status codes

### 18. Role-based access control

| Route | Access Level | Example Routes |
|------|-------------|---------------|
| Public (Not Logged In) | Public pages and learning content | `/about`, `/contact`, `/donate`, `/learn/<classroom>` |
| Learner | Learn and track progress | `/learner-dashboard`, practice sessions, `/profile` |
| Contributor | Content suggestions & translations | `/contributor-dashboard`, `/feedback-updates` |
| Creator | Create/edit explorations | `/creator-dashboard`, `/exploration_editor/<id>` |
| Curriculum Admin | Manage topics, skills, classrooms | `/topic_editor/<id>`, `/classroom-admin` |
| Moderator | Review content | `/moderator` |
| Blog editor | Manage blog posts | `/blog-dashboard` |
| Blog Admin | Admin blog settings | `/blog-admin` |
| Voiceover Admin | Manage voiceovers | `/voiceover-admin` |
| Release Coordinator | Cache & release tools | `/release-coordinator` |
| Super Admin | Full access | `/admin` and all routes |

### 19. Troubleshooting tips
Error: 'NoneType' object has no attribute 'version'

**Fix:**
1. Assign yourself the release-coordinator role
2. Go to /release-coordinator
3. Navigate to MISC section
4. Click Flush Cache

Route shows 404 but should exist
Check:
- Is the route registered in app.routing.module.ts?
- Is the route constant defined in assets/constants.ts?
- Are you using the correct URL format?
- Does the route require login?
Page loads but shows "Access Denied"
Check:
- Do you have the required role?
- Some pages require specific roles (see Section 18)
- Contact an admin if needed

### 20. Quick reference for contributors

**Login & Roles**
- Login: /login
- Admin panel: /admin
  
**Generate Test Data**
1. Go to /admin
2. Activities tab
3. Generate dummy data
   
**Classroom Access**
- All classrooms: /classrooms
- Specific classroom: /learn/<classroom_url>

**Editor Access**
- Exploration editor: /exploration_editor/create/<id>
- Collection editor: /collection_editor/create/<id>
- Topic editor: /topic_editor/<id>
- Skill editor: /skill_editor/<id>
- Story editor: /story_editor/<id>

### 21. Contributor Checklist
- Dev server starts successfully
- Dummy classroom created
- Topic created & published
- Topic added to classroom
- /learn/<classroom_url> loads correctly
- All routes tested
- Cache flushed (if needed)
- No console errors
- Routes tested for logged-in and logged-out users

### 22. Summary
This routing guide provides a complete reference for all routes in Oppia.
When contributing:
- Always check the correct URL format
- Verify guard requirements
- Use exact, case-sensitive paths
- Test logged-in and logged-out states
- Refer to troubleshooting if issues occur
- Contact Oppia maintainers or open a GitHub issue if needed
