from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author
from .serializer import AuthorSerializer
from rest_framework import status


# Create your views here.


@api_view()
def list_authors(request):
    authors = Author.objects.all()
    serializers = AuthorSerializer(authors, many=True)
    return Response(serializers.data, status.HTTP_200_OK)


@api_view()
def author_detail(request, pk):
    # author = get_object_or_404()
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OKy)


def welcome(request):
    return HttpResponse('ok')


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'book/author-list.html', {'authors': authors})
