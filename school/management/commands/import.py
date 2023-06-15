from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('school.json') as f:
            pass
            # TO DO
            return print('done')

