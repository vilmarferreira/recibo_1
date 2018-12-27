from django.shortcuts import render
from dal import autocomplete


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.form import ReceiptForm
from core.models import Receipt, Person


class createReceipt(CreateView):
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy('index')
    template_name = 'core/form2.html'

def index(request):
    return render(request,'core/index.html')


class PersonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !


        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
