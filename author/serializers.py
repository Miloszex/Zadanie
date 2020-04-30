from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Author


class AuthorDetailsSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Author

    def get_books(self, obj):
        return [item.title for item in obj.books.all()]


