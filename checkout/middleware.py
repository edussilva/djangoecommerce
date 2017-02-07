# coding: utf-8
from .models import CartItem


def cart_item_moddleware(get_response):

    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key:
            cart_items = CartItem.objects.filter(cart_key=session_key).update(
                cart_key=request.session.session_key
            )
        return response
    return middleware