- after creating database model update in settings.py as
  AUTH_USER_MODEL='account.user'

  then python3 manage.py makemigrations
  python3 manage.py migrate

templates from core/templates/core/base.html can access account/templates/account/signup.html
via {% extends "core/base.html" %}
