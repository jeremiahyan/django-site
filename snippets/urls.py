from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


app_name = 'snippets'

urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^(?P<pk>[0-9]+)/?$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
