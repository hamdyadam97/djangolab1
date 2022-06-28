from django.urls import path,include
from . import views
from django.conf import settings
app_name='Staff'
urlpatterns = [
    path('list/',views.staff_list,name='student_list'),
    path('insert/',views.staff_insert,name='student_insert'),
    path('delete/',views.staff_delete,name='student_delete'),
]

