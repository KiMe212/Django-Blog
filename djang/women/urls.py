from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('abouts/', about, name='about'),
    path('posts/', posts)

]
