from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_employee, name='delete_employee')
]
