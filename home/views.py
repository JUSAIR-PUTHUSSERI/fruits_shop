from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def Product_Home(request):
    products=Product.objects.order_by('id')[:3]
   
    return render(request,'index.html',{'products':products})


@login_required(login_url='login')
def Product_list(request):
    all_products=Product.objects.all()
    context={
        'all_products':all_products
    }
    return render(request,'All_products.html',context)

def Product_list_one(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'product_list.html',{'product':product})

def product_search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(product_name__icontains=query) if query else []
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search_results.html', context)



