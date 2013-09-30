from django.conf.urls import patterns, include, url
from django.contrib import admin

from spreadsheets.views import (
        DataSetList,
        DataSetCreate,
        DataSetDetail,
        SpreadsheetList,
        SpreadsheetCreate,
        SpreadsheetDetail,
        )

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^spreadsheets/$', SpreadsheetList.as_view(), name='spreadsheet-list'),
    url(r'^spreadsheets/add/$', SpreadsheetCreate.as_view(), name='spreadsheet-create'),
    url(r'^spreadsheets/(?P<pk>[\d]+)/$', SpreadsheetDetail.as_view(), name='spreadsheet-detail'),
    url(r'^datasets/$', DataSetList.as_view(), name='dataset-list'),
    url(r'^datasets/add/$', DataSetCreate.as_view(), name='dataset-create'),
    url(r'^datasets/(?P<pk>[\d]+)/$', DataSetDetail.as_view(), name='dataset-detail'),
)
