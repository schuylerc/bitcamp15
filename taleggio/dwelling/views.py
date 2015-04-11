from django.shortcuts import render

# Create your views here.
def dwellingDetail(request, dwelling_id):
	#this shows an individual dwellings based on the id
	return render(request, 'dwellingDetail.html', {'user': request.user})


def dwellings(request):
	#should show a list of all available dwellings
	return render(request, 'dwellings.html', {'user': request.user})