- after creating database model update in settings.py as
  AUTH_USER_MODEL='account.user'

  then python3 manage.py makemigrations
  python3 manage.py migrate

templates from core/templates/core/base.html can access account/templates/account/signup.html
via {% extends "core/base.html" %}

- django have inbuilt authentication system
- so if you can authicate use authicate directly
- csrf token when doing with forms
- login will directly create a session tokens and can validate accordingly
-

- after updateing views then should immedialtly take care of the urls.py also
