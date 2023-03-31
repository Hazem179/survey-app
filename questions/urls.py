from django.urls import path
from . import views
urlpatterns = [
path('home/', views.home, name='home'),
    path('add_question/', views.add_question, name='add_question'),
path('get_question/', views.get_question, name='get_question'),
]
