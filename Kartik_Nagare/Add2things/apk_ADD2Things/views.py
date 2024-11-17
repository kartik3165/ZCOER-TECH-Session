from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def result(request):
    return render(request,'result.html')

def add(request):
    return render(request,'add.html')

def addnumber(request):
    num1 = int(request.GET['input1'])
    num2 = int(request.GET['input2'])
    total = num1 + num2
    return render(request, 'add.html' , { 'add_results' : total })

def div(request):
    return render(request,'div.html')

def divnumber(request):
    num1 = int(request.GET['input1'])
    num2 = int(request.GET['input2'])
    total = num1 / num2
    return render(request, 'div.html' , { 'div_results' : total })

def multi(request):
    return render(request,'multi.html')

def multinumber(request):
    num1 = int(request.GET['input1'])
    num2 = int(request.GET['input2'])
    total = num1 * num2
    return render(request, 'multi.html' , { 'multi_results' : total })

def sub(request):
    return render(request,'sub.html')

def subnumber(request):
    num1 = int(request.GET['input1'])
    num2 = int(request.GET['input2'])
    total = num1 - num2
    return render(request, 'sub.html' , { 'sub_results' : total })