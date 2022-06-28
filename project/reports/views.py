from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.

def report_list(request):
     return HttpResponse("viewLsit")

def report_insert(request):
     return HttpResponse("report")

def staff_delete(request):
     name='hamdy adam'
     context = {
          'name':name
                }
     return render(request,'report/link.html',context)

