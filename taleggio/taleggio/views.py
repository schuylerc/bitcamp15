from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def auth_test(request):
    return render(request, 'auth_test.html')
