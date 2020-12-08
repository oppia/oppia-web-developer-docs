# How to access Oppia webpages
Oppia has many webpages and this is a comprehensive guide on how to access all those pages. Before a contributor makes a PR, we expect that the contributor has thoroughly tested the changes made in the PR for functional correctness. Part of this process is manually testing any pages that are affected by their code.

## Sign Up (As Administrator)

Many Oppia Pages require authentication to access. In order to sign in:
1. Click the sign-in button on the top left navigation bar
![Sign-In Button](images/Webpage-Guide/signInButton.png)

2. Once redirected to the login page, click the **Sign in as Administrator checkbox** and then login.

![Sign-In page](https://user-images.githubusercontent.com/16653571/41500954-e88a0262-71b8-11e8-9cac-456fb46782c1.png)

## Webpage Guide

**Admin Page**

The Admin page is a page exclusively for developers. It has many functionalities including changing permissions, configuration values, and running jobs. Certain webpages cannot be accessed unless the current user does not have the required permissions. 

1. Login into the Oppia as an administrator

![Sign-In page](https://user-images.githubusercontent.com/16653571/41500954-e88a0262-71b8-11e8-9cac-456fb46782c1.png)

2. Go to the profile menu and click on the "Admin" link

![Admin Panel Link](https://user-images.githubusercontent.com/16653571/41501009-e04e9a76-71b9-11e8-958e-985f5bc7122a.png)

**About Page**

The About page provides a brief overview of Oppia. It details the goals of the Oppia organization, credits its contributors, and provides links to guides and tutorials on how to further explore Oppia

1. Click the About Menu button on the top right navigation bar

2. Click on the “About Oppia” link

![AboutPageLink](images/Webpage-Guide/aboutPageLink.png)

**Collection_editor**

The Collection editor page allows users to create collections in Oppia. The collection editor page can only be accessed by users with the role _COLLECTION_EDITOR_

1. Navigate to the Admin page
2. Click the **ROLES** tab

![Admin Role Tab](https://user-images.githubusercontent.com/16653571/41501684-a543b22e-71c6-11e8-883c-cec35e32535e.png)

3. Change the role of your username to _COLLECTION_EDITOR_

![assignrole](https://user-images.githubusercontent.com/16653571/41503346-ff754c9e-71ee-11e8-9b72-9e16dae46418.png)

4. Exit the Admin page, and navigate to the splash page (http://localhost:8181/splash) 
5. Click on the “Create” button in the top navigation bar 

![Create Button](https://user-images.githubusercontent.com/16653571/41504441-a7f60512-720c-11e8-85c2-8fee5f55a42c.png)

5. Select “Create Collection”

![CREATE COLLECTION button](https://user-images.githubusercontent.com/16653571/41504483-d946fd3c-720d-11e8-997d-943cd8703e57.png)

**Collection-Player Page**

The Collection player page allows users to explore collections in Oppia.

1. Login into Oppia and change role to collection_editor
2. Go to the admin activities tab and reload the collection “welcome_to_collections.yaml”

![Reload Collections](images/Webpage-Guide/reloadCollections.png)

3. Navigate back to the community-library page and type in the search bar “collections”
4. Click on the card titled Introduction to collections in Oppia

**Contact Page**

The Contact page details the ways to communicate with the Oppia team and get involved

1. Click on the About menu at the top navigation Bar
2. Click on the “Contact Us” link

**Creator-Dashboard Page**

The Creator-Dashboard page allows users to view all explorations they have created, or are currently creating

1. Login into Oppia
2. Navigate to the Creator-Dashboard page at http://localhost:8181/creator-dashboard

**Contributor-Dashboard Page**

The Contributor-Dashboard page allows users to translate existing explorations into a different language, or create questions for existing Oppia explorations

1. Login into Oppia
2. Navigate to the Contributor-Dashboard page at http://localhost:8181/contributor-dashboard

**Delete-Account Page**

The Delete-Account page allows users to delete their accounts. Currently, it is deactivated and certain code needs to be changed to access it.

1. Go to constants.ts and change "ENABLE_ACCOUNT_DELETION": false -> true
2. Navigate to http://localhost:8181/delete-account

**Donate Page**

The Donate Page provides a way for people to donate to the Oppia organization

1. Go to http://localhost:8181/donate or click on the donate button in the navigation bar

**Emaildashboard Page**
1. Login into Oppia and change role to Admin
2. Navigate to http://localhost:8181/emaildashboard

**Exploration-Editor Page**

The Exploration-Editor page allows users to create explorations in Oppia.

1. Login into Oppia
2. Click the create button on the top right

**Exploration-Player Page**

The Exploration-Player page allows users to play explorations in Oppia.

1. Navigate to
http://localhost:8181/community-library
2. Enter fractions into the search bar
3. Click on the exploration titled ‘Fractions 1 - What is the Fraction?’

**Get-Started Page**

The Get-Started page allows users to play explorations in Oppia.

1. Navigate to http://localhost:8181/get-started

**Landing Pages**
1. Navigate to http://localhost:8181/teachers

**Skill Editor Page**
1. Set Role to Admin 
2. Go to topic_and_skills_dashboard and create a topic
3. Go to the topic editor and scroll down to the Create Skill button
4. Create a skill, and wait for the skill editor tab to open

**Story Editor Page**
1. Set Role to Admin

![assignrole](https://user-images.githubusercontent.com/30312043/78745056-b8b70b80-7980-11ea-942a-b2aab314c201.png)

2. Go to topic_and_skills_dashboard and create a topic

![createtopic](images/Webpage-Guide/createTopicModal.png)

3. Go to the topic editor and click on the Add Story button

![createtopic](images/Webpage-Guide/addStoryButton.png)

4. Complete create story modal, and wait for the story editor page to load

![createtopic](images/Webpage-Guide/addStoryModal.png)

**Story Player Page**
1. Follow steps in story editor page
2. Add a chapter to the story 
3. Create an exploration and link it to the story
4. Go to the Preview tab of the Story player

**Topic editor/Subtopic Player Page**
1. Set Role to Admin 

![assignrole](https://user-images.githubusercontent.com/30312043/78745056-b8b70b80-7980-11ea-942a-b2aab314c201.png)

2. Go to topic_and_skills_dashboard and create a topic

![Create Button](https://user-images.githubusercontent.com/30312043/78745178-06cc0f00-7981-11ea-9eca-f4495e05b0e4.png)

3. Create some skills and a topic and assign these skills to the topic.
4. Edit and publish the topic after adding subtopics (add some content for these), and a story with few chapters.
5. Use the preview button to navigate to the topic player

**Preferences Page**
1. Sign into Oppia
2. Go to http://localhost:8181/preferences

**Profile Page**
1. Sign in to Oppia
2. Click on the profile menu and click your username to go to the profile page

**Community-Library Page**
1. Sign in to Oppia
2. Go to http://localhost:8181/community-library

**Topic_And_Skills_Dashboard Page**
1. Set Role to Admin 
2. Go to http://localhost:8181/topics-and-skills-dashboard or click the topic and skills dashboard link

![Create Topic Button](images/Webpage-Guide/topicAndSkillDashboardLink.png)

**Thanks Page**
1. Go to http://localhost:8181/thanks

**Terms Page**
1. Go to http://localhost:8181/terms