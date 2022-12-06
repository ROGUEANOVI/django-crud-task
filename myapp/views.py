from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreatenewProject

# Create your views here.
def home(request):
  return render(request,"home.html")

def hello(request, username):
  return render(request, "hello.html", {"usernamecontext": username})

def about(request):
  return render(request, "about.html")

def projects(request):
  projects = Project.objects.all()
  return render(request, "projects/projects.html", {"projects": projects})

def project(request, id):
  #task = Task.objects.get(id=id)
  project = get_object_or_404(Project, id=id)
  return JsonResponse({"id": project.id, "name": project.name}, safe=False)

def create_project(request):
  if request.method == "GET":
    return render(request, "projects/create_project.html", {"forms": CreatenewProject()})
  else:
    Project.objects.create(name=request.POST["name"])
    return redirect("list-projects")

def tasks(request):
  tasks = Task.objects.all()
  return render(request, "tasks/tasks.html", {"tasks": tasks})

def task(request, title):
  #task = Task.objects.get(id=id)
  task = get_object_or_404(Task, title=title)
  return JsonResponse({"title": task.title, "Description": task.description, "id": task.project_id}, safe=False)

def create_task(request):
  if request.method == "GET":
    return render(request, "tasks/create_task.html", {"forms": CreateNewTask()})
  else:
    Task.objects.create(title=request.POST["title"], description=request.POST["description"], project_id= 1)
    return redirect("list-tasks")
    