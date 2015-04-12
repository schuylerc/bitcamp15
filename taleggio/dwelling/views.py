from django.views.generic import CreateView, DetailView, DeleteView, ListView,\
    UpdateView
from .models import Dwelling, DwellingSerializer
from review.models import DwellingReview
from dwelling.models import Dwelling
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.db.models import Q
import random

@csrf_exempt
def search(request):
    searchQuery = request.POST.get('searchQuery')
    template_name = 'dwellings.html'
    if searchQuery != None:
        queryset = Dwelling.objects.filter(Q(address__number__contains=searchQuery) | Q(address__street__contains=searchQuery) | Q(address__city__contains=searchQuery) | Q(address__state__contains=searchQuery) | Q(address__zipcode__contains=searchQuery))
        
        context = {'object_list': queryset}

        return render_to_response(template_name, context)
    else:
        queryset = Dwelling.objects.all()
        context = {'object_list': queryset}
        return render_to_response(template_name, context)

class DwellingCreate(CreateView):
    model = Dwelling

class DwellingUpdate(UpdateView):
    model = Dwelling
    template_name = 'dwelling_update.html'

class DwellingList(ListView):
    model = Dwelling
    template_name = 'dwellings.html'

class DwellingDelete(DeleteView):
    model = Dwelling

class DwellingView(DetailView):
    model = Dwelling
    template_name = 'dwelling_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DwellingView, self).get_context_data(**kwargs)
        context['reviews'] = DwellingReview.objects.all()
        context['crime'] = random.randint(30,80)
        context['totalRating'] = Dwelling.objects.calculateRating(context['reviews'])
        return context

class DwellingViewSet(viewsets.ModelViewSet):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer