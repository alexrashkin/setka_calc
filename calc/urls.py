from django.urls import path

from .views import check_params

urlpatterns = [
    path('', check_params, name='check_params'),
]