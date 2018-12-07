# Aim of the project:
  To make people with disability feel comfortable in using Oppia. The project will increase the accessibility.
# Features to be added during this project
  1. Use google analytics in translation tab 
  2. Use of Aria for increasing accessibility of the translation tab
  3. Test cases for the Aria
  4. Use of tab to navigate throughout the translation tab
# Milestones of the project
  1. Add google analytics for usage of translation tab 
  2. Add keyboard shortcuts for start and stop recordings
  3. Tabbing through the translation tab
  4. Writing test case for accessibility
# Technical Design and implementation (The flowchart will be as per the milestones)
  1. Adding translation tab usage in SiteAnalyticsService.js so as to keep record of its usability
  2. Shortcut key to start recording 
      1. Use of space-bar will be most comfortable as the key shape identical 
      2. The audio will start recording as the key is hit and stop if the key is pressed again.
      3. To upload a file we will use tabbing.
  3. Tabbing is important as it give a full control to website using keyboard
      1. Use of Aria will give a easy and comfortable use of tabbing through the translation tab
      2. Use of tab to select different options in translation tab can also be used if user have screen reader which will read out the title or labels of that option.
  4. Finally writing test case on accessibility
      1. Writing color contrast tests for better look
      2. Writing test for labels and title so that Aria gets it correctly
      3. Some test case will also check the tabbing process.
# My involvement
  This project is my first open source project as well as my first project for oppia other than solving some small issues. I hope you will be satisfied with my work as well as users will get a new experience in using this new feature