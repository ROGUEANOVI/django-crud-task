from django.urls import path
from myapp import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hello/<str:username>', views.hello, name='hello'),
  path('projects/list-projects', views.projects, name='list_projects'),
  path('project/<int:id>', views.project, name='project'),
  path('projects/create-project', views.create_project, name='create_project'),
  path('tasks/list-tasks', views.tasks, name='list_tasks'),
  path('task/<str:title>', views.task, name='task'),
  path('tasks/create-task', views.create_task, name='create_task'),
]