from django.urls import path
from . import views

urlpatterns = [
    # path('',views.apiOverview),
    path("", views.taskList, name="tasklist"),
    path("task-detail/<str:pk>/", views.taskOne, name="taskone"),
    path("task-create/", views.taskCreate, name="taskcreate"),
    path("task-update/<str:pk>/", views.taskUpdate, name="taskupdate"),
    path("task-delete/<str:pk>/", views.taskDelete, name="taskdelete"),
    ]