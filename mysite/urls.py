from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'home'),
    path('portfolio/', views.portfolio, name= 'portfolio'),
    path('contact/', views.contact, name= 'contact'),
    path('about/',views.about, name = 'about'),
    path('philosophy/', views.philosophy, name='philosophy'),
    path('onwork/', views.onwork, name='onwork'),
    path('mlmodel/', views.mlmodel, name='mlmodel'),
]