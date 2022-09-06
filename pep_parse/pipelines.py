import datetime as dt
import os

from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Pep(Base):
    __tablename__ = 'pep'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(200))
    status = Column(String(50))


class PepParsePipeline:
    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        pep = Pep(
            number=item['number'],
            name=item['name'],
            status=item['status'],
        )
        self.session.add(pep)
        self.session.commit()
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
            query = self.session.query(
                Pep.status,
                func.count(Pep.status)
            ).group_by(Pep.status)
            total = 0
            for status, quantity in query:
                f.write(f'{status}, {quantity}\n')
                total += quantity
            f.write(f'Total,{total}\n')
        self.session.close()
