from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import Insurances
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse

# Create your views here.

class InsuranceInsert(FormView):

    model = Insurances
    def post(self, request):
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(form.errors['date'])
        return redirect('insurance_insert')

    def get(self, request):
        form = InsuranceForm()
        return render(request, 'myapp/insuranceForm.html', context={ 'form':form})

class AllInsurances(ListView):
    model = Insurances
    def get(self, request):
        # <view logic>
        form = InsuranceForm()
        insurance = Insurances.objects.all()
        return render(request, 'myapp/allInsurances.html', context={'insurances':insurance, 'form': form})

class InsuranceUpdate(UpdateView):
    model = Insurances
    template_name = 'myapp/insuranceUpdate.html'
    fields = '__all__'
    form=InsuranceForm()
    success_url = "/insurance/"
    # def get(self, request, pk):
    #     form=InsuranceForm()
    #     insurance=Insurances.objects.filter(id=pk)
    #     return render(request, 'myapp/insuranceUpdate.html', context={'insurance':insurance[0],'form':form})
    # def get_context_data(self, **kwargs): 
    #     context = super(InsuranceUpdate, self).get_context_data(**kwargs) 
    #     context['policyID'] = self.get_object().policyID 
    #     context['name'] = self.get_object().name 
    #     context['insuranceType'] = self.get_object().insuranceType
    #     context['dateOfCommencement'] = self.get_object().dateOfCommencement 
    #     context['expiryType'] = self.get_object().expiryType 
    #     context['installmentAmount'] = self.get_object().installmentAmount 
    #     context['maturityAmount'] = self.get_object().maturityAmount 
    #     context['dateOfMaturity'] = self.get_object().dateOfMaturity 
    #     context['aadhar'] = self.get_object().aadhar 
    #     context['confirmation'] = self.get_object().confirmation 
    #     return context

class InsuranceDelete(DeleteView):
    model = Insurances
    template_name = 'myapp/insuranceDelete.html'
    success_url = reverse_lazy('insurance_view')