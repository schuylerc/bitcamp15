from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def dwelling(request):
	return render(request, 'dwelling.html')

