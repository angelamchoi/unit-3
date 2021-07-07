from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_widget, name='add_widget'),
    path('<int:widget_id>/delete', views.delete_widget, name='delete_widget'),
]