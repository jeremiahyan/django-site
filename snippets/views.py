from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetHyperSerializer, UserHyperSerializer
from snippets.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


# Create your views here.
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserHyperSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserHyperSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserHyperSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetHyperSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @api_view(['GET', 'POST'])
# class SnippetList(APIView):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetHyperSerializer(snippet, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         data = JSONParser().parse(request)
#         serializer = SnippetHyperSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetGenericList(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class SnippetGenericList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetHyperSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)


# @api_view(['GET', 'POST', 'DELETE'])
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetHyperSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetHyperSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetGenericDetail(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class SnippetGenericDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetHyperSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
