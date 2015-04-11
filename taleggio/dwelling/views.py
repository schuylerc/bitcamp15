from django.shortcuts import render

# Create your views here.
def dwellingDetail(request):
	#this shows an individual dwellings based on the id
	return render(request, 'dwelling.html', {'user': request.user})