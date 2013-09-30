from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from .models import DataSet, Spreadsheet
from .forms import SpreadsheetForm, DataSetForm


class SpreadsheetList(ListView):
    model = Spreadsheet

class DataSetList(ListView):
    model = DataSet

class SpreadsheetDetail(DetailView):
    model = Spreadsheet

class DataSetDetail(DetailView):
    model = DataSet

class SpreadsheetCreate(CreateView):
    form_class = SpreadsheetForm
    model = Spreadsheet
    success_url = reverse_lazy('spreadsheet-list')

class DataSetCreate(CreateView):
    form_class = DataSetForm
    model = DataSet    
