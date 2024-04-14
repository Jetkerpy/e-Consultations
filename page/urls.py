from django.urls import path

from . import views

app_name = "page"


urlpatterns = [
    path('', views.home, name="home"),
    path('aptekar/', views.apte_kar, name="aptekar"),
    path('what/', views.view_more, name="view_more"),
    
]