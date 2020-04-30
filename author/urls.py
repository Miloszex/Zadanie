from rest_framework import routers

from author.views import AuthorViewSet

router = routers.SimpleRouter()
router.register('author', AuthorViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
