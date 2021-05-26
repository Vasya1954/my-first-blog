from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .models import products
from .forms import PostProduct, select_date

def main_page(request):
    return render(request, 'canteen/main.html')

def products_see(request):
    if request.method == "POST":
        form = PostProduct(request.POST)
        if form.is_valid():
            form.save()
            prod = products.objects.all()
            form = PostProduct()
            data = {'prod': prod, 'form': form}
    else:
        prod = products.objects.all()
        form = PostProduct()
        data = {'prod': prod, 'form': form}
    return render(request, 'canteen/products_add.html', context=data)

def products_edit(request, pk):
    product = products.objects.get(pk=pk)
    if request.method == "POST":
        form = PostProduct(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            return redirect('products_see')
    else:
        prod = products.objects.all()
        form = PostProduct(instance=product)
        data = {'prod': prod, 'form': form}
    return render(request, 'canteen/products_add.html', context=data)

def products_dell(request, pk):
    product = products.objects.get(pk=pk)
    product.delete()
    return redirect('products_see')

def days(request):
    return render(request, 'canteen/days.html')

def days_free(request):
    form = select_date()
    return render(request, 'canteen/days_free.html', {'form': form})

def days_cost(request):
    return render(request, 'canteen/days_cost.html')