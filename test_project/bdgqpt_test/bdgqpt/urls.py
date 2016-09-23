# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from bdgqpt import views
app_name = 'bdgqpt'

urlpatterns = [
    # /bdgqpt/
    url(r'^$', views.index, name='index'),
    #/bdgqpt/caozuopiao/
    url(r'^caozuopiao/$', views.caozuopiao_list, name='caozuopiaohomepage'),
    # /bdgqpt/caozuopiao/Add/
    url(r'^caozuopiao/Add/(\w+)/$', views.caozuopiao_create, name='Addcaozuopiao'),
    #/bdgqpt/caozuopiao/2/
    url(r'^caozuopiao/(?P<id>[0-9]+)/$', views.caozuopiao_update, name='Updatecaozuopiao'),
    #name-autocomplete-method
    url(r'^name-autocomplete/$',views.NameAutocomplete.as_view(),name='name-autocomplete'),
]
