from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Product
from django.core import serializers
import json
# from .forms import ProductForm

# Create your views here.


def list_products(request):
    product_data = Product.objects.all()
    
    # print(list(products))
    product_list = list(product_data)
    data = serializers.serialize('json', product_list)
    # print(json.loads(data))
    result = json.loads(data)
    print(result[0]['model'])
    # # return JsonResponse(student_list, safe=False)
    return render(request, 'products.html', {'products': result})
    # # return render(request, 'products.html', {'products': products})
