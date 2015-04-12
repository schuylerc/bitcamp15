from django.views.generic import CreateView, DetailView, DeleteView, ListView,\
    UpdateView
from .models import Dwelling, DwellingSerializer
from review.models import Review
from rest_framework import viewsets


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
        context['reviews'] = Review.objects.all()
        context['totalRating'] = Dwelling.objects.calculateRating(context['reviews'])
        return context

class DwellingViewSet(viewsets.ModelViewSet):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer