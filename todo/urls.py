from django.urls import path, include
from . import views


urlpatterns=[
    path('addTask/', views.addTask, name='addTask'), 
    #Mark as Done
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    #Editing Task
    path('edit_task/<int:pk>/',views.edit_task, name="edit_task"),
    #Delete Task
    path('delete_task/<int:pk>/',views.delete_task, name="delete_task"),
    #Mark as Undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name="mark_as_undone"),
]  