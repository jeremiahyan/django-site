from django.conf.urls import include, url

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


app_name = 'snippets'

schema_view = get_schema_view(title='Passion API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
    'get': 'list',
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})


# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     # url(r'^$', views.api_root),
#     url(r'^$', snippet_list, name='snippet-list'),
#     url(r'^(?P<pk>[0-9]+)/?$', snippet_detail, name='snippet-detail'),
#     url(r'^(?P<pk>[0-9]+)/highlight/?$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
#
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
]
