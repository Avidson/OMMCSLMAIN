from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Product, Review
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from cart.form import CartAddProductForm
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 40) #for paginator to display items on each page
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page_obj = paginator.get_page(paginator.num_pages)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page' : page,
        'page_obj' : page_obj,
    }
    return render(request, 'ecommerce/ecommerce.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    reviews = product.products.filter(active=True, post_id=id)

    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        body = request.POST['comments']

        new_review = Review.objects.get_or_create(
            post = product,
            name = name,
            email = email,
            body = body
        )

        if new_review:
            review_message = messages.info(request, 'Your review has been posted')

    context = {
        'product' : product,
        'cart_product_form' : cart_product_form,
        'reviews' : reviews, 
    }

    return render(request, 'ecommerce/productDetail.html', context=context)


class SearchResultView(ListView):

    model = Product
    template_name = 'ecommerce/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(description__icontains=query) | Q(name__icontains=query)
        )
        return object_list


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'ecommerce/create.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'ecommerce/create.html',
                  {'cart': cart, 'form': form})

