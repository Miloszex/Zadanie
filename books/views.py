# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from author.models import Author
from books.models import Book
from books.serializers import (
    BookCreateSerializer,
    BookDetailsSerializer,
    BookListSerializer
)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.filter()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializers_strategy = {
        'retrieve': BookDetailsSerializer,
        'list': BookListSerializer
    }

    def get_serializer_class(self):
        return self.serializers_strategy.get(self.action,
                                             BookCreateSerializer)

