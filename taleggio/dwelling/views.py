from django.shortcuts import render

# Create your views here.
def dwellingDetail(request, dwelling_id):
	#this shows an individual dwellings based on the id
	return render(request, 'dwellingDetail.html', {'user': request.user})