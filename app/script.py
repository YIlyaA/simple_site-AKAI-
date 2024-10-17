import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') 

django.setup()

from website.models import DataCris

with open('fixtures/website/dane.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data:
    datacris = DataCris.objects.create(
        typ=entry['Typ'],
        masa=entry['Masa'],
        czystosc=entry['Czystosc'],
        barwa=entry['Barwa'],
        pochodzenie=entry['Pochodzenie'],
        wlasciciel=entry['Własciciel']
    )
    datacris.save()

print("Dane zostały załadowane do bazy danych.")
