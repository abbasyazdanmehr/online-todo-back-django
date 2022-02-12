from django.urls import path

from todoapp.views import TaskCreateView, TaskDestroyView, TaskRetrievView, TaskUpdateView, TasksListView, UsersListView

app_name = 'todoapp'

urlpatterns = [
    path('', TasksListView.as_view(), name='taskslist'),
    path('<int:pk>/', TaskRetrievView.as_view(), name='taskretrieve'),
    path('tasknew', TaskCreateView.as_view(), name='taskcreate'),
    path('tasknew', TaskUpdateView.as_view(), name='taskupdate'),
    path('taskdestroy/<str:title>/', TaskDestroyView.as_view(), name='taskdestroy'),
    path('users/', UsersListView.as_view(), name='users'),
]
