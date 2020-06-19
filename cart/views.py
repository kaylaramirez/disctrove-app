from django.shortcuts import render
from django.views.generic import TemplateView
from cart.models import Cart


# Create your views here.
class CartView(TemplateView):
    template_name = 'cart/overview.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            card_id = request.session['cart_id']
        except KeyError:
            cart = Cart.objects.create()
            request.session['cart_id'] = card_id = cart.pk

        kwargs['cart'] = card_id
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['cart_message'] = 'This is your cart overview.'
        return super().get_context_data(**kwargs)

    #def get(self):

    #def post(self, request, **kwargs):
    #    try:
    #        request.session.get('cart_id')
    #    except KeyError:
    #        request.session['cart_id'] = 1
        # check session data

