from django.views.generic import CreateView, DetailView, DeleteView, ListView,\
    UpdateView
from .models import Dwelling


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
    template_name = 'dwellingDetail.html'
