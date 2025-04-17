from django.urls import path, include
from library import views
urlpatterns = [
    path('', views.home),
    path('save/', views.home),

    #Request, URL
    path('search/', views.search),
]
