from django.shortcuts import render
from .forms import InsuranceForm
from .models import Insurances
from django.views.generic import FormView
# Create your views here.

class Home(FormView):
    model = Insurances
    def post(self, request):
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    def get(self, request):
        form = InsuranceForm()
        insurance = Insurances.objects.all()
        return render(request, 'myapp/home.html', context={'insurance':insurance, 'form':form})
# def home(request):
#     if request.method == "POST":
        
    