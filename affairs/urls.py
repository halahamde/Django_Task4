from unicodedata import name
from django.urls import path

from affairs.views import *

app_name = 'affairs'

urlpatterns = [
    path('home', home ),
    path('genericlist', myuserList.as_view(), name='genericlist'),
    path('tracklist', trackList.as_view(), name='tracklist'),
    path('addusertoadmin', addusertoadmin),
    path('loginusertoadmin', loginusertoadmin),
    path('logout', mylogout),
    path('add', addStudent ),
    path('update', updateStudent.as_view()),
    path('delete', deleteStudent ),
    path('select', selectAll),
    path('search', search )
]