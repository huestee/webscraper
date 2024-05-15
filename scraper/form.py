from django import forms

class ProductSearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    reference = forms.CharField(max_length=100, required=False)
    sku = forms.CharField(max_length=50, required=False)
