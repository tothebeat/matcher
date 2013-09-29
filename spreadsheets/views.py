from django.views.generic import ListView
from .models import DataSet, Spreadsheet

def index(request):
    return 

class SpreadsheetList(ListView):
    model = Spreadsheet

class DataSetList(ListView):
    model = DataSet
