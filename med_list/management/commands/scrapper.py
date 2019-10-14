from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Download and process the source'

    def handle(self, *args, **options):
        response = requests.get(settings.SOURCE_URL)

        if response.status_code != 200:
            print(f'woops: {response}')
            return

        parsed_html = BeautifulSoup(response.text, features='html.parser')
        lists = parsed_html.find_all('li')

        good_lines = []
        for el in lists:
            lines = [str.strip(line) for line in str.splitlines(el.text)]
            good_lines += lines

        with open(settings.NEW_DATA, 'w') as f:
            # empirically clarified that useful information starts with line with number START_LINE_NUMBER and ends with line with content TERMINATE_LINE
            for i, line in enumerate(good_lines):
                if i > settings.START_LINE_NUMBER:
                    if line == settings.TERMINATE_LINE:
                        break

                    f.write(f'{line}\n')
