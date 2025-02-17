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

- we can use like below, where the dictionary indicating that we can pass values to the html file

```python

def projects(request):
    projects=Project.objects.filter(created_by=request.user)
    return render(request,'project/projects.html',{
        'my_projects':projects
    })


```

- you can add a delete button in that by passing id as paramenetr to the url
