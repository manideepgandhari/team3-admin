from django.urls import path
from . import views

app_name='paper'
urlpatterns=[
path('',views.home,name='home'),
path('login/',views.login,name='login'),
path('accept/',views.accept,name='accept'),
path('uploadpaper/',views.uploadpaper,name='uploadpaper'),
path('timetable/',views.timetable,name='timetable'),
path('check_user_upload/',views.check_user_upload,name='check_user_upload'),
path('getrequestnoinfo/',views.getrequestnoinfo,name='getrequestnoinfo'),
path('sendrequestinfo/',views.sendrequestinfo,name='sendrequestinfo'),
]
