from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. (бизнес логика)


def index1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse('len is {}'.format(len(name)))
    return HttpResponse('It is GET request')


def index2(request):
    age = request.POST.get('age')
    if int(age) < 18:
        return HttpResponse('В доступе отказано')
    else:
        return HttpResponse('Добро пожаловать')


