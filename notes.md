- after creating database model update in settings.py as
  AUTH_USER_MODEL='account.user'

  then python3 manage.py makemigrations
  python3 manage.py migrate
