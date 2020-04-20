from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, pk):
    passenger = int(request.POST.get('passenger'))
    id = pk

    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = int(cart[id])+passenger
    else:
        cart[id] = cart.get(id, passenger)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, pk):
    passenger = int(request.POST.get('passenger'))
    id = pk

    cart = request.session.get('cart', {})

    if passenger > 0:
        cart[id] = passenger
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
