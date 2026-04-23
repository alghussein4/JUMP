from django.core.management.base import BaseCommand
from hospitals.models import Governorate

class Command(BaseCommand):
    help = "Seed initial Jordan governorates"

    def handle(self, *args, **kwargs):
        governorates = [
            "Amman",
            "Irbid",
            "Zarqa",
            "Balqa",
            "Madaba",
            "Karak",
            "Tafileh",
            "Ma'an",
            "Aqaba",
            "Mafraq",
            "Jerash",
            "Ajloun",
        ]

        for name in governorates:
            obj, created = Governorate.objects.get_or_create(name=name)
            if created:
                self.stdout.write(f"Created: {name}")
            else:
                self.stdout.write(f"Already exists: {name}")

        self.stdout.write(self.style.SUCCESS("Done seeding governorates"))