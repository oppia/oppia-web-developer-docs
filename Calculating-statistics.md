<!-- This guide was created by Stephanie Federwisch as a Google document and then transferred to the wiki. -->

This page should walk you through how to go from a statistic you want to calculate from Oppia data through creating the models, jobs and getting them up and running. For each step of the process, we've included a reference to an example Pull Request which will provide a good idea of what that step includes.

This document walks through how to create each of these levels.

The recommended way of going through this process is to:
 * Plan the overall approach: start at the presentation layer and work your way down the layers to the event log (steps 1 - 4 in the diagram below). This will not involve writing code.
 * Write code to record the data you need for your calculations (steps 5-7).
 * Use the data in the UI (step 8).

Each of these three sections will be a separate commit in a branch off of develop. After all the steps are completed and reviewed, this branch can be merged into develop.

## 1-4. Figuring out what you need

1. Start by thinking about what you want to display. This could mean drawing charts and/or listing out data you want to display.
2. List out processed data fields. Figure out which data you need to display and find one field for each. For example, a bulleted list would have one field in the model for each bullet point. A histogram could be drawn by having a list of data point values, but if you want to have standard deviation or mean, you would want to have separate fields for those as well.
3. Map out how you would calculate each field in your model. For some fields this may be straightforward, like how counting how many students go to the page for a number of students that started the exploration, whereas others might be more complex and this stage may take a while, like how confused are students.
4. Figure out what interactions you would need to keep track of to do those calculations. For mapping out completions of an exploration, this might be “I need to know when students complete the exploration.” Keep in mind when you would record these events. So if you wanted to know an average time spent in a particular state it would become “I need to know how much time was spent in the state when the student leaves the exploration”.

So, you have a model of what you want to create and you know which model it should be in.

## 5. Creating the events

1. (Example: [#3841](https://github.com/oppia/oppia/pull/3841)) Changes to core.storage.statistics.gae_models.py:
   
    1. Define a class of the form <statistic_name>EventLogEntryModel. Each instance of this model will account for one count of the statistic you want to record. Make sure this model contains all the information you would need to identify the context of an instance of this model (exploration_id, schema_version etc...). Instances of this event model will be used to recompute the statistics aggregated model if there are any data discrepancies.

        1. Now, add the statistic count as a field of the ‘ExplorationStatsModel’ in the same file. The field should be named <statistic_name>_v2. Also keep in mind to update the corresponding getter methods and also, the save and retrieve methods for this model.

2. (Example: [#3857](https://github.com/oppia/oppia/pull/3857)) Changes to ‘core.domain.stats_domain.py’:

    1. Add the statistics field respectively in the ExplorationStats class and similarly modify corresponding helper methods.
    2. If it is a state level statistic, modify the StateStats class instead of the ExplorationStats class.

## 6. Create Backend Handlers for incoming statistics

1. (Example: [#3916](https://github.com/oppia/oppia/pull/3916/files#diff-7dae2fea02c39c3f79ba7f502b2ec181)) Now, open the file ‘core.controllers.reader.py’.

    1. First, add validation for this new field in the class ‘StatsEventHandler’. This event handler will be updating the aggregated statistics model.
    2. Then, create a new EventHandler for the new statistics, of the form ‘<statistics_name>EventHandler’. This will be the event handler that records an instance of each count for the statistic.

2. (Example: [#3916](https://github.com/oppia/oppia/pull/3916/files#diff-5bc02cefb3ea9e27f1a6776eabd1935d)) Now, open the file ‘main.py’. Create a route through which the event models will be recorded.

## 7. Record events from the User

1. (Example: [#3916](https://github.com/oppia/oppia/pull/3916/files#diff-d12d8529029e2a0c1b2430573bace920)) Open the ‘core.templates.dev.head.pages.exploration-player-page.services.stats-reporting-service.ts’. Add a method to this file for handling any record of the event. The function name can be of the form ‘record<statisticName>’. This function performs two things:

    1. Make a $http.post() call to the URL we created in step 6 (part 2) with the respective args to record an instance of the event log entry model.
    2. Increment count for this statistic field in the aggregatedStats dictionary which holds the values for the ExplorationStatsModel. Periodic calls will automatically be sent to the StatsEventHandler automatically to update the ExplorationStatsModel.

2. (Example: [#3916](https://github.com/oppia/oppia/pull/3916/files#diff-4d9e2d3cc0a2b28fdbdb3585b080610e)) Now, we need to figure out where in the player view recording will be required. For state related stats, we would probably capture our new statistic on entering a state or leaving a state. For answer related stats, you’d probably capture your statistic inside the submitAnswer function in the player view.

## 8. Using it in the UI

Now, your newly added statistic will be available in the ExplorationStatsModel. You should find that the ExplorationStatsModel has already been retrieved in the statistics tab. Visualizing your newly added statistic will be simply using the corresponding field from the stats model in the view.



Well, that’s the gist of it. Have fun recording your stats, and don’t forget to write tests throughout the way.