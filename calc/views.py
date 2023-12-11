from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .forms import SetkaOrderForm
from .utils import calculate_weight_and_price


def check_params(request):
    if request.method == 'POST':
        form = SetkaOrderForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height'] * 1000
            length = form.cleaned_data['length'] * 1000
            rolls = form.cleaned_data['rolls']
            diameter = form.cleaned_data['diameter']
            cell_size = form.cleaned_data['cell_size']
        
            # Logic to process the data and return a JSON response
            weight, total_price = calculate_weight_and_price(height, length, rolls, diameter, cell_size, settings.PRICE_PER_KG)
            return JsonResponse({'result': {'weight': weight, 'total_price': total_price}})
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        form = SetkaOrderForm()
        return render(request, 'check_params.html', {'form': form})