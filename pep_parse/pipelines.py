import datetime as dt
import os

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_dict = {}

    def process_item(self, item, spider):
        status = item['status']
        if status in self.status_dict:
            self.status_dict[status] += 1
        else:
            self.status_dict[status] = 1
        return item

    def close_spider(self, spider):
        filename = os.path.join(
            BASE_DIR,
            'results',
            ('status_summary_'
             f'{dt.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")}.csv')
        )
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = sum(self.status_dict.values())
            for status, quantity in self.status_dict.items():
                f.write(f'{status}, {quantity}\n')
            f.write(f'Total,{total}\n')
