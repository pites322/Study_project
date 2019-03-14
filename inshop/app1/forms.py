from django_registration.forms import RegistrationForm
from .models import User, ShoppingList, Product
from django import forms


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

        # def __init__(self, *args, **kwargs):
        #     self.fields[email_field].required = False


class AddBuy(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = []


class ChangeWarranty(forms.ModelForm):
    class Meta:
        model = Product
        fields = []