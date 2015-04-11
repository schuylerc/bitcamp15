from django.views.generic import CreateView, DetailView, DeleteView, ListView,\
    UpdateView
from dwellings.models import Dwelling


class DwellingCreate(CreateView):
    model = Dwelling


class DwellingUpdate(UpdateView):
    model = Dwelling


class DwellingList(ListView):
    model = Dwelling


class DwellingDelete(DeleteView):
    model = Dwelling


class DwellingView(DetailView):
    model = Dwelling
