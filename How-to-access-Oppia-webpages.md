This is a quick guide on how to access webpages on the Oppia dev server.

**Admin Page**
1. Login into the Oppia as an administrator
2. Go to the profile menu and click on the "admin" link

**About Page**
1. Click on the About menu at the top navigation Bar
2. Click on the “About Oppia” link

**collection_editor**
1. Login into Oppia and change role to collection_editor
2. Navigate to the creator dashboard and click on the “Create” button in the top navigation bar
3. Select “Create Collection”

**Collection_player**
1. Login into Oppia and change role to collection_editor
2. Go to the admin activities tab and reload the collection “welcome_to_collections.yaml”
3. Navigate back to the community-library page and type in the search bar “collections”
4. Click on the card titled Introduction to collections in Oppia

**contact**
1. Click on the About menu at the top navigation Bar
2. Click on the “Contact Us” link

**Creator_dashboard**
1. Login into Oppia
2. Navigate to the creator dashboard page at http://localhost:8181/creator-dashboard

**contributor-dashboard webpage **
1. In feconf.py change variable  COMMUNITY_DASHBOARD_ENABLED = True
2. Login into Oppia and change role to Admin
3. Go to the community-dashboard webpage

**delete_account webpage**
1. Go to constants.ts and change "ENABLE_ACCOUNT_DELETION": false -> true
2. Navigate to http://localhost:8181/delete-account

**Donate**
1. Go to http://localhost:8181/donate
Or click on the donate button in the navigation bar

**12. email_dashboard**
1. Login into Oppia and change role to Admin
2. Navigate to http://localhost:8181/emaildashboard

**13. email_dashboard_result**
1. Login into Oppia and change role to Admin
2. Navigate to http://localhost:8181/emaildashboard
3. Submit a query and click on the link provided

**14. Exploration_Editor**
1. Login into Oppia
2. Click the create button on the top right

**15. Exploration_Player**
1. Navigate to
http://localhost:8181/community-library
2. Enter fractions into the search bar
3. Click on the exploration titled ‘Fractions 1 - What is the Fraction?’

**16. Get_Started**
1. Navigate to http://localhost:8181/get-started

**17. Landing pages**
1. Navigate to http://localhost:8181/teachers

**18. Skill_Editor**

1. Set Role to Admin 
2. Go to topic_and_skills_dashboard and create a topic
3. Go to the topic editor and scroll down to the Create Skill button
4. Create a skill, and wait for the skill editor tab to open

**19. Story_Editor**
1. Set Role to Admin 
2. Go to topic_and_skills_dashboard and create a topic
3. Go to the topic editor and scroll down to the Create Story button
4. Complete create story modal, and wait for the story editor page to load

**20. Story Player**
1. Follow steps in story editor CUJ
2. Add a chapter to the story 
3. Create an exploration and link it to the story
4. Go to the Preview tab of the Story player

**21. Topic editor/Subtopic Player**
1. Set Role to Admin 
2. Go to topic_and_skills_dashboard and create a topic
3. Activate your Screen reader go through the checklist (For topic editor)
4. Create some skills and a topic and assign these skills to the topic.
5. Edit and publish the topic after adding subtopics (add some content for these), and a story with few chapters.
6. Use the preview button to navigate to the topic player

**22. Preferences**
Sign into Oppia
Go to http://localhost:8181/preferences

**23. Profile**
1. Sign in to Oppia
2. Click on the profile menu and click your username to go to the profile page

**24. Community-library**
1. Sign in to Oppia
2. Go to http://localhost:8181/community-library


**25. Topic_and_skills_dashboard**
1. Set Role to Admin 
2. Go to topic_and_skills_dashboard and create a topic and create a skill
3. Go back to the topic_and_skills_dashboard

**26. Thanks**
Go to http://localhost:8181/thanks

**27. Terms**
1. Go to http://localhost:8181/terms

**28. Sign Up (run locally on release)**
1. Click the sign-in button on the top navigation bar
2. Go through the login page
3. Wait for redirection to sign up page


