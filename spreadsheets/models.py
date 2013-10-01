from __future__ import unicode_literals
import xlrd

from django.db import models
from django.core.urlresolvers import reverse_lazy


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
    At core, an XLSX file. Wrapped with methods to act like
    a terrible, terrible database. No CRUD here. 
    '''
    _file = models.FileField(upload_to='documents/%Y/%m/%d/')
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    dataset = models.ForeignKey(DataSet, null=True)

    def __repr__(self):
        return '<Spreadsheet: {filename}>'.format(filename=self._file)

    def __unicode__(self):
        return self.name

    def number_of_rows(self):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        return worksheet.nrows

    def number_of_rows(self):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        return worksheet.ncols

    def row(self, row_number):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        row = map(lambda cell: cell.value, worksheet.row(row_number))
        return row

    def column(self, column_number):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        column = map(lambda cell: cell.value, worksheet.col(column_number))
        return column

    def header_row(self):
        '''
        Just the values in the first row that act as column headers,
        not any of the data.
        '''
        return self.row(0)

    def data_rows(self):
        '''
        Just the values, not including the header row.
        '''
        return [self.row(n) for n in xrange(1, self.number_of_rows())]

    def data_as_dicts(self):
        '''
        Assuming the first row in the data is the label/header row, and
        every subsequent row can be considered a data row.
        '''
        header_row = self.header_row()
        data_rows = self.data_rows()
        return [dict(zip(header_row, data_row)) for data_row in data_rows]

    def get_absolute_url(self):
        return reverse_lazy('dataset-detail', args=[self.pk])