from django.conf.urls import re_path
from secondApp import views

#template tagging
app_name='secondApp'

urlpatterns=[
re_path(r'^register/$',views.register,name='register'),
re_path(r'^user_login/$',views.user_login,name='user_login'),
]
