from django.urls import path
from all_apps.users.views import *

urlpatterns=[
    path('',home,name="home"),
]