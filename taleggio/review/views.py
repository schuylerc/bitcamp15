from django.shortcuts import render

# Create your views here.
def reviewDetail(request, review_id):
	#this shows an individual dwellings based on the id
	return render(request, 'reviewDetail.html', {'user': request.user})


def reviews(request):
	#should show a list of all available dwellings
	return render(request, 'reviews.html', {'user': request.user})