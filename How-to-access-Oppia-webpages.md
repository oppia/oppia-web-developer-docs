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

The About page provides a brief overview of information about Oppia. It details the goals of the Oppia organization and provides links to guides and tutorials on how to explore Oppia

1. Click on the About menu at the top navigation Bar
2. Click on the “About Oppia” link

![AboutPageLink](images/Webpage-Guide/aboutPageLink.png)

**Collection_editor**
1. Navigate to the Admin webpage
2. Go to roles tab in Admin page

![Admin Role Tab](https://user-images.githubusercontent.com/16653571/41501684-a543b22e-71c6-11e8-883c-cec35e32535e.png)

3. Assign your username as a collection editor

![assignrole](https://user-images.githubusercontent.com/16653571/41503346-ff754c9e-71ee-11e8-9b72-9e16dae46418.png)

4. Navigate to the splash page and click on the “Create” button in the top navigation bar

![Create Button](https://user-images.githubusercontent.com/16653571/41504441-a7f60512-720c-11e8-85c2-8fee5f55a42c.png)

5. Select “Create Collection”

![CREATE COLLECTION button](https://user-images.githubusercontent.com/16653571/41504483-d946fd3c-720d-11e8-997d-943cd8703e57.png)

**Collection-Player Page**
1. Login into Oppia and change role to collection_editor
2. Go to the admin activities tab and reload the collection “welcome_to_collections.yaml”

![Reload Collections](images/Webpage-Guide/reloadCollections.png)

3. Navigate back to the community-library page and type in the search bar “collections”
4. Click on the card titled Introduction to collections in Oppia

**Contact Page**
1. Click on the About menu at the top navigation Bar
2. Click on the “Contact Us” link

**Creator-Dashboard Page**
1. Login into Oppia
2. Navigate to the Creator-Dashboard page at http://localhost:8181/creator-dashboard

**Contributor-Dashboard Page**
1. Login into Oppia
2. Navigate to the Contributor-Dashboard page at http://localhost:8181/contributor-dashboard

**Delete-Account Page**
1. Go to constants.ts and change "ENABLE_ACCOUNT_DELETION": false -> true
2. Navigate to http://localhost:8181/delete-account

**Donate Page**
1. Go to http://localhost:8181/donate
Or click on the donate button in the navigation bar

**Emaildashboard Page**
1. Login into Oppia and change role to Admin
2. Navigate to http://localhost:8181/emaildashboard

**Exploration-Editor Page**
1. Login into Oppia
2. Click the create button on the top right

**Exploration-Player Page**
1. Navigate to
http://localhost:8181/community-library
2. Enter fractions into the search bar
3. Click on the exploration titled ‘Fractions 1 - What is the Fraction?’

**Get-Started Page**
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