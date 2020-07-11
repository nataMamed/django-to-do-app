from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('update_task/<int:task_id>', views.update_task_view, name='update_task'),
    path('delete_task/<int:task_id>', views.delete_task_view, name='delete_task')
]
