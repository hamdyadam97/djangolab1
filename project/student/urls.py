from django.urls import path,include
from . import views
from django.conf import settings
app_name='Student'
urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('insert/',views.student_insert,name='student_insert'),
    path('update/',views.student_update,name='student_update'),
    path('delete/',views.student_delete,name='student_delete'),
]

