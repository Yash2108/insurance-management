from django.shortcuts import render
from .forms import InsuranceForm
from .models import Insurances
# Create your views here.
def home(request):
    if request.method == "POST":
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = InsuranceForm()
    return render(request, 'myapp/home.html', context={'form':form})