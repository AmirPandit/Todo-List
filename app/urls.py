from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name ='create'),
    path('record', views.view, name='view'),
    path('record/<int:id>', views.viewdetail, name='viewdetail'),
    path('record/<int:id>/edit', views.edit, name='edit'),
    path('record/<int:id>/delete', views.delet, name='delete'),
]