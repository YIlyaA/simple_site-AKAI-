import json
from django.core.management.base import BaseCommand
from website.models import DataCris

class Command(BaseCommand):
    help = 'Load data from JSON file into the DataCris model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Path to the JSON file containing the data.',
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        if not file_path:
            self.stdout.write(self.style.ERROR('Please provide a JSON file path using --file argument'))
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Invalid JSON format"))
            return

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

        self.stdout.write(self.style.SUCCESS(f"Data loaded successfully from {file_path}"))
