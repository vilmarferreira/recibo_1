from django import forms
from dal import autocomplete
from core.models import Receipt, Person


class ReceiptForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),widget=autocomplete.ModelSelect2(url='person-autocomplete'))

    class Meta:
        model=Receipt
        exclude= ()