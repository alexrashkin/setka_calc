# Generated by Django 3.2 on 2023-11-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SetkaOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rolls', models.PositiveIntegerField()),
            ],
        ),
    ]
