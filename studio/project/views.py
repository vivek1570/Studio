from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.

@login_required
def projects(request):
    projects=Project.objects.filter(created_by=request.user)
    return render(request,'project/projects.html',{
        'my_projects':projects
    })


@login_required
def add_project(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        description=request.POST.get('description','')
        if name:
            print(description)
            project=Project.objects.create(name=name,description=description,created_by=request.user)
            return redirect('/projects')
        else:
            print('Not Valid')
    else:
        print("not entered")

    return render(request,'project/add.html')




@login_required
def delete_project(request,project_id):
    project=get_object_or_404(Project,id=project_id)

    project.delete()

    return redirect('/projects/')


@login_required
def project(request,pk):
    project=Project.objects.filter(created_by=request.user).get(pk=pk)

    return render(request,'project/project.html',{
        'project':project
    })

@login_required
def edit_proejct(request,pk):
    project=Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method=='POST':
        name=request.POST.get('name','')
        description=request.POST.get('description','')

        if name:
            project.name=name
            project.description=description
            project.save()

            return redirect('/projects/')
    
    return render(request,'project/edit.html',{
        'project':project
    })