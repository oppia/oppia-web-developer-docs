## NOTE: This page is under development.

### 1. ADD ROLE
1.1 Open file feconf.py.

1.2 Search for `ROLE_ID_GUEST` to go to the appropriate place where role Ids are defined.

1.3 Add a constant for the new role string (follow the convention used in defining other roles).

1.4 Go to core/domain/role_services.py.

1.5 [_If a user can be updated to this role via admin interface_] Search `UPDATABLE_ROLES` and add the role Id in the list.

1.6 [_If a user can be viewed by this role via admin interface_] Search `VIEWABLE_ROLES` and add the role Id in the list.

1.7 Search `HUMAN_READABLE_ROLES` and add the corresponding entry for this role.

1.8 Search `PARENT_ROLES` and add a new entry for the role.
- key -> the role variable from feconf.
- value -> list of roles from which this role inherits actions.

1.9 Search `ROLE_ACTIONS` and add a new entry for the role.
- key -> the role variable from feconf.
- value -> empty list.
To add actions corresponding to this role follow instructions [here](#add_action).

1.10 Run backend test corresponding to role changes `bash scripts/run_backend_tests.sh --test_target=core.domain.role_services_test`.

1.11 Follow instructions here to attach users to this role.


***

### 2. REMOVE ROLE
2.1 Make sure no user is attached to the role you are going to delete. Instructions to [view role](#view_user_role) and [update role](#update_user_role).

2.2 Go to core/domain/role_services.py

2.3 Search `UPDATABLE_ROLES`, `VIEWABLE_ROLES` and `HUMAN_READABLE_ROLES`. Delete the entry corresponding to this role (if any).

2.4 Go to ROLE_ACTIONS to delete the role from here:
- delete all actions from ROLE_ACTIONS[role_to_delete] instructions to remove action are [here](#remove_action).
- Remove the role from ROLE_ACTIONS.

2.5 Go to PARENT_ROLES to delete the role from here:
- Add elements in role’s list to all its children.
- Remove the role from ROLE_ACTIONS.

2.6 Go to feconf.py and delete the role Id variable corresponding to this role from here.

2.7 Run backend test corresponding to role changes `bash scripts/run_backend_tests.sh --test_target=core.domain.role_services_test`.

***

### 3. <a name="add_action"></a> ADD ACTION
3.1 Implement decorator corresponding to this action in domain/action_decorators.py and apply it in necessary places.

3.2 To make this action work, you have to add this to ROLE_ACTIONS. Go to core/domain/role_services.py

3.3 Search `ACTION_` and add constant variable corresponding to the action.

3.4 Search `ROLE_ACTIONS` and add the action to the appropriate role (minimum role required to perform this action).

***

### 4. <a name="remove_action"></a> REMOVE ACTION
4.1 Remove the corresponding decorator of action from domain/action_decorators.py and from wherever it is applied.

4.2 Go to file core/domain/role_services.py.

4.3 Remove the constant corresponding to this action.

4.4 Remove the role from ROLE_ACTIONS dict.

***

### 5. <a name="view_user_role"></a> VIEW USER ROLE
5.1 There are two ways by which you can see user’s role (by role and by username).

5.2 Go to /admin#roles.

5.3 Fill the form to view roles.

***

### 6. <a name="update_user_role"></a> UPDATE USER ROLE
6.1 Go to /admin#roles.

6.2 Fill the form to update user’s role.

***

### 7. VIEW ROLE HIERARCHY
7.1 Go to /admin#roles.

7.2 Role Hierarchy is shown on the page.

***

### 8. UPDATE_ROLE_HIERARCHY
8.1 Existing role hierarchy can be seen on /admin#roles page.

8.2 Go to core/domain/role_services.py.

8.3 Update the list values in PARENT_ROLES dict to adjust hierarchy and go to /admin#roles to view the changes.
