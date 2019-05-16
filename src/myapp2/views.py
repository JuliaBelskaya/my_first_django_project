from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. (бизнес логика)


def cw18_1(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        cons_amount = 0
        vowels_amount = 0
        for letter in comment:
            if letter in 'aeyuoi':
                vowels_amount += 1
            elif letter in 'qwrtpsdfghjklzxcvbnm':
                cons_amount += 1
        len_comment = len(comment)
        result = f'amount of vowels is {vowels_amount}, amount of cons is {cons_amount}, len of comment is {len_comment}'
        return HttpResponse(result)

    return HttpResponse('It is GET request')


def cw18_2(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        comm = comment.split('.')
        result = f'{comm} (c) {name}'
        return HttpResponse(result)
    return HttpResponse('It is GET request')

