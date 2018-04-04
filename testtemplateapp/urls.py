from django.urls import path
from testtemplateapp import views

app_name = 'test'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name = 'about')
]