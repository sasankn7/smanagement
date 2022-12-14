from django.urls import path
from .views import Indeview,CreateCourse,UpdateView,DeleteView,StudentView,InstratorView
app_name='course'

urlpatterns = [
    path('',Indeview,name='index'),
    path('create/',CreateCourse,name='add'),
    path('update/<int:pk>/',UpdateView,name='update'),
    path('delete/<int:pk>/',DeleteView,name='delete'),
    path('student/',StudentView,name='student'),
    path('instractor/',InstratorView,name='instractor')
]