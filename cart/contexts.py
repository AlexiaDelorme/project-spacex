from django.shortcuts import get_object_or_404
from trips.models import Trip


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    trip_count = 0

    for id, passenger in cart.items():
        trip = get_object_or_404(Trip, pk=id)
        total += passenger * trip.category.price
        trip_count += passenger
        cart_items.append({'id': id, 'passenger': passenger, 'trip': trip})

    return {
        'cart_items': cart_items,
        'total': total,
        'trip_count': trip_count
    }
