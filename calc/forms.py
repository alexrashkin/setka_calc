from django import forms
from django.conf import settings


class SetkaOrderForm(forms.Form):
    height = forms.DecimalField(
        min_value=settings.MIN_HEIGHT / 1000,
        max_value=settings.MAX_HEIGHT / 1000,
        initial=1.5,
        decimal_places=2,  # Определение двух знаков после запятой
        label='Высота рулона (в метрах)'
    )
    length = forms.DecimalField(
        min_value=settings.MIN_ROLL_LENGTH / 1000,
        max_value=settings.MAX_ROLL_LENGTH / 1000,
        initial=10.0,
        decimal_places=2,
        label='Длина рулона (в метрах)'
    )
    rolls = forms.IntegerField(
        min_value=1,
        max_value=settings.MAX_ROLLS,
        initial=1,
        label='Количество рулонов'
    )
    diameter = forms.FloatField(
        initial=settings.DIAMETER,
        widget=forms.HiddenInput()
    )
    cell_size = forms.FloatField(
        min_value=settings.MIN_CELL_SIZE,
        max_value=settings.MAX_CELL_SIZE,
        initial=settings.MAX_CELL_SIZE,
        label='Размер ячейки (в миллиметрах)'
    )
