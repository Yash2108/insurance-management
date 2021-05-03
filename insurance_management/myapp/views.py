from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import Insurances
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse


class InsuranceInsert(FormView):
    model = Insurances

    def post(self, request):
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('insurance_insert')

    def get(self, request):
        form = InsuranceForm()
        return render(request, 'myapp/insuranceForm.html', context={ 'form':form})

class AllInsurances(ListView):
    model = Insurances

    def get(self, request):
        form = InsuranceForm()
        insurance = Insurances.objects.all()
        return render(request, 'myapp/allInsurances.html', context={
            'insurances':insurance, 
            'form': form, 
            'expiry':expiryChoices,
            'insuranceChoices': insuranceChoices})

class InsuranceUpdate(UpdateView):
    model = Insurances
    template_name = 'myapp/insuranceUpdate.html'
    form_class=InsuranceForm
    success_url = "/insurance/"

class InsuranceDelete(DeleteView):
    model = Insurances
    template_name = 'myapp/insuranceDelete.html'
    success_url = reverse_lazy('insurance_view')