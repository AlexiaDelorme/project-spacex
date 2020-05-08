from django.shortcuts import get_object_or_404
from trips.models import Trip


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    trip_count = 0

    for id, passenger in cart.items():
        trip = get_object_or_404(Trip, pk=id)
        sub_total = passenger * trip.category.price
        total += sub_total
        passenger_range = range(passenger)
        trip_count += passenger
        cart_items.append({
            'id': id,
            'trip': trip,
            'passenger': passenger,
            'passenger_id': [],
            'passenger_range': passenger_range,
            'sub_total': sub_total
        })
    
    return {
        'cart_items': cart_items,
        'total': total,
        'trip_count': trip_count,
        'per_id_count': len(cart_items)
    }
