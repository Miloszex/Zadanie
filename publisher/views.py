# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from publisher.models import Publisher
from publisher.serializers import PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.filter()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializer_class = PublisherSerializer
