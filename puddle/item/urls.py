from django.urls import path
from .views import readMore,new,delete,edit,browse

app_name = "item"
urlpatterns = [
    path('new/',new,name='new'),
    path('<int:pk>/',readMore,name='readMore'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('browse/',browse,name='browse')
]
