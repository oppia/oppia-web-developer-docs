### Populating translation opportunities
- Start a local server and sign in as an administrator (testadmin@example.com, assume username “a”).
- Navigate to the Admin page.
- Click the Roles tab.
- In the Role editor, enter the admin username (“a”). Click Add Role, and add the “Curriculum Admin” role.
- Navigate to the Activities tab. Click Load Data under Load dummy new structures data.
- You should now see translation opportunities in the Translate Text tab at /contributor-dashboard.


### Populating question opportunities
- Start server and sign in as administrator (assume username “a”).
- Navigate to the Admin page.
- Click the Roles tab.
- In the Role editor, enter the admin username (“a”). Click Add Role, and add both the “Curriculum Admin” role and “Question Admin” role.
- Go to http://localhost:8181/contributor-dashboard-admin and give submit question rights and review questions rights to your current username
- Navigate back to the Admin page and navigate to the Activities tab. Click Load Data under Load dummy new structures data.
- For the question opportunities to be valid, their corresponding topics must be part of a classroom topic. Navigate to the Config tab. Click Add element under [topic_id] (in the “The details for each classroom page.” section) and enter the topic id for the new topics that were created. (You can find a topic’s ID in its page URL from the Topic and Skills Dashboard). Make sure to click save at the bottom of the config page.
- To enable the “Submit Question” tab for your user, make sure your signed in user is allowlisted for submitting question suggestions.
