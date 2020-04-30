import pytest

from books.tests.factories import BookFactory


@pytest.mark.django_db
class TestBookModel:

    def test_str(self):
        book = BookFactory()
        assert str(book) == book.title
