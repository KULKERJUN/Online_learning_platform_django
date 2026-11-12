from django.urls import path
from authentication_app.views import *

urlpatterns = [
    path('',login_view,name='login_view'),
    path('register/',register_view,name='register_view')
]