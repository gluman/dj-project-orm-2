from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('school.json') as f:
            data = json.load(f)
            for record in data:
                person = {
                    'model': ,
                    'shop': Shop,
                    'book': Book,
                    'stock': Stock,
                    'sale': Sale,
                }[record.get()]
            return print('done')

