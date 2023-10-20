from django.urls import path, include
from rest_framework import routers

from .views import AuthorViewset, CategoryViewset, BookViewset

router = routers.DefaultRouter()

router.register('authors', AuthorViewset)
router.register('categories', CategoryViewset)
router.register('books', BookViewset)

urlpatterns = [
    path('', include(router.urls)),
]
