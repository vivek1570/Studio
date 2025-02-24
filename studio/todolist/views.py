from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Todo
from project.models import Project

@login_required
def add_todo(request,project_id):
    project=Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method=='POST':
        name=request.POST.get('name','')
        description=request.POST.get('description','')

        if name:
            Todo.objects.create(project=project,name=name,description=description,created_by=request.user)

            return redirect(f'/projects/{project_id}/')
    return render(request,'todolist/add.html',{
        'project':project
    })

# def todos(request,project_id):
#     todos=Todo.objects.filter(project_id=project_id)

#     return render(request,'')