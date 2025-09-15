from django.urls import path
from apps.base.views import AuthorLIstView, AuthorDetailView

urlpatterns = [
    path("", AuthorLIstView.as_view(), name='author'),
    path("authors/<int:pk>", AuthorDetailView.as_view(), name='author-detail')
]
