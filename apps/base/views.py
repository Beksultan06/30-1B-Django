from django.shortcuts import render
from apps.base.models import Author
from django.views.generic import ListView, DetailView


class AuthorLIstView(ListView):
    model = Author
    template_name = "author-list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author-detail.html"
    context_object_name = "author"