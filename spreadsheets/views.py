from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from .models import DataSet, Spreadsheet
from .forms import SpreadsheetForm, DataSetForm
from .utils import ExcelSpreadsheet


class SpreadsheetList(ListView):
    model = Spreadsheet

class SpreadsheetDetail(DetailView):
    model = Spreadsheet

    def get_context_data(self, **kwargs):
        context = {}
        spreadsheet = self.object.get_spreadsheet    
        context['header_row'] = spreadsheet.header_row
        context['data_rows'] = spreadsheet.data
        context.update(kwargs)
        return super(SpreadsheetDetail, self).get_context_data(**context)

class SpreadsheetCreate(CreateView):
    form_class = SpreadsheetForm
    model = Spreadsheet
    success_url = reverse_lazy('spreadsheet-list')

class DataSetList(ListView):
    model = DataSet

class DataSetDetail(DetailView):
    model = DataSet

class DataSetCreate(CreateView):
    form_class = DataSetForm
    model = DataSet
    success_url = reverse_lazy('dataset-list')
