from django.urls import path
from .views import AuthorListCreateView, CategoryListCreateView, BookListCreateView, BookDetailView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
