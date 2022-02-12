from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

class TasksListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetrievView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk' # this is default.
    
class TaskDestroyView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'title'
    
class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
        
class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    

