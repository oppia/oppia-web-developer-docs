# Table of contents
- [Populating translation opportunities](#populating-translation-opportunities)
- [Populating question opportunities](#populating-question-opportunities)
- [Generating explorations](#generating-explorations)
- [Creating a Classroom](#creating-a-classroom)

### Populating translation opportunities
1. Start a local server and sign in as an administrator (testadmin@example.com, assume username “a”).
2. Navigate to the Admin page.
3. Click the Roles tab.
4. In the Role editor, enter the admin username (“a”). Click Add Role, and add the “Curriculum Admin” role.
5. Navigate to the Activities tab. Click Load Data under Load dummy new structures data.
6. You should now see translation opportunities in the Translate Text tab at /contributor-dashboard.


### Populating question opportunities
1. Start the server and sign in as administrator (assume username “a”).
2. Navigate to the Admin page.
3. Click the Roles tab.
4. In the Role editor, enter the admin username (“a”). Click Add Role, and add both the “Curriculum Admin” role and “Question Admin” role.
5. Go to http://localhost:8181/contributor-admin-dashboard and grant submit-question and review-question rights to your current username
6. Navigate back to the Admin page, then go to the Activities tab. Click Load Data under Load dummy new structures data.
7. For the question opportunities to be valid, their corresponding topics must be part of a classroom topic. Navigate to the classroom admin page: `http://localhost:8181/classroom-admin`.
8. Click **Add New Classroom** (or edit an existing classroom), and add the relevant **topic IDs** to the classroom. Save your changes.
9. To enable the “Submit Question” tab for your user, make sure your signed-in user is allowlisted for submitting question suggestions.

### Generating explorations
1. To generate data, we must first navigate to the admin page. We will automatically be redirected to the `ACTIVITIES` tab.
2. This tab will have several sections:
   1. Reload a single exploration: This section has preloaded explorations. These can be loaded onto your local server by clicking the `Reload` button for each of them.
   2. Generate dummy explorations: Along with the option to generate dummy explorations (with no content), we can also publish a certain number of them.
   3. Reload a single collection: This section has preloaded collections.
   4. Load dummy new structures data: This section provides a combination of topics, skills, stories, and exploration.
   5. Generate dummy skill with questions.
   6. Generate a dummy math classroom.

### Creating a Classroom
1. Navigate to the Admin roles tab (`/admin`) and assign the **Curriculum Admin** role to yourself.
2. Go to the classroom admin page: `http://localhost:8181/classroom-admin`.
3. Click **Add New Classroom**, then add the classroom name and URL fragment.
4. Edit the classroom details and add the course details, topic intro, and **topic IDs** to the classroom.
5. Save your changes. The newly created classroom will be visible on the learner dashboard Home tab, or you can access it from `http://localhost:8181/learn/`.
