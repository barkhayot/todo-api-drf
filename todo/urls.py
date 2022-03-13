from django.urls import path
from .views import ListCreateTodoAPIView, RetrieveUpdateDestroyTodoAPIView

urlpatterns = [
    path('', ListCreateTodoAPIView.as_view(), name='todos'),
    path('<int:id>', RetrieveUpdateDestroyTodoAPIView.as_view(), name='control')
]