from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """Render the cart content page"""

    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add passenger(s) for a specified trip to the cart"""

    passenger = int(request.POST.get('passenger'))
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id])+passenger
    else:
        cart[id] = cart.get(id, passenger)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """Ajust passenger number for a specified trip"""

    passenger = int(request.POST.get('passenger'))
    cart = request.session.get('cart', {})

    if passenger > 0:
        cart[id] = passenger
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """Remove a specified trip from the cart"""

    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
