from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CartAddForm
from home.models import Product
from .cart import Cart

# Create your views here.

class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html' , {'cart': cart})

class CartAddView(View):
    def post(self , request , product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'])
        return redirect('orders:cart')