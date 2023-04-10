from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_question, name='get_question'),
    path('add_question/', views.add_question, name='add_question'),
    path('get_object/<int:id>', views.get_object, name='get_object'),
]
