# django-app

## Problem 1: Migration applied before its dependency
Follow next steps:
* delete this file : migrations\0001_initial.py
* delete this : db.sqlite3
* put this code in settings.py : AUTH_USER_MODEL = 'users.CustomUser'
* Then do (makemigrations) then (migrate )
Reference: [Migration applied before its dependency](https://stackoverflow.com/questions/38996599/django-manage-py-migration-applied-before-its-dependency)