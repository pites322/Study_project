from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, ShoppingList, User
from .forms import AddBuy, ChangeWarranty
from django.utils import timezone
from django.views.generic.base import TemplateView
from functools import wraps


class HomePage(TemplateView):

    template_name = "app1/Main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['Products'] = Product.objects.all()
        purchases = ShoppingList.objects.all()
        purchase_amount = 0
        for purchase in purchases:
            if purchase.buyer_id == self.request.user.id:
                purchase_amount = purchase_amount + purchase.price
            else:
                pass
        context['purchase_amount'] = purchase_amount

        return context


def product_details(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    form = AddBuy()
    warr = ChangeWarranty(request.POST, instance=prod)
    if request.method == 'POST':
        form = form.save(commit=False)
        form.buyer = request.user
        form.buyer_id = request.user.id
        form.product_id = prod.id
        form.price = prod.price
        form.data_of_buy = timezone.now()
        form.payed_or_not = 'No'
        form.product_name = prod.name
        form.save()
        warr = warr.save()
        warr.name = prod.name
        warr.manufacturer = prod.manufacturer
        warr.color = prod.color
        warr.bluetooth_or_wire = prod.bluetooth_or_wire
        warr.connection_range = prod.connection_range
        warr.work_time = prod.work_time
        warr.warranty = prod.warranty - 1
        warr.wire_lenght = prod.wire_lenght
        warr.type_connector = prod.type_connector
        warr.price = prod.price
        warr.photo = prod.photo
        warr.save()
        return redirect('bits in bytes')
    else:
        pass
    return render(request, 'app1/prod_detail.html', {'prod': prod, 'form': form, 'warr': warr})
