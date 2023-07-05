from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import SaleForm
from .models import sales


# Create your views here.

def list_sales(request):
    all_sales = sales.objects.all()
    context = {
        'all_sales':all_sales
    }
    return render(request, 'cloth/index.html', context)

def get_sale(request, id):
    sale = sales.object.get(id=id)
    context = {
            "sale":sale
        }
    return render(request, 'cloth/index.html', context)

    
def create_sale(request):
    form = SaleForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('list_sales')
    
    context = {
        'form': form
    }
    return render(request, 'cloth/sale-form.html', context)


def update_sale(request, id):
    sale = sales.objects.get(id=id)
    
    form = SaleForm(request.POST or None, instance=sale)
    
    if form.is_valid():
        form.save()
        return redirect('list_sales')
    
    
    return render(request, 'cloth/sale-form.html', {'form':form, 'sale':sale})


def delete_sale(request, id):
    sale = sales.objects.get(id=id)
    
    if request.method == 'POST':
        sale.delete()
        return redirect ('list_sales')
    
    elif request.method == 'GET':
        context = {
            'form':SaleForm,
            'sale':sale
        }
        return render(request, 'cloth/sale-form.html', context)
