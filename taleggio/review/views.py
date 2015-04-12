from django.shortcuts import render
from django.views.generic import ListView
from review.models import DwellingReview

# Create your views here.
def reviewDetail(request, review_id):
	#this shows an individual dwellings based on the id
	return render(request, 'reviewDetail.html', {'user': request.user})


class ReviewList(ListView):
    model = DwellingReview
    template_name = 'reviews.html'
