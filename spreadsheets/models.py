from __future__ import unicode_literals
import xlrd

from django.db import models
from django.core.urlresolvers import reverse_lazy


class DataSet(models.Model):

    name = models.CharField(max_length=255)

    def __repr__(self):
        return '<DataSet: {name}>'.format(name=self.name)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('dataset-detail', args=[self.pk]) 

class Spreadsheet(models.Model):

    _file = models.FileField(upload_to='documents/%Y/%m/%d/')
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    dataset = models.ForeignKey(DataSet, null=True)

    def __repr__(self):
        return '<Spreadsheet: {filename}'.format(filename=self._file)

    def __unicode__(self):
        return self.name

    def number_of_rows(self):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        number_of_rows = worksheet.nrows
        return number_of_rows

    def number_of_rows(self):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        number_of_columns = worksheet.ncols
        return number_of_columns

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

    def data(self):
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        data = [[worksheet.cell(row_index, col_index).value
            for col_index in xrange(worksheet.ncols)] 
            for row_index in xrange(worksheet.nrows)]
        return data

    def data_as_dicts(self):
        '''
        Assuming the first row in the data is the label/header row, and
        every subsequent row can be considered a data row.
        '''
        workbook = xlrd.open_workbook(file_contents=self._file.read())
        self._file.seek(0)
        worksheet = workbook.sheet_by_index(0)
        header_row = map(lambda cell: cell.value, worksheet.row(0))
        data = []
        for row_index in xrange(1, worksheet.nrows):
            record = dict(zip(header_row, map(lambda cell: cell.value, worksheet.row(row_index))))
            data.append(record)
        return data

    def get_absolute_url(self):
        return reverse_lazy('dataset-detail', args=[self.pk]) 

