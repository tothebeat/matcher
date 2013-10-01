from __future__ import unicode_literals
import xlrd

class ExcelSpreadsheet(object):

	def __init__(self, name, file_contents, *args, **kwargs):
		self.name = name
		self.workbook = xlrd.open_workbook(file_contents=file_contents)
		self.worksheet = self.workbook.sheet_by_index(0)
		self.number_of_rows = self.worksheet.nrows
		self.number_of_columns = self.worksheet.ncols

	def __repr__(self):
		return '<ExcelSpreadsheet: {name}>'.format(name=self.name)

	def __unicode__(self):
		return self.name

	def _values(self, cells):
		return map(lambda cell: cell.value, cells)

	def row(self, row_number):
		return self._values(self.worksheet.row(row_number))

	def column(self, column_number):
		return self._values(self.worksheet.col(column_number))

	@property
	def header_row(self):
		return self.row(0)

	def row_as_dict(self, row_number):
		return dict(zip(self.header_row, self.row(row_number)))

	@property
	def data(self, include_header_row=False):
		start_row = 1
		if include_header_row:
			start_row = 0
		return [self.row(row_number) 
			for row_number in xrange(start_row, self.number_of_rows)]

	@property
	def data_as_dicts(self):
		return [self.row_as_dict(row_number) 
			for row_number in xrange(1, self.number_of_rows)]
