from rest_framework import routers

from book.views import BookViewSet

from django.urls import path, include

router = routers.DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "books"
