from django.shortcuts import render

def calc(request, a, b):
    return HttpResponse("{}+{}={}".format(a, b, a+b))