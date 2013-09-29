from django.conf.urls import patterns, include, url

from .views import DataSetList, SpreadsheetList

urlpatterns = patterns('',
    url(r'^$', SpreadsheetList.as_view()),
)
