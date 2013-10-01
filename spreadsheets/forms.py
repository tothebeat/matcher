from django import forms
from .models import Spreadsheet, DataSet

class SpreadsheetForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet
        exclude = ['number_of_rows', 'number_of_columns']

class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
