"""
View configuration for home app
"""
from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import redirect
from django.views.generic import TemplateView

from home.forms import SearchForm
from products.models import Manufacturer


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        kwargs['searchForm'] = SearchForm()
        kwargs['manufacturers'] = Manufacturer.objects.all()

        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))


class SearchView(TemplateView):
    template_name = 'home/search_results.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
