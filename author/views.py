# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from author.models import Author
from author.serializers import AuthorSerializer, AuthorDetailsSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.filter()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filterset_fields = ['nickname']
    SERIALIZERS_MAP = {
        'retrieve': AuthorDetailsSerializer
    }

    def get_serializer_class(self):
        return self.SERIALIZERS_MAP.get(self.action, AuthorSerializer)
