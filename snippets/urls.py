from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


app_name = 'snippets'

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^$', views.SnippetGenericList.as_view(), name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)/?$', views.SnippetGenericDetail.as_view(), name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/?$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
