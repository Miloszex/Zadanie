from rest_framework import routers

from publisher.views import PublisherViewSet

router = routers.SimpleRouter()
router.register('publisher', PublisherViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
