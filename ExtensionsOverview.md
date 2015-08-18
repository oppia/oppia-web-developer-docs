# Creating Extensions #

These pages explain how to create new interactions and associated code, and how to integrate them with Oppia.

Each state/card of an Oppia exploration contains an [interaction](InteractiveWidgets.md) which receives an answer from the reader and sends it to the Oppia backend. Based on this answer, Oppia then determines what to show next to the reader.

Currently, new interactions must be added by the owner of the Oppia application by making a change to the code. However, you are very welcome to [submit interactions](Contributing.md) to the Oppia codebase for inclusion in the main Oppia release -- though if you would like to do this, we'd encourage you to get in contact with us prior to writing the interaction, in order to ensure that it is a good fit and to minimize duplication of work. Please note that submissions will go through a review process, and that we might ask you to make certain modifications (usually in order to make the submission more general). We might also decide that it would be better not to include the interaction in the main codebase, and if this ends up being the case, we will communicate this as early as possible.

**Important!** The following specifications for interactions and associated code are not yet set in stone, and are still evolving. We cannot guarantee backwards-compatibility yet, and will update this notice when that changes. However, we will update existing interactions in the core Oppia codebase if any changes are made to how interactions are defined.

### Documentation ###

Interactions and associated objects are related as follows:

<img src='https://raw.githubusercontent.com/oppia/oppia/wiki/images/extensionsOverview.png' width='500'>

The arrows indicate dependencies, so each interaction parameter must specify both a value generator and an object type, while the interaction handler must specify an object type (that will be sent to the backend when a reader submits an answer to the interaction). The rules available to the exploration creator will be all of those associated with the interaction handler's object type. Interactions must be enabled in <code>feconf.py</code>.<br>
<br>
The following links lead to pages that describe, in more detail, how to create each of these extensions.<br>
<br>
<ul><li><a href='CreatingInteractions.md'>Interactions</a>
</li><li><a href='CreatingObjects.md'>Objects</a>
</li><li><a href='CreatingValueGenerators.md'>Value generators</a>
</li><li><a href='CreatingRules.md'>Rules</a>
</li><li><a href='CreatingDependencies.md'>Dependencies</a>
