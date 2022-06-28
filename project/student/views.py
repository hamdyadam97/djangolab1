from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def student_list(request):
     return HttpResponse("viewLsit")

def student_insert(request):
     return render(request,'student/insert.html')

def student_delete(request):
     return HttpResponseRedirect('/')

def student_update(request):
     return  render(request,'student/update.html')