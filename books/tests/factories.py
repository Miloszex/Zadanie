from factory.django import DjangoModelFactory
import factory.fuzzy

from books.models import Book
from publisher.tests.factories import PublisherFactory


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=20)
    pages_num = factory.fuzzy.FuzzyInteger(low=1)
    cover_image = factory.django.ImageField(filename='img')
    publisher = factory.SubFactory(PublisherFactory)

    class Meta:
        model = Book
