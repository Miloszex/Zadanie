from rest_framework.serializers import ModelSerializer

from publisher.models import Publisher


class PublisherSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Publisher
