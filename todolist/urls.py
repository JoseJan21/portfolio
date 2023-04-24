from django.urls import path
from . import views



urlpatterns = [
    path('', views.list_routines, name='todolist'),
    path('insert/', views.insert_tarea, name='insert_tarea'),
    path('update/', views.update, name='update'),
    path('delete/<int:tarea_id>', views.delete, name='delete'),
    path('update/<int:tarea_id>', views.update_form, name='update_form'),
    path('create_routine/', views.create_routine, name='create_routine'),
    path('register/', views.register_todolist, name='register_todolist'),
    path('login/', views.login_todolist, name='login_todolist'),
    path('logout/', views.logout_todolist, name='logout_todolist'),
    path('tasks/', views.page, name='tasks'),
]