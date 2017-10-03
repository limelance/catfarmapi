from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CatViewSet


cat_list = CatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

cat_detail = CatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cats/$', cat_list, name='cat-list'),
    url(r'^cats/(?P<pk>[0-9]+)/$', cat_detail, name='cat-detail'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
