"""
inventory views
"""
from django.contrib import messages
from django.views.generic import TemplateView, ListView

from products.models import Product


class ProductView(TemplateView):
    template_name = 'products/listings.html'

    def get_context_data(self, **kwargs):
        kwargs['discs'] = Product.objects.all()
        kwargs['disc_manufacturer'] = 'All Discs Available'
        return super().get_context_data(**kwargs)


class ManufacturerView(TemplateView):
    template_name = 'products/listings.html'

    def get_context_data(self, **kwargs):
        kwargs['disc_manufacturer'] = self.kwargs['manufacturer']
        kwargs['discs'] = Product.objects.filter(
                                    manufacturer=self.kwargs['manufacturer'])
        return super().get_context_data(**kwargs)


class DetailsView(TemplateView):
    template_name = 'products/details.html'

    def get_context_data(self, **kwargs):
        kwargs['disc_name'] = self.kwargs['disc']
        kwargs['disc_manufacturer'] = self.kwargs['manufacturer']
        kwargs['discs'] = Product.objects.filter(manufacturer__manufacturer_name=self.kwargs['manufacturer'],
                                                disc=self.kwargs['disc'])
        return super().get_context_data(**kwargs)


    #def get(self, request, *arg,**kwargs):
    #    return self.render_to_response(self.get_context_data(**kwargs))
