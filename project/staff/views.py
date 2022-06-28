from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.

def staff_list(request):
     return HttpResponse("viewLsit")

def staff_insert(request):
     return JsonResponse({'name': 'Ahmed'})

def staff_delete(request):
     return HttpResponseRedirect('/staff/list')

