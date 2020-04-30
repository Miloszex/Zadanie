import io

import pytest
from PIL import Image

from author.tests.factories import AuthorFactory
from books.tests.factories import BookFactory
from publisher.tests.factories import PublisherFactory


@pytest.mark.django_db
class TestBookViewSet:

    def formatted_url(self, object_id=None, action=None):
        url = '/api/v1/book/book/'
        if object_id:
            url = f'{url}{object_id}/'
        if action:
            url = f'{url}{action}/'
        return url

    def test_list_books(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        books = [BookFactory(publisher=publisher) for i in range(3)]
        for book in books:
            book.authors.set(authors)
        response = client.get(self.formatted_url())
        assert response.status_code == 200
        assert len(response.data) == 3
        
    def test_get_book(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        books = [BookFactory(publisher=publisher) for i in range(3)]
        for book in books:
            book.authors.set(authors)
        response = client.get(self.formatted_url(books[0].id))
        assert response.status_code == 200
        assert response.data['title'] == books[0].title
        assert len(response.data['authors']) == 2

    def test_create_book(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        payload = {
            'title': 'Test',
            'pages_num': 300,
            'cover_image': self.generate_photo_file(),
            'publisher': publisher.id,
            'authors': [author.id for author in authors]
        }
        response = client.post(self.formatted_url(), payload)
        assert response.status_code == 201
        assert response.data['title'] == payload['title']

    def test_create_book_failed(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        book = BookFactory(title='Test')
        payload = {
            'title': 'Test',
            'pages_num': 300,
            'cover_image': self.generate_photo_file(),
            'publisher': publisher.id,
            'authors': [author.id for author in authors]
        }
        response = client.post(self.formatted_url(), payload)
        assert response.status_code == 400

    def test_update_book(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        book = BookFactory(title='Test', pages_num=10)
        book.authors.set(authors)
        payload = {
            'title': 'xyz',
            'pages_num': 20
        }
        response = client.patch(self.formatted_url(book.id), data=payload, content_type='application/json')
        import pudb
        pudb.set_trace()
        assert response.status_code == 200
        assert response.data['title'] == 'xyz'

    def test_delete_book(self, client):
        publisher = PublisherFactory()
        authors = [AuthorFactory() for author in range(2)]
        book = BookFactory(publisher=publisher)
        book.authors.set(authors)
        response = client.delete(self.formatted_url(book.id))
        assert response.status_code == 204
        with pytest.raises(BookFactory._meta.model.DoesNotExist):
            book.refresh_from_db()

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

