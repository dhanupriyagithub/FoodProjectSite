


# views.py
from django.shortcuts import render
from productapp.models import DemoModel

def base_site(request):
    products  = DemoModel.objects.all()
    return render(request, 'admin/product_list.html', {'products': products})

