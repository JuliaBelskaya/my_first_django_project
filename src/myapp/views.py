from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. (бизнес логика)

def index(request):    #вызывается из интернета, принимает запрос
    return HttpResponse('Hello, Cat')


