from django import forms
from .models import Spreadsheet, DataSet

class SpreadsheetForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet

class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
