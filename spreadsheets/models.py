from __future__ import unicode_literals
import xlrd

from django.db import models
from django.core.urlresolvers import reverse_lazy

from .utils import ExcelSpreadsheet


class DataSet(models.Model):
    '''
    A collection of Spreadsheets.
    '''
    name = models.CharField(max_length=255)

    def __repr__(self):
        return '<DataSet: {name}>'.format(name=self.name)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('dataset-detail', args=[self.pk])


class Spreadsheet(models.Model):
    '''
    Just an uploaded XLSX file.
    '''
    _file = models.FileField(upload_to='documents/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)
    dataset = models.ForeignKey(DataSet, blank=True, null=True)

    def __repr__(self):
        return '<Spreadsheet: {filename}>'.format(filename=self.filename)

    def __unicode__(self):
        return self.filename

    def get_absolute_url(self):
        return reverse_lazy('dataset-detail', args=[self.pk])

    @property
    def filename(self):
        return self._file.name.split('/')[-1]

    @property
    def get_spreadsheet(self):
        spreadsheet = ExcelSpreadsheet(self.name, self._file.read())
        self._file.seek(0)
        return spreadsheet