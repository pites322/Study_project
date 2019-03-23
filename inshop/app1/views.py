from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, ShoppingList, User
from .forms import AddBuy, ChangeWarranty, ChangeUserInformation
from django.utils import timezone
from django.views.generic.base import TemplateView
from functools import wraps


class HomePage(TemplateView):

    template_name = "app1/Main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['Products'] = Product.objects.all()
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
        warr.warranty = prod.warranty - 1
        warr.save()
        return redirect('bits in bytes')
    else:
        pass
    return render(request, 'app1/prod_detail.html', {'prod': prod, 'form': form, 'warr': warr})


class Profile(TemplateView):

    template_name = "app1/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        pk = self.request.user.id
        user_data = get_object_or_404(User, pk=pk)
        context['first_name'] = user_data.first_name
        context['last_name'] = user_data.last_name
        context['region'] = user_data.region
        context['city'] = user_data.city
        context['address'] = user_data.first_name
        context['delivery'] = user_data.first_name
        return context


def user_change_info(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeUserInformation(request.POST, instance=user)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('profile')
    else:
        form = ChangeUserInformation(instance=user)
    return render(request, 'app1/profile_correct.html', {'form': form})


def basket(request, pk=None):
    prod_in_bask = ShoppingList.objects.filter(buyer_id=request.user.id)
    if pk is not None:
        dell_pod = ShoppingList.objects.filter(id=pk)
        del_prod_obj = dell_pod.get()
        prod = get_object_or_404(Product, pk=del_prod_obj.product_id)
        dell_pod.delete()
        warr = ChangeWarranty(request.POST, instance=prod)
        warr = warr.save()
        warr.warranty = prod.warranty + 1
        warr.save()
        return redirect('basket')
    else:
        pass
    return render(request, 'app1/basket.html', {'prod_in_bask': prod_in_bask})