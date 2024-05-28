from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    return render(request, 'cart.html', {'order': order})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart')

@login_required
def checkout(request):
    order = get_object_or_404(Order, user=request.user, is_ordered=False)
    if request.method == 'POST':
        # Process payment here
        order.is_ordered = True
        order.save()
        return redirect('home')
    return render(request, 'checkout.html', {'order': order})from django.shortcuts import render

# Create your views here.
