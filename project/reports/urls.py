from django.urls import path,include
from . import views
from django.conf import settings
app_name='Report'
urlpatterns = [
    path('list/',views.report_list,name='report_list'),
    path('insert/',views.report_insert,name='report_insert'),
    path('delete/',views.staff_delete,name='report_delete'),
]

