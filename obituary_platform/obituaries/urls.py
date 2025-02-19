from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('obituaries/', views.view_obituaries, name='view_obituaries'),
    path('landing/', views.landing_page, name='landing_page'),
    path('confirmation/', views.confirmation, name='confirmation'),  # Add this line
]
