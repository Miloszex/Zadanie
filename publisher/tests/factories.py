from factory.django import DjangoModelFactory
import factory.fuzzy

from publisher.models import Publisher


class PublisherFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=10)

    class Meta:
        model = Publisher
