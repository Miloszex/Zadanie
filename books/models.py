# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=75, unique=True)
    pages_num = models.PositiveIntegerField()
    cover_image = models.ImageField()
    publisher = models.ForeignKey('publisher.Publisher', null=True,
                                  on_delete=models.SET_NULL)
    authors = models.ManyToManyField('author.Author', related_name='books')

    def __str__(self):
        return f'{self.title}'
