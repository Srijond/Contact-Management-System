from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_data),
    path('add/',views.add_contact),
    path('update/<str:pk>/',views.update_contact),
    path('delete/<str:pk>/',views.delete_contact),
    
]