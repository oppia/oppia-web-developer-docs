Oppia users are associated with a role. There are multiple roles in the Oppia platform, each role is independent and associated with a set of actions. The user role defines the actions which the user can perform on the Oppia platform.


Editing roles and actions for the platform can be done using the following instructions: 
## Adding a new role
1. Open file feconf.py.
2. Search for ROLE_ID_GUEST to go to the appropriate place where role Ids are defined.
3. Add a constant for the new role string (follow the convention used in defining other roles).
4. Go to core/domain/role_services.py.
   1. If a user can be updated to this role via the admin interface
      1. Search UPDATABLE_ROLES and add the role Id to the list.
   2. If a user can be viewed by this role via the admin interface
      1. Search VIEWABLE_ROLES and add the role Id to the list.
   3. Search HUMAN_READABLE_ROLES and add the corresponding entry for this role.
   4. Search _ROLE_ACTIONS and add a new entry for the role.
      1. key → The role variable from feconf.
      2. value -> The list of actions allowed for the role.
5. Run backend test corresponding to role changes python -m scripts.run_backend_tests --test_target=core.domain.role_services_test.
6. Manually test the changes by [assigning the new role to a user](#assigning-a-role-to-a-user) and through [roles and actions visualizer](#roles-and-actions-visualizer).

## Removing the existing role
1. Make sure no user is attached to the role you are going to remove. 
   1. Write a one-off job to audit to check whether a user is associated with such a role.
   2. Write a one-off job to remove such a role from the users, if it exists. [Talk to admins before planning the removal.]
2. Open core/domain/role_services.py in the editor
   1. Search UPDATABLE_ROLES, VIEWABLE_ROLES, and HUMAN_READABLE_ROLES. Delete the entry corresponding to this role (if any).
   2. Check _ROLE_ACTIONS and [remove all unique actions](#removing-existing-action) allocated to the given role. 
   3. Remove the role entry from ROLE_ACTIONS
3. Open feconf.py and delete the ROLE_ID* variable corresponding to the given role.
4. Run backend test corresponding to role changes python -m scripts.run_backend_tests --test_target=core.domain.role_services_test.
5. Manually test the changes
   1. Roles and actions visualizer should not show the given [role and associated unique actions](#roles-and-actions-visualizer).


## Adding new action
1. Open core/domain/role_services.py
   1. Search for “ACTION_”, and add a constant variable corresponding to the new action.
   2. Search for “ROLE_ACTIONS” and add the new action to the appropriate roles.
2. Implement a decorator corresponding to this action in controllers/acl_decorators.py and apply it in necessary places.
3. Implement the tests for the new decorator in controllers/acl_decorators_test.py, in order to check the proper functioning of this decorator.

## Removing existing action
1. Open core/domain/role_services.py.
   1. Search ACTION_ and remove the constant corresponding to this action.
   2. Remove the action from ROLE_ACTIONS.
2. Remove the corresponding decorator of action (and corresponding tests) from controller/action_decorators.py and from wherever it is applied.


## Assigning a role to a user
1. Go to /admin
2. Switch to the “Roles” tab
3. Fill in the form “Update Role”
   1. Enter the username of the user
   2. Select the role.
4. Click the “Update role” button

## View user role
1. There are two ways by which you can see the user’s role (by role and by username)
2. Go to /admin#roles
3. Fill in the form to view roles

## Roles and actions visualizer
1. Go to /admin
2. Switch to the “Roles” tab
3. “Role and actions” card will appear on the right side of the page
4. Click the role you’re interested in to check the actions allocated to the selected role.