from rest_framework import serializers
from author.serializers import AuthorSerializer
from books.models import Book


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailsSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_authors(self, obj):
        return [f'{item.first_name} {item.last_name}' for item in obj.authors.all()]


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'cover_image')

