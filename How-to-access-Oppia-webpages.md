## Table of Contents

- [Overview of Entities](#overview-of-entities)
- [Key Terms](#key-terms)
- [Other Terms](#other-terms)
- [User Account Pages](#user-account-pages)
  - [Log In or Create Account](#log-in-or-create-account)
  - [Log in as a Super-Administrator](#log-in-as-a-super-administrator)
- [Oppia Webpages](#oppia-webpages)
  - [About Page](#about-page)
  - [Admin Page](#admin-page)
      - [Important Admin Page Tabs](#important-admin-page-tabs)
  - [Android Page](#android-page)
  - [Blog Admin Page](#blog-admin-page)
  - [Blog Author Profile Page](#blog-author-profile-page)
  - [Blog Dashboard Page](#blog-dashboard-page)
  - [Blog Homepage Page](#blog-homepage-page)
  - [Blog Post Page](#blog-post-page)
  - [Classroom Admin Page](#classroom-admin-page)
  - [Classroom Page](#classroom-page)
  - [Classrooms Page](#classrooms-page)
  - [Collection Editor Page](#collection-editor-page)
  - [Collection Player Page](#collection-player-page)
  - [Community Library Page](#community-library-page)
  - [Contact Page](#contact-page)
  - [Contributor Admin Dashboard Page](#contributor-admin-dashboard-page)
  - [Contributor Dashboard Page](#contributor-dashboard-page)
      - [Important Contributor Dashboard Page Tabs](#important-contributor-dashboard-page-tabs)
  - [Create Learner Group Page](#create-learner-group-page)
  - [Creator Dashboard Page](#creator-dashboard-page)
  - [Creator Guidelines Page](#creator-guidelines-page)
  - [Custom Error Pages](#custom-error-pages)
  - [Delete Account Page](#delete-account-page)
  - [Diagnostic Test Player Page](#diagnostic-test-player-page)
  - [Donate Page](#donate-page)
  - [Edit Learner Group Page](#edit-learner-group-page)
      - [Important Edit Learner Group Page Tabs](#important-edit-learner-group-page-tabs)
  - [Email Dashboard Page](#email-dashboard-page)
  - [Embedded Exploration Player Page](#embedded-exploration-player-page)
  - [Exploration Editor Page](#exploration-editor-page)
  - [Exploration Player Page](#exploration-player-page)
  - [Facilitator Dashboard Page](#facilitator-dashboard-page)
  - [Feedback Updates Page](#feedback-updates-page)
  - [Get Started Page](#get-started-page)
  - [Iframe Error Page](#iframe-error-page)
  - [Learner Dashboard Page](#learner-dashboard-page)
  - [License Page](#license-page)
  - [Maintenance Page](#maintenance-page)
  - [Moderator Page](#moderator-page)
  - [New Lesson Player Page](#new-lesson-player-page)
  - [Partnerships Page](#partnerships-page)
  - [Pending Account Deletion Page](#pending-account-deletion-page)
  - [Practice Session Page](#practice-session-page)
  - [Preferences Page](#preferences-page)
  - [Privacy Policy Page](#privacy-policy-page)
  - [Profile Page](#profile-page)
  - [Release Coordinator Page](#release-coordinator-page)
      - [Important Release Coordinator Page Tabs](#important-release-coordinator-page-tabs)
  - [Review Test Page](#review-test-page)
  - [Signup Page](#signup-page)
  - [Skill Editor Page](#skill-editor-page)
  - [Story Editor Page](#story-editor-page)
  - [Story Player Page](#story-player-page)
  - [Study Guide Page](#study-guide-page)
  - [Teach Page](#teach-page)
  - [Terms of Use Page](#terms-of-use-page)
  - [Thank You Page](#thank-you-page)
  - [Topic Editor Page](#topic-editor-page)
  - [Topic Viewer Page](#topic-viewer-page)
  - [Topics & Skills Dashboard Page](#topics--skills-dashboard-page)
  - [View Learner Group Page](#view-learner-group-page)
  - [Voiceover Admin Page](#voiceover-admin-page)
  - [Volunteer Page](#volunteer-page)
- [Populating Data on Local Server](#populating-data-on-local-server)
  - [Populating the Explorations](#populating-the-explorations)
  - [Populating the Collections](#populating-the-collections)
  - [Populating the Blog Data](#populating-the-blog-data)
  - [Populating the Contributor Dashboard](#populating-the-contributor-dashboard)
  - [Populating the Story Player](#populating-the-story-player)
  - [Creating a Classroom](#creating-a-classroom)
  - [Creating a Topic](#creating-a-topic)
  - [Creating a Skill](#creating-a-skill)
  - [Generate Stories](#generate-stories)
  - [Generate Chapters](#generate-chapters)
  - [Populating the Community Library](#populating-the-community-library)
  - [Populating the New Lesson Player Page](#populating-the-new-lesson-player-page)
  - [Populating the Practice Session Page](#populating-the-practice-session-page)
  - [Populating the Study Guide Page](#populating-the-study-guide-page)
  - [Populating the Topic Viewer Page](#populating-the-topic-viewer-page)
  - [Populating the Classroom Page](#populating-the-classroom-page)
  - [Populating the Review Test Page](#populating-the-review-test-page)
 
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
C1 --> c2("Card-2")
S1 --> C2("Chapter-2")
C2 --> c3("Card-3")
c3 --> co("Content")
c3 --> in("Interaction")
in --> mc("Multiple-Choice")
in --> is("Image Selection")
in --> fi("Fraction-Input")
in --> oqt("Other Question Types")
S2 --> C3("Chapter-3")
S2 --> C4("Chapter-4")
C3 --> c4("Card-4")
C4 --> c5("Card-5")
C4 --> c6("Card-6")
```
As you go through https://www.oppia.org/, you will find these entities.

### Key Terms

1. **Classroom**: A Classroom in Oppia is a collection of topics grouped under a single subject. For example: https://www.oppia.org/learn/math this displays a Maths classroom.
2. **Topic**: A topic is a broad term that refers to the subject content being taught. For example: https://www.oppia.org/learn/math displays a list of math topics. A single topic can be described through multiple stories.
3. **Story**: Stories are situations/scenarios that are meant to help users understand the topic. For example, if the topic is addition, then one of the stories could be about where a kid goes to a shop and buys 3 pens and 4 pencils. The lesson could then explain the concept of addition while discussing the total number of items bought. As another example, https://www.oppia.org/learn/math/place-values/story talks about Jaime’s adventures for learning about place values. A single story can be referenced in multiple chapters and is essentially a collection of chapters.
4. **Chapter**: A chapter corresponds to different lessons through which we aim to teach the topic to the users. Each chapter has an associated exploration, and this exploration may have several cards. For example, https://www.oppia.org/learn/math/place-values/story shows a bunch of chapters to learn the place values topic.
5. **Card**:
A card is the primary component of lesson where each card consists of:

   - **Content**: This refers to the tutor’s question to the learner.
   - **Interaction**: Interactions refer to the type of question the users are shown (e.g. multiple-choice, image selection, fraction input, etc.)
   - **Response**: Feedback from Oppia to the learner based on the learner's answer to the interaction.

   For example, [this card](https://www.oppia.org/explore/K645IfRNzpKy?story_url_fragment=jaimes-adventures-in-arcade&topic_url_fragment=place-values&classroom_url_fragment=math&node_id=node_1) shows a card in one of the place values chapters.

### Other Terms

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
   
## User Account Pages

### Log In or Create Account

Many Oppia Pages require authentication to access. In order to sign in:

1. Click the sign-in button on the top left navigation bar.

   ![Sign-In Button](images/Webpage-Guide/signInButton.png)

2. Once redirected to the login page, choose an email address and sign in. If you have used this email address before, you will be signed in to the existing account. Otherwise, a new account will be created for you.
   
   ![Sign-in page](images/Webpage-Guide/nonAdminSignUp.png)

### Log in as a Super-Administrator

Super Admin can:
- Access the Admin page
- Assign roles to users
- Run dummy data generation jobs
  
Some of these roles (e.g. "Topic admin") give the user access to privileged pages (e.g. the topics and skills dashboard).

There are two ways to become a super admin on the local server.

#### Method A — Implicit Super Admin Email (Fast):
1. On the sign-in page, enter testadmin@example.com.
2. A message will appear: "This email address has implicit Super Admin privileges!" — you now have Super Admin access.

   ![Sign-in page with implicit super-admin email address](images/Webpage-Guide/implicitSuperAdmin.png)

#### Method B — Grant Super Admin via Firebase emulator (Explicit):

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

### About Page

- **Description:** 
Provides information about the Oppia Foundation, its mission, team, and Impact.  

- **Url:** 
/about

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click About in the Navbar.

![About page](images/Webpage-Guide/about.png)


### Admin Page

- **Description:**
The Admin page is where Super Admins manage roles, run dummy data generation jobs, and reload prebuilt content.

- **Url:** 
http://localhost:8181/admin

- **Permissions Required:**
[Super Admin](#log-in-as-a-super-administrator)

**Steps to Access:**
  1. Log in as a super-admin. 
  2. Go to the profile menu and click on the "Admin Page" link.
      
![Admin Panel Link](https://user-images.githubusercontent.com/16653571/41501009-e04e9a76-71b9-11e8-958e-985f5bc7122a.png)

#### Important Admin Page Tabs

We have the following tabs on the Admin Page:

- [Activities Tab](#activities-tab)
- [Misc Tab](#misc-tab)
- [Platform Parameters Tab](#platform-parameters-tab)
- [Roles Tab](#roles-tab)

#### **Activities Tab**

- **Description:**
This page allows Super Admin to generate, reload, or seed data on the local development server, such as explorations, collections, skills, topics, and  classrooms.

- **Url:**
http://localhost:8181/admin (Activities tab)

- **Permissions Required:**
[Super Admin](#log-in-as-a-super-administrator)

**Steps to Access:** 
  1. Log in as a super-admin.
  2. Navigate to /admin.
  3. Click on the Activities tab.
  4. Choose the required data generation or reload action.

![Activities](images/Webpage-Guide/adminactivities.png)

#### **Misc Tab**

- **Description:**
This page contains advanced admin tools used to maintain, debug, and manage Oppia’s internal data.
These tools are mainly for super-admins and developers, and are usually used during development, testing, data fixes, or emergency maintenance.
Most learners and creators will never need to use this page.

- **Url:**
http://localhost:8181/admin (Misc tab)

- **Permissions Required:**
[Super Admin](#log-in-as-a-super-administrator)

**Steps to Access:**
  1. Log in as a super-admin
  2. Navigate to /admin
  3. Open the Misc tab

![Misc tab](images/Webpage-Guide/adminmisc.png)

#### **Platform Parameters Tab** 

- **Description:**
This page displays platform-level configuration parameters that control feature flags and site behavior across Oppia. Admins can view platform configuration parameters. Some values may be editable depending on the environment.

- **Url:**
http://localhost:8181/admin (Platform Parameters tab)

- **Permissions Required:**
[Super Admin](#log-in-as-a-super-administrator)

**Steps to Access:**
  1. Log in as a super-admin.
  2. Open /admin.
  3. Navigate to the Platform Parameters tab.
  4. Review or update configuration values as required.

![Platform Parameters](images/Webpage-Guide/adminplatform.png)

#### **Roles Tab** 

- **Description:** 
Allows Super Admin to assign roles such as Curriculum Admin, Question Admin, or Release Coordinator, etc.

- **Url:**
http://localhost:8181/admin (Roles tab)

- **Permissions Required:**
[Super Admin](#log-in-as-a-super-administrator)

**Steps to Access:**

  1. Navigate to the Admin page.
  2. Click the "Roles" tab and enter the username of the user whose roles you want to edit.

   ![Admin Role Tab](images/Webpage-Guide/adminroles.png)

  3. Assign the desired role, "Question Admin" in this screenshot:

   ![Assigning role](images/Webpage-Guide/assignroles.png)

### Android Page

- **Description:** 
 Android Page allows to learn on the go with the Oppia Android app to access free, high-quality lessons in math, science, and more, even offline.

- **Url:** 
/android

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click LEARN in the navbar.
  2. Click try it today.
   
![Android page](images/Webpage-Guide/android.png)

### Blog Admin Page

- **Description:**
Administrative dashboard for managing blog settings, categories, featured posts, and blog-wide configurations.

- **Url:**
/blog-admin

- **Permissions Required:**
Blog Admin role

**Steps to Access:**
  1. Log in as a Super Admin
  2. Assign yourself the Blog Admin role via /admin → Roles
  3. Navigate to http://localhost:8181/blog-admin

![Blog Admin](images/Webpage-Guide/blogadmin.png)

### Blog Author Profile Page

- **Description:**
Displays a blog author's profile, including their bio, published posts, and author information.

- **Url:**
/blog/author/<author_username>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to any blog post
  2. Click on the author's name
  3. OR directly visit http://localhost:8181/blog/author/<author_username>

![Blog Author Profile](images/Webpage-Guide/blogauthor.png)

### Blog Dashboard Page

- **Description:**
Management interface for blog authors to create, edit, and publish blog posts.

- **Url:**
/blog-dashboard

- **Permissions Required:**
Blog Editor role

**Steps to Access:**
  1. Log in as a Super Admin
  2. Assign yourself the Blog Editor role via /admin (Roles)
  3. Navigate to http://localhost:8181/blog-dashboard

![Blog Dashboard](images/Webpage-Guide/blogdashboard.png)

### Blog Homepage Page

- **Description:**
The main blog page displaying recent blog posts, featured articles, and blog categories.

- **Url:**
/blog

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Click "Blog" in the navigation bar
  2. OR directly visit http://localhost:8181/blog
   
![Blog Homepage](images/Webpage-Guide/bloghomepage.png)

- To populate the Blog Homepage: See [Populating the Blog Data](#populating-the-blog-data)

### Blog Post Page

- **Description:**
Displays a single blog post with its full content, images, and comments.

- **Url:**
 /blog/<blog_post_slug>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to /blog
  2. Click on a blog post title
  3. OR directly visit http://localhost:8181/blog/<blog_post_slug>

![Individual Blog Post](images/Webpage-Guide/blogpostslug.png)

### Classroom Admin Page

- **Description:**
This page allows Curriculum Admins to create and manage classrooms, assign  topics, and configure classroom content displayed to learners.

- **Url:**
http://localhost:8181/classroom-admin

- **Permissions Required:**
Curriculum Admin role

**Steps to Access:**
  1. Log in as a super-admin.
  2. Assign yourself the Curriculum Admin role.
  3. Navigate to /classroom-admin.
  4. Create or edit classrooms and assign topics.

![Classroom admin](images/Webpage-Guide/classroomadmin.png)

### Classroom Page

- **Description:**
Individual classroom landing page displaying all topics within that classroom, along with the classroom description and learning path.

- **Url:**
/learn/<classroom_url>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to /learn
  2. Click on a classroom card (e.g., "Math")

Example:
 http://localhost:8181/learn/math

![Classroom Page](images/Webpage-Guide/learn:math.png)

- To populate the Classroom Page: See [Populating the Classroom Page](#populating-the-classroom-page)

### Classrooms Page

- **Description:**
Landing page showing all available classrooms (Math, Science, etc.) that learners can explore.

- **Url:**
/learn

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Click "Learn" in the navigation bar
  2. OR directly visit http://localhost:8181/learn

![Classrooms](images/Webpage-Guide/allclassrooms.png)

### Collection Editor Page

- **Description:**
This page allows creators to create and edit collections, which are ordered groups of explorations designed to guide learners through a learning path.

- **Url**: 
http://localhost:8181/collection_editor/create/<collection_id>

- **Permissions Required:**
Collection Editor 

**Steps to Access:**
  1. Log in to Oppia.
  2. Navigate to /creator-dashboard.
  3. Click Create New Collection.
  4. You will be redirected to the Collection Editor page.

![Collection editor](images/Webpage-Guide/collectioneditor.png)

### Collection Player Page
- **Description:**
This page displays a learner-facing view of a collection, allowing learners to play explorations in sequence.

- **Url:**
http://localhost:8181/collection/<collection_id>

- **Permissions Required:**
Public (no login required)

**Steps to Access:**
  1. Ensure a collection is published.
  2. Navigate to /community-library.
  3. Search for the collection.
  4. Open the collection to start learning.

![Collection player](images/Webpage-Guide/collections.png)

- Ways to Generate Collections: See [Populating the Collections](#populating-the-collections).

### Community Library Page

- **Description:**
The Community Library allows users to browse, search, and filter explorations and collections available on Oppia.

- **Url:**
http://localhost:8181/community-library

- **Permissions Required:**
Public (no login required)

**Steps to Access:**
  1. Open Oppia in a browser.
  2. Navigate to /community-library.
  3. Use filters or search to find learning content.
   
![Community library](images/Webpage-Guide/communitylibrary.png)

- To populate the Community Library Page: [Populating the Community Library](#populating-the-community-library)

### Contact Page

- **Description:** 
Contact Page allows to connect with the Oppia team,share your feedback, ask questions, and discover how to join our global community of contributors.

- **Url:** 
/contact

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Get Involved in the navbar.
  2. Then click on Contact Us.

![Contact page](images/Webpage-Guide/contact.png)

### Contributor Admin Dashboard Page

- **Description:**
This is used to manage community reviewer permissions. It allows administrators to grant or revoke question review and translation review rights to trusted contributors.

- **Url:**
http://localhost:8181/contributor-admin-dashboard

- **Permissions Required:**
Question Admin or Translation Admin.

**Steps to Access:**
  1. Assign yourself the Question Admin role/Translation Admin.
  2. Navigate to /contributor-admin-dashboard

![Contributor admin dashboard](images/Webpage-Guide/contributordashboardadmin.png)

### Contributor Dashboard Page

- **Description:**
Allows contributors to submit translation suggestions and questions.

- **Url:**
http://localhost:8181/contributor-dashboard

- **Permissions Required:**
Logged-in users.

**Steps to Access:**
  1. Log in to Oppia.
  2. Navigate to /contributor-dashboard.

![Contributor dashboard](images/Webpage-Guide/mycontributions.png)

#### Important Contributor Dashboard Page Tabs

We have the following tabs on the Contributor Dashboard Page:

- [My Contributions Tab](#my-contributions-tab)
- [Translate Text Tab](#translate-text-tab)

#### **My Contributions Tab** 
This is your personal dashboard where you can track your history and impact. It is divided into three sections (visible in the side-nav):

1. **Accomplishments:** 
Displays your overall contribution Stats and any Badges you have earned for your work.
![Badges](images/Webpage-Guide/Badges.png)

2. **Available Tasks:** 
If you have been granted "Reviewer" rights by an admin, this section shows you a list of other people's contributions that need your approval.                                   
- Question Review Rights
This permission allows users to review question suggestions submitted by other contributors.
- Translation Review Rights
This permission allows users to review translation suggestions in specific languages.    
![translations](images/Webpage-Guide/reviewtranslations.png)

3. **Contributions:**
Shows the status of everything you have submitted (e.g., translations or 
questions). You can see if they are "Accepted," "Rejected," or "In Review."
![translations](images/Webpage-Guide/translations.png)

#### **⁠⁠Translate Text Tab**
This is where the actual work happens for translators.
It shows a list of Opportunities (lessons that need to be translated into your chosen language).
You can use the Language and Topic filters at the top to find specific lessons you want to work on.
Clicking Translate on any item will open the translation editor for that lesson.

Note: The "Available Tasks" section in the Contributor Dashboard becomes visible when a user has reviewer permissions. 
![Translate Text](images/Webpage-Guide/translatetext2.png)

- Ways to Generate Contributions:
  See [Populating the Contributor Dashboard](#populating-the-contributor-dashboard).

### Create Learner Group Page

- **Description:**
Interface for facilitators to create a new learner group, add members, and assign lessons.

- **Url:**
/create-learner-group

- **Permissions Required:**
Logged-in users

**Steps to Access:**
  1. Log in to Oppia
  2. Navigate to /facilitator-dashboard
  3. Click "Create Learner Group"
  4. OR directly visit http://localhost:8181/create-learner-group

![Create Learner Group](images/Webpage-Guide/createlearnergroup.png)

### Creator Dashboard Page

- **Description:**
This dashboard allows creators to manage explorations and collections they have created, including drafts and published content.

- **Url:**
http://localhost:8181/creator-dashboard

- **Permissions Required:**
Logged-in users

**Steps to Access:**
  1. Log in to Oppia.
  2. Navigate to /creator-dashboard.
      - Create, edit, or manage your explorations and collections.

 ![Creator dashboard](images/Webpage-Guide/creatordashboard.png)

### Creator Guidelines Page

- **Description:** 
Provides instructions and best practices for participating in the community and creating explorations.

- **Url:** 
 /creator-guidelines

- **Permissions Required:** 
 None

**Steps to Access:** 
  1. Click Creator-guidelines in the footer.

![Creator Guidelines](images/Webpage-Guide/creatorguidelines.png)

### Custom Error Pages

- **Description:**
Custom error pages for specific HTTP error codes (400, 401, 500, etc.) with helpful messages and recovery options.

- **Url:**
/error/<status_code>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. These pages are automatically displayed when the corresponding error occurs
  2. For testing, visit http://localhost:8181/error/404 or /error/500

![Custom Error Pages](images/Webpage-Guide/404error.png)

### Delete Account Page

- **Description:** 
This page allows signed-in learners to request deletion of their account.
In local development, the account may be deleted immediately. On production, the deletion request can be marked as pending and processed later.

- **Url:** 
http://localhost:8181/delete-account

- **Permissions Required:**
Learners must be signed in.

**Steps to Access:** 
  1. Log in to Oppia.
  2. Navigate to /preferences (Preferences page).
  3. On that page there is Delete button.
   
When the user clicks this button, they are taken to the Delete Account page, where they can confirm the deletion.
Follow the on-screen confirmation steps.

**Note**:
On local servers, deletion may happen immediately.
On production, deletion requests may remain pending.

![Delete account page](images/Webpage-Guide/deleteaccount.png)

### Diagnostic Test Player Page

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

**Steps to Access:**
  1. Navigate to the classroom page.
  2. On the classroom page, click Take quiz.
   ![classroom page](images/Webpage-Guide/takequiz.png)
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

### Donate Page

- **Description:** 
Explains how community can support or align with Oppia Foundation's mission. 

- **Url:**   
/donate

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Donate in the Navbar.

![ Donate page](images/Webpage-Guide/donate.png)

### Edit Learner Group Page

- **Description:**
Allows facilitators to edit learner group details, manage members, and update assigned lessons.

- **Url:**
/edit-learner-group/<group_id>

- **Permissions Required:**
The user must be the Facilitator of that specific group.

**Steps to Access:**
  1. Navigate to /facilitator-dashboard
  2. Click on a learner group
  3. Click "Edit Group"
   
![Edit Learner Group](images/Webpage-Guide/editleanergroup.png) 

#### Important Edit Learner Group Page Tabs

We have the following tabs on the Edit Learner Group Page:
- [Learners Progress Tab](#learners-progress-tab)
- [Overview Tab](#overview-tab)
- [Preferences Tab](#preferences-tab)
- [Syllabus Tab](#syllabus-tab)

#### Learners Progress Tab
Tracks individual learner progress. You can see:
 - Which stories each learner has completed
 - Which skills they've mastered or are struggling with
 - Overall completion percentages

   ![Learners' Progress](images/Webpage-Guide/leanergroupprogress.png)

#### Overview Tab
Shows a high-level summary of the group with two sub-tabs:
      - Skills Analysis — Shows common skills that learners in this group are struggling with. Helps facilitators identify weak areas.
      - Progress in Stories — Shows how learners are progressing through the assigned stories/chapters.
        
#### Preferences Tab
Group settings including:
 - Edit the group title and description
 - Invite learners by username
 - Remove learners from the group
 - Delete the group entirely

![Preferences](images/Webpage-Guide/learnergrouppreferences.png)

#### Syllabus Tab
Manage the group's learning content:
 - Add/remove stories — Assign stories from topics for learners to work through
 - Add/remove skills — Assign specific skills for practice

![Syllabus](images/Webpage-Guide/leaenergroupsyllabus.png)

### Email Dashboard Page

- **Description:**
Interface for managing and sending bulk emails to specific user groups or the entire Oppia community.

- **Url:**
/emaildashboard

- **Permissions Required:**
Admin privileges

**Steps to Access:**
  1. Log in as a Super Admin
  2. Navigate to http://localhost:8181/emaildashboard

![Email Dashboard](images/Webpage-Guide/emaildashboard.png)

### Embedded Exploration Player Page

- **Description:**
A stripped-down version of the exploration player designed to be embedded in external websites via iframe.

- **Url:**
/embed/exploration/<exploration_id>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Directly visit http://localhost:8181/embed/exploration/<exploration_id>
  2. OR embed in an iframe:

![Embedded Exploration Player](images/Webpage-Guide/embedexploration.png)

### Exploration Editor Page

- **Description:**
The exploration editor is where creators build interactive lessons. It includes a card-based interface for adding content, interactions, and feedback paths.

- **Url:**
/create/<exploration_id>

- **Permissions Required:**
Logged-in users (exploration owner or collaborators)

**Steps to Access:**
  1. Log in to Oppia
  2. Navigate to Creator Dashboard (/creator-dashboard)
  3. Click "Create Exploration"
  4. OR open an existing exploration from your dashboard

![Exploration Editor](images/Webpage-Guide/explorationeditor.png)

### Exploration Player Page

- **Description:**
The legacy exploration player interface for playing individual explorations (lessons).

- **Url:**
/explore/<exploration_id>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Find an exploration in the Community Library
  2. Click "Play" on the exploration
  3. OR directly visit http://localhost:8181/explore/<exploration_id>

![Old Exploration Player](images/Webpage-Guide/oldexploration.png)

- To populate the Exploration Player Page: See [Populating the Explorations](#populating-the-explorations)
  
### Facilitator Dashboard Page

- **Description:**
A dashboard for classroom facilitators to manage learner groups, track student progress, and assign lessons.

- **Url:**
/facilitator-dashboard

- **Permissions Required:**
Logged-in users with Full User Role.

**Steps to Access:**
  1. Log in as a Super Admin, navigate to [Release Coordinator](#release-coordinator-page) -> Features tab, and enable the Learner Groups flag (internally learner_groups_are_enabled).
  2. Ensure your user account has the Full User role (assigned via the Admin -> Roles tab).
  3. Navigate to http://localhost:8181/facilitator-dashboard

![Facilitator Dashboard](images/Webpage-Guide/Facilatordashboard.png)

### Feedback Updates Page

- **Description:**
Displays all feedback threads from explorations that the user has participated in 
or subscribed to. Users can view conversation threads, read messages, and reply 
to feedback on explorations.

- **Url:**
/feedback-updates

- **Permissions Required:**
Logged-in users

**Steps to Access:**
  1. Log in to Oppia
  2. directly visit http://localhost:8181/feedback-updates

![Feedback Updates](images/Webpage-Guide/feedback.png)

### Get Started Page

- **Description:** 
Provides guidance on how to begin using Oppia as a contributor.

- **Url:** 
/get-started

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Get Started in the footer

![Get Started page](images/Webpage-Guide/getstarted.png)


### Iframe Error Page

- **Description:**
A special error page designed to display within iframes without breaking the parent page.

- **Url:**
/error/iframed

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. This page is automatically shown when an error occurs within an embedded Oppia iframe
  2. OR directly visit http://localhost:8181/error/iframed

![Iframe Error Page](images/Webpage-Guide/iframeerror.png)

### Learner Dashboard Page

- **Description:**
The learner's personal homepage showing their learning progress, goals, ongoing lessons, recommended topics, and achievements.

- **Url:**
/learner-dashboard

- **Permissions Required:**
Logged-in users

**Steps to Access:**
  1. Log in to Oppia
  2. Click the Oppia logo or "Home" link
OR directly visit http://localhost:8181/learner-dashboard

![Learner Dashboard](images/Webpage-Guide/leanerdashboard.png)

### License Page

- **Description:** 
Details the licenses under which Oppia’s content and software are released.

- **Url:** 
/license

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Linked from the image receiver or audio uploader components during the creation process.

![License page](images/Webpage-Guide/license.png)

### Maintenance Page

- **Description:**
Displayed when Oppia is in maintenance mode. Shows a message that the site is temporarily unavailable.

- **Url:**
/maintenance

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. This page is automatically displayed when the server is in maintenance mode
  2. For testing, admins can start the server with python -m scripts.start --prod_env --maintenance_mode.
  3. OR directly visit http://localhost:8181/maintenance

**NOTE:** Maintenance mode only works with --prod_env flag. That's why the server is started with python -m scripts.start --prod_env --maintenance_mode.
![Maintenance Page](images/Webpage-Guide/maintenance.png)

### Moderator Page

- **Description:**
Page for moderators to manage explorations and user feedback.

- **Url:** 
/moderator

- **Permissions Required:**
Moderator

**Steps to Access:** 
  1. Click Moderator Page in the side navigation bar.

![Moderator](images/Webpage-Guide/moderator.png)

### New Lesson Player Page

- **Description:**
The modern lesson player interface with improved UX for playing explorations.

- **Url:**
/lesson/<exploration_id>

- **Permissions Required:**
Public (with authorization check)

**Steps to Access:**
  1. Go to [Release Coordinator](#release-coordinator-page) → Features tab
  2. Find new_lesson_player and set "Force-enable for all users" to Yes → Click **Save**
     ![Force-enable](images/Webpage-Guide/newlessonplayerenable.png)
  3. Navigate through a classroom → topic → story → chapter
  4. Click on a chapter — it will now open in the New Lesson Player

![New Lesson Player](images/Webpage-Guide/newlessonplayer.png)

- To populate the New Lesson Player Page: [Populating the New Lesson Player Page](#populating-the-new-lesson-player-page)
  
**NOTE:** This feature is currently in the development stage and has not been 
released to production yet. It is only available on local development servers.

### Partnerships Page

- **Description:** 
Provides information for organizations interested in partnering with Oppia to help students access education.

- **Url:** 
/partnerships

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Get Involved in the navbar.
  2. Then click on the Schools and Organizations.
![Partnerships page](images/Webpage-Guide/partnerships.png)

### Pending Account Deletion Page

- **Description:**
Displayed after a user requests account deletion. Shows the deletion status and estimated completion time.

- **Url:**
/pending-account-deletion

- **Permissions Required:**
None (Public - shown after deletion request)

**Steps to Access:**
  1. User is automatically redirected here after requesting account deletion
  2. OR directly visit http://localhost:8181/pending-account-deletion

![Pending Account Deletion](images/Webpage-Guide/pendingaccountdeletion.png)

### Practice Session Page

- **Description:**
An interactive practice session where learners answer practice questions to reinforce their understanding of a topic's skills.

- **Url:**
/learn/<classroom_url>/<topic_url>/practice/session?selected_subtopic_ids=[<id>]

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to /learn/<classroom_url>/<topic_url>/story (Topic Viewer page)
  2. Go to Practice Tab
  3. Select skills you want to practice.
  4. Click "Start"
  5. Answer questions related to the topic

Example:
http://localhost:8181/learn/math/add/practice/session?selected_subtopic_ids=%5B1%5D

![Practice Session](images/Webpage-Guide/practicesession.png)

- To populate the Practice Session Page:  See [Populating the Practice Session Page:](#populating-the-practice-session-page)
  
### Preferences Page

- **Description:** This page allows learners to change their settings on Oppia, such as language preference and email preferences.

- **Url:** http://localhost:8181/preferences

- **Permissions Required:** No special permissions. Any signed-in learner can access it.

**Steps to Access:**
  1. Log in to Oppia.
  2. Open the top-right profile menu
  3. Click Preferences.

![Preferences page](images/Webpage-Guide/preferences.png)

### Privacy Policy Page

- **Description:** 
Explains how Oppia collects, uses, and protects user data.

- **Url:** 
/privacy-policy

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Privacy Policy in the footer.

![Privacy Policy page](images/Webpage-Guide/privacypolicy.png)

### Profile Page

- **Description:** 
This page displays a learner’s profile. It shows their username, bio, badges, and created lessons.

- **Url:** 
http://localhost:8181/profile/<username>

- **Permissions Required:** 
No special permissions. Public profiles are viewable by anyone.

**Steps to Access:** 
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

**Steps to Access:**
  1. Log in as a Super Admin.
  2. Assign yourself the Release Coordinator role via Admin → Roles.
  3. Navigate to /release-coordinator.
  4. Use tools such as Flush Cache under the Misc tab.

#### Important Release Coordinator Page Tabs

We have the following tabs on the Release Coordinator Page:

- [Beam Jobs Tab](#beam-jobs-tab)
- [Features Tab](#features-tab)
- [Misc Tab](#misc-tab)

#### **Beam Jobs Tab**
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

#### **Features Tab**
It is used to enable, disable, and control feature flags.
It helps roll out new features gradually using:
- rollout percentage
- user groups
- force-enable options
It prevents breaking the site by testing features on limited users first

Example:
 Enable a new UI feature only for 10% of users before full release.

![Features](images/Webpage-Guide/releasefeatures.png)

#### **Misc Tab**
   
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

### Review Test Page

- **Description:**
A test that learners can take after completing a story to review what they've learned.

- **Url:**
/learn/<classroom_url>/<topic_url>/review-test/<story_url>

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Complete a story
  2. Click "Take Review Test" at the end of the story
  3. The review test player will load

Example:
http://localhost:8181/learn/math/fractions/review-test/introduction-to-fractions

![Review Test Page](images/Webpage-Guide/reviewtestpage.png)

How to Enable Review Test Page
1. Navigate to http://localhost:8181/release-coordinator -> Features Tab
 ![Enable Review Test Page](images/Webpage-Guide/reviewenable.png)
2. Find EnableReadyForReviewTest and enable it.
3. Click Save

- To populate Review Test Page: See  [Populating the Review Test Page.](#populating-the-review-test-page)

### Signup Page

- **Description:**
Account creation page where new users can register for an Oppia account.

- **Url:**
/signup

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Click "Sign In" button
  2. On the login page, enter a new email address
  3. Complete the signup flow (username selection, terms acceptance)

![Signup Page](images/Webpage-Guide/signup.png)

### Skill Editor Page
- **Description:** 
The skill editor allows the creation of skills in Oppia. You can access the Skills editor under the skills tab of [topics-and-skills-dashboard page](#topics--skills-dashboard-page).

- **Url:**
http://localhost:8181/skill_editor/<skill_id>

- **Permissions Required:**
Curriculum Admin role.

**Steps to Access:**
  1. Open the Topics & Skills Dashboard.
  2. Click the Topic in which you want to add skills.
  3. Go to the ADD SKILL .
   ![ADD SKILL](images/Webpage-Guide/newskilllink.png)
  4. New Skill modal will pop up.
  5. Once you click on Save button of the modal,a new tab will be opened.
  6. That will be Skill Editor page.
   
![Skill editor](images/Webpage-Guide/skilleditor2.png)

### Story Editor Page

- **Description:**
This allows the user to create stories in Oppia.

- **Url:**
http://localhost:8181/story_editor/<story_id>

- **Permissions Required:**
Curriculum Admin role

**Steps to Access:** 
  1. Navigate to /topics-and-skills-dashboard.
  2. [Create a topic](#creating-a-topic).
  3. Go to the [topic editor](#topic-editor-page) and click on the add story button.
   ![canonicalstories](images/Webpage-Guide/topiceditor.png)
  4. Complete the “New story” modal and wait for the story editor page to load.

![New story](images/Webpage-Guide/storyeditor.png)

### Story Player Page

- **Description:** 
Displays the learner-facing view of a story and its chapters.

- **Url:**
/learn/<classroom_url_fragment>/<topic_url_fragment>/story/<story_url_fragment>

- **Permissions Required:**
Public (no login required)

**Steps to Access:**
  1. Navigate to /learn (Classrooms Page).
  2. Click on a Classroom (for example, "Math").
  3. Click on a Topic (for example, "Multiplication").
  4. Click "Continue" on a Story.
  5. The Story Player page opens.
![Story player page](images/Webpage-Guide/storyplayer.png)

- To populate the Story Player Page it needs a published topic in a classroom, with a story that has chapters linked to published explorations: See [Populating the Story Player](#populating-the-story-player)
 

### Study Guide Page

- **Description:**
Displays detailed study materials, explanations, and worked examples for a specific subtopic.

- **Url:**
/learn/:classroom_url_fragment/:topic_url_fragment/studyguide/:subtopic_url_fragment

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to /learn/<classroom_url>/<topic_url>/story (Topic Viewer page)
  2. Click on a subtopic from the list
  3. The study guide for that subtopic will load

Example:
 http://localhost:8181/learn/math/fractions/studyguide

 ![Study Guide](images/Webpage-Guide/studyguide.png)

- To populate the Study Guide Page: [Populating the Study Guide Page:](#populating-the-study-guide-page)
  
### Teach Page

- **Description:** 
Provides resources and guidance for teachers who want to use Oppia in their classrooms or create educational content.

- **Url:** 
/teach

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click For Parents/Teachers in the footer.
![Teach](images/Webpage-Guide/teach.png)

### Terms of Use Page

- **Description:** 
Defines the legal terms and conditions for using the Oppia platform.

- **Url:**
/terms

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Terms of Service in the footer.

![Terms of Use](images/Webpage-Guide/terms.png)

### Thank You Page

- **Description:** 
Confirmation page displayed after a successful donation.

- **Url:**
/thanks

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Users are redirected automatically after completing a donation.

![Thank You page](images/Webpage-Guide/thankyou.png)

### Topic Editor Page

- **Description:**
Interface for creating and managing topics, including subtopics, stories, skills, and diagnostic test configuration.

- **Url:**
/topic_editor/<topic_id>

- **Permissions Required:**
Curriculum Admin role

**Steps to Access:**
  1. Log in as a Super Admin
  2. Assign yourself the Curriculum Admin role
  3. Navigate to Topics and Skills Dashboard
  4. Click on an existing topic OR create a new one
  5. The Topic Editor page will open

![Topic Editor](images/Webpage-Guide/topiceditor1.png)

### Topic Viewer Page

- **Description:**
Displays a topic's details, stories, practice sessions, and study materials for learners.

- **Url:**
/learn/<classroom_url>/<topic_url>/story

- **Permissions Required:**
None (Public)

**Steps to Access:**
  1. Navigate to /learn (Classrooms page)
  2. Click on a classroom (e.g., "Math")
  3. Click on a topic (e.g., "Fractions")

Example:
http://localhost:8181/learn/math/fractions/story

![Topic Viewer](images/Webpage-Guide/topicviewer.png)

- To populate the Topic Viewer Page: [Populating the Topic Viewer Page](#populating-the-topic-viewer-page)
  
### Topics & Skills Dashboard Page

- **Description:** 
The central hub for Curriculum Admins to create and manage Topics (and their stories) and Skills.

- **Url:**
http://localhost:8181/topics-and-skills-dashboard

- **Permissions Required:**
Curriculum Admin role.

**Steps to Access:**
  1. Log in as a Super Admin.
  2. Assign yourself the Curriculum Admin role.
  3. Navigate to /topics-and-skills-dashboard.


![Topics & Skills dashboard](images/Webpage-Guide/topicsandskillsdashboard.png)

### View Learner Group Page

- **Description:**
Displays learner group information, member progress, and group activities.

- **Url:**
/learner-group/<group_id>

- **Permissions Required:**
Group members or facilitators

**Steps to Access:**
  1. Navigate to /facilitator-dashboard (for facilitators)
  2. OR access via shared group link (for members)
  3. Click on the group to view details

![View Learner Group](images/Webpage-Guide/viewgroup.png)

### Voiceover Admin Page

- **Description:**
Administrative tool for managing voiceover recordings, reviewing submitted voiceovers, and assigning voiceover tasks.

- **Url:**
/voiceover-admin

- **Permissions Required:**
Voiceover Admin role

**Steps to Access:**
  1. Log in as a Super Admin
  2. Assign yourself the Voiceover Admin role via /admin (Roles)
  3. Navigate to http://localhost:8181/voiceover-admin

![Voiceover Admin](images/Webpage-Guide/voiceoveradmin.png)


### Volunteer Page

- **Description:** 
Provides information on how to join the Oppia community as a volunteer and contribute in various roles.

- **Url:** 
/volunteer

- **Permissions Required:** 
None

**Steps to Access:** 
  1. Click Get Involved in the navbar.
  2. Then click on the Volunteer.

![Volunteer page](images/Webpage-Guide/volunteer.png)

## Populating Data on Local Server

This section explains all the ways data can be created, loaded, or generated on the Oppia local development server.

### Populating the Explorations

- To populate the Explorations:
  - **Quick method:** Use Generate Dummy Explorations OR Reload a Single Exploration in [Activities tab](#activities-tab).

  - **Manual method:**

    - Open Creator Dashboard or Go to: http://localhost:8181/creator-dashboard 
    - Click: “Create Exploration”
    - Choose Interaction Type (You will be asked to select from Multiple Choice, Text Input, etc.)
    - Click Create
    - Add Content to the Card  
        - Content → The question shown to the learner  
        - Interaction → How the learner answers  
        - Response → Feedback after submission  
    - Click Save Draft
    - Add More Cards (Optional)
    -  Preview the Exploration
    -   Publish the Exploration
    -   Use Exploration in a Story  
       - Go to Topic Editor  
       - Open a Story  
       - Add a Chapter  
       - Select your published Exploration  
       - Save draft → Publish topic again if needed


### Populating the Collections

- To populate the Collections:
  - **Quick method:** Use Reload a Single Collection in [Activities tab](#activities-tab).

  - **Manual method:** Using the Collection Editor

    - Log in to Oppia
    -  Navigate to /creator-dashboard
    -  Click the "+ CREATE EXPLORATION" button
    -  A modal appears: "Create an Activity"
    -  Select "New Collection"
    -  Click "CREATE COLLECTION"
    -  You will be redirected to the Collection Editor page  

**Note:** Despite the button saying "Create Exploration", it opens a modal where you can choose to create either an Exploration OR a Collection.

**Limitations of Quick method:**
- Cannot edit structure  
- Cannot choose explorations  
- Cannot create new collections  


### Populating the Blog Data

- To populate the Blog Data:

  - **Quick method:**

     - Go to [Activities tab](#activities-tab)
     - Scroll to "Generate dummy blog post"
     - Click "Generate" next to titles
     - Each click generates and publishes a blog post  


### Populating the Contributor Dashboard

- To populate the Contributor Dashboard:
  
   - **Quick method:**
     
     - **Method 1: Generate Dummy Translation Opportunities**
      
       - **Populates:** Translate Text tab (with translation opportunities) and My Contributions → Translations (after submitting translations)
       - **Steps:**
         - Log in as a [Super Admin](#log-in-as-a-super-administrator)
         - Assign yourself the Curriculum Admin role via Admin → Roles tab
         - Go to [Activities tab](#activities-tab)
         - Scroll to "Generate dummy translation opportunities"
         - Enter the number of translation opportunities to generate
         - Click "Generate Translation Opportunities"
         - Navigate to the Contributor Dashboard → Translate Text tab
         - Select a language (for example, Hindi) and a topic to see the generated opportunities
          
     - **Method 2: Load Dummy New Structures Data**
       
       - **Populates:** Translate Text tab (with translation opportunities)
       - **Steps:**
         - Log in as a [Super Admin](#log-in-as-a-super-administrator)
         - Assign yourself the Curriculum Admin role via Admin → Roles tab
         - Go to [Activities tab](#activities-tab)
         - Scroll to "Load dummy new structures data"
         - Click "Load Data"
         - Navigate to the Contributor Dashboard → Translate Text tab to see translation opportunities

  - **Manual method:**

    - **My Contributions**
      - Log in to Oppia
      - Navigate to the Contributor Dashboard
      - Open the Translate Text tab
      - Select a Topic and a Target Language (for example, Hindi)
      ![Translate Text tab](images/Webpage-Guide/translatetext.png)
      - Choose an Opportunity
      - Enter a translation
      - Click Save and Close  
      ![Translate Text tab](images/Webpage-Guide/hinditranslatetext.png)

    - **Available Tasks (Reviewer Rights Required)**
       The Available Tasks section displays suggestions submitted by other users that require review. This section is visible only to users with reviewer rights.
      - Navigate to the Admin page
      -  Open the Roles tab
      -  Enter your username
      -  Select roles: Translation Admin, Question Admin
      -  Click Update
      -  Go to Contributor Admin Dashboard  
      - In Manage Contributor Rights:
        - Enter username  
        - Select category (Translation Reviewer or Question Reviewer)
        - Select language (for example, Hindi)  
        - Click Add Rights  
      ![Contributor Rights](images/Webpage-Guide/contributorhindireview.png)
      - Log in with a different account (or open an incognito window)
      - Submit a translation or question suggestion using the steps above
      ![Contributor Rights](images/Webpage-Guide/acceptedtranslation.png)
      - Log back in with the reviewer account
      - Open Available Tasks
      - Review suggestion  
      ![reviewtranslations](images/Webpage-Guide/reviewtranslations.png)

  - **Accomplishments**
      
     -  Log in with reviewer rights
     -  Go to Available Tasks
     -  Review suggestion
     -  Click Accept  

      **Result:**
      - The contributor’s statistics will update in the Accomplishments tab.  
      - Badges will be awarded automatically when contribution milestones are reached (e.g., 50 accepted translations).
**Note:**  
The Available Tasks section remains hidden until reviewer permissions are granted through the Contributor Admin Dashboard.

### Populating the Story Player

- To populate the Story Player Page:
  - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab).
    (creates a complete topic with a story and 3 chapters in one click).
    
  - **Using Activities Tab generators:**
    
     - Generate or create a topic (Curriculum Admin required)
     -  Use [Generate Stories](#generate-stories) to create stories for that topic
     -  Use [Generate Chapters](#generate-chapters) to create chapters for those stories
    
  - **Manual method:** See [Creating a Topic](#creating-a-topic) and [Populating the Explorations](#populating-the-explorations).
    
### Creating a Classroom
   - **Quick method:**
     
     - Go to [Activities tab](#activities-tab)
     - In the Generate a dummy math classroom section, click the Generate Data button.

   ![Dummy math classroom](images/Webpage-Guide/generatingdummymath.png)
   
   - **Manual method:**
     
     - Open /classroom-admin
     - Click Add New Classroom
       
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

### Creating a Topic
   - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab) (Loads a complete dataset, including: Topics,Skills,Stories,Questions)
   - **Manual method:**
      - Open the Topics and Skills Dashboard.
      - Click on CREATE TOPIC.
      - A form will open where you need to fill:
         - Topic name
         - Topic thumbnail
         - Other required details           
  ![create topic](images/Webpage-Guide/createtopic.png)

         - After saving, you will be redirected to the Topic Editor page.          
 ![Topic Editor page](images/Webpage-Guide/topiceditor.png)
         - In the main editor tab, you will see validation errors that must be fixed before publishing.
    
![warnings](images/Webpage-Guide/warnings.png)
     
Sections in the Topic Editor:
- **Details** – Basic information about the topic
  
- **Subtopics** – Lists subtopics and the skills linked to them
![Subtopics](images/Webpage-Guide/subtopics.png)

**Adding Content to a Subtopic:**
- In the Topic Editor, click on a subtopic name to open the Subtopic Editor.
- Fill in the required fields:
   - **Title** — Name of the subtopic
   - **URL Fragment** — Used in the Study Guide URL
   - **Explanation** — Rich-text content shown on the Study Guide page (click the pen icon to edit)
   - **Thumbnail Image** — Upload a thumbnail
- Under the **Skills** section, skills from the topic are listed. You can remove skills from the subtopic using the options menu.
- Skills are assigned to subtopics by dragging them from the "Uncategorized Skills" section in the main Topic Editor.

- **Diagnostic Tests-**
Add skills that will be used to test learners before recommending this topic.
A skill must have at least 3 questions and be assigned to the topic to be used here.

![Diagnostic Tests](images/Webpage-Guide/diagnostictest.png)

- **Canonical Stories**-
This section lists all stories that belong to this topic.

![Canonical Stories](images/Webpage-Guide/canonicalstories.png)

- Preview the Topic
  
   - Click the Preview button in the top navigation bar
   - This shows exactly how learners will see your topic before publishing.

![Preview the Topic](images/Webpage-Guide/topicpreview.png)

- Publish the Topic
Once all validation errors are resolved:

  - Click Publish Topic
  - Your Topic is now live in the system.

- Add the Published Topic to the Math Classroom
  
  To make your topic visible on the Math Classroom page:

  - Go to http://localhost:8181/classroom-admin
  - Select the classroom (e.g. Math)
  - Click edit (pencil icon)
  - Add the published Topic ID
  - Save changes
  - Verify on the Math Classroom Page: http://localhost:8181/learn/math

 You should now see your newly created topic listed on the classroom page.

### Creating a Skill 
 - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab) (Loads a complete dataset, including: Topics,Skills,Stories,Questions)
   
 - **Manual method:**
   
    NOTE - A skill must have:
   
     - At least **3 questions** to appear in the **Diagnostic Test**
     - At least **10 questions** to appear in **Practice Sessions**

There are two ways to create a skill:

**Method 1: From Topic Editor**

  - Open any Topic Editor
  - Click ADD SKILL under the Subtopics section
  - The skill will be automatically assigned to the topic
    
**Method 2: From Topics and Skills Dashboard**

- Go to the dashboard  
- Click **ADD SKILL**  
- This skill will not be assigned to any topic automatically  

![ADD SKILL](images/Webpage-Guide/newskill.png)

- After saving, you will be taken to the **Skill Editor page**

- Sections inside the Skill Editor:

  - **Details**  
    ![Details](images/Webpage-Guide/populatingdetails.png)

  - **Worked Example**  
    ![Worked Example](images/Webpage-Guide/workedexample.png)

  - **Misconceptions**  
    - These are common mistakes learners make  
    - You can force these misconceptions to appear in all questions  
    ![Misconceptions](images/Webpage-Guide/misconception.png)

  - **Pre-requisite Skills**  
    - These are skills learners should complete first  
    - You can filter by:
      - Topic  
      - Subtopic  
      - Skill name  
    ![Pre-requisite Skills](images/Webpage-Guide/prerequisiteskills.png)

  - **Rubrics**  
    - Helps question creators follow defined standards  
    ![Rubrics](images/Webpage-Guide/rubrics.png)

- Adding questions to a skill:

  - Scroll to the **Questions** section  
  - Click **ADD QUESTION**

  - Inside the **Question Editor**, fill these parts:

    - **Difficulty**  
      ![Difficulty](images/Webpage-Guide/difficulty.png)

    - **Problem**  
      ![Problem](images/Webpage-Guide/skilleditor.png)

    - **Interaction**  
      ![Interaction](images/Webpage-Guide/interaction.png)
 
    - **Answers and Responses**  
      ![Answers and Respones](images/Webpage-Guide/interaction.png)

    - **Hints**  
      ![ADD Hints](images/Webpage-Guide/addhint.png)

  - After filling everything, click **Save**

    ![Save](images/Webpage-Guide/creatingtopicsave.png)
    
### Generate Stories
 - **Quick method:** Use Generate Stories in [Activities tab](#activities-tab)
  
### Generate Chapters
 - **Quick method:** Select a story from the dropdown, enter the number of chapters, and click **Generate Chapters** in [Activities tab](#activities-tab)
 

### Populating the Community Library
Populated when:
- Explorations are published (See [Populating the Explorations](#populating-the-explorations))
- Collections are published  (See [Populating the Collections](#populating-the-collections))
### Populating the New Lesson Player Page
- To populate the New Lesson Player Page:
  - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab)
    
  - **Manual method:**
    - Create classroom (See [Creating a Classroom](#creating-a-classroom))
    - Create topic (See [Creating a Topic](#creating-a-topic))
    - Add stories and chapters (See [Generate Stories](#generate-stories) and [Generate Chapters](#generate-chapters))
    - Link explorations (See [Populating the Explorations](#populating-the-explorations))
    
### Populating the Practice Session Page
- To populate the Practice Session Page:
   - **Manual method:** Create a topic with skills that have at least 10 questions each. Then enable "Show Practice Tab to learners" in the [Topic Editor](#topic-editor-page). See [Creating a Skill](#creating-a-skill) and [Creating a Topic](#creating-a-topic).

**Note**

Even after adding 10 questions to the skills in a topic, the Practice Session route will return a 404 until you open the Topic Editor and explicitly check the "Show Practice Tab to learners" checkbox. This checkbox remains disabled until the 10-question minimum is met.

### Populating the Study Guide Page
- To populate the Study Guide Page it needs a published topic in a classroom, with a subtopic that has content, a thumbnail, and skills assigned.
   - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab)
     
   - **Manual method:** See [Creating a Topic](#creating-a-topic)


### Populating the Topic Viewer Page
- To populate the Topic Viewer Page it needs a topic with stories, subtopics, and skills, published and added to a classroom.
    - **Quick method:** Use Load Dummy New Structures Data in [Activities tab](#activities-tab)
      
    - **Manual method:** See [Creating a Classroom](#creating-a-classroom) and [Creating a Topic](#creating-a-topic)
      
### Populating the Classroom Page
- To populate the Classroom Page: See [Creating a Classroom](#creating-a-classroom)
  
### Populating the Review Test Page

- To populate the Review Test Page:
  
     - **Quick method:**
       
       - Go to http://localhost:8181/admin -> Activities tab and click Load dummy new structures data once
       - Go to http://localhost:8181/classroom-admin, edit the "Math" classroom, and add the ID of "Dummy Topic 1" to the topics list
       - Open the Topic Editor for "Dummy Topic 1". Under the Canonical Stories tab, open the "Help Jaime win the Arcade" story.
       - Click on each chapter (node) and manually add the generated dummy skills to the Acquired Skills section, then save.
       - Log in as a student and complete at least one chapter. Once finished, the Review Test for those skills will be unlocked.
  
     - **Using Activities Tab generators:**
       
       - Generate a topic, then use the Generate Stories and Generate Chapters buttons in [Activities tab](#activities-tab).
       - Use Generate Skills to create at least 3 skills for the topic in [Activities tab](#activities-tab).
       - Use Generate Question Suggestions to add questions to those skills in [Activities tab](#activities-tab).
       
     - **Manual method:**
       - Create a topic, story, and chapters in the Topic Editor. (See [Creating a Topic](#creating-a-topic))
       - Assign skills with questions to those chapters, publish everything, and complete the chapters as a learner.
       
Note: The "Load dummy new structures data" button generates a basic structure but requires manual linking in the Classroom Admin and Topic Editor to fully function. Additionally, some reloaded explorations may be missing interaction data (such as multiple-choice options), which can occasionally prevent a learner from reaching the completion screen required to unlock the Review Test.

