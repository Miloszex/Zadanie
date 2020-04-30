from factory.django import DjangoModelFactory
import factory.fuzzy
import datetime
from author.models import Author


class AuthorFactory(DjangoModelFactory):
    first_name = factory.fuzzy.FuzzyText(length=10)
    last_name = factory.fuzzy.FuzzyText(length=10)
    nickname = factory.fuzzy.FuzzyText(length=10)
    birth_date = factory.fuzzy.FuzzyDate(start_date=datetime.date(2000, 1, 1))

    class Meta:
        model = Author