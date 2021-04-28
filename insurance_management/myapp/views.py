from django.shortcuts import render, redirect
from .forms import InsuranceForm
from .models import Insurances
from django.views.generic import FormView, ListView
from django.http import HttpResponse, JsonResponse

# Create your views here.

class Home(FormView):

    model = Insurances
    def post(self, request):
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(form.errors['date'])
        return redirect('home')

    def get(self, request):
        form = InsuranceForm()
        insurance = Insurances.objects.all()
        return render(request, 'myapp/home.html', context={ 'form':form})

class AllInsurances(ListView):
    def get(self, request):
        # <view logic>
        insurance = Insurances.objects.all()
        return HttpResponse('result')