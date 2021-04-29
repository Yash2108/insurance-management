from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', InsuranceInsert.as_view(), name='insurance_insert'),
    path('view/', AllInsurances.as_view(), name='insurance_view'),
    path('<int:pk>/', InsuranceUpdate.as_view(), name="insurance_update"),
    
    path('<int:pk>/delete/', InsuranceDelete.as_view(),name='insurance_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)