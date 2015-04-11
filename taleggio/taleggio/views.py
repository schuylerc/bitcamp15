from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'user': request.user})


def auth_test(request):
    return render(request, 'auth_test.html', {'user': request.user})


def dwellings(request):
	#should show a list of all available dwellings
	return render(request, 'dwellings.html', {'user': request.user})