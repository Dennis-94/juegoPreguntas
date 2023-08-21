from django.urls import path, include

from . import views

urlpatterns = [    
    path('tab/',views.tablas,name="tab")
]