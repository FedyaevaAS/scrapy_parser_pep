# Асинхронный парсер PEP
### Описание
Парсер выводит собранную информацию в два файла .csv:
 - Список всех PEP: номер, название и статус.
 - Сводка по статусам PEP — сколько найдено документов в каждом статусе (статус, количество)

### Стек
- Python
- Scrapy

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/FedyaevaAS/scrapy_parser_pep
cd scrapy_parser_pep/
```
Cоздать и активировать виртуальное окружение:
```
py -m venv env
```
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить парсер
```
scrapy crawl pep
```
### Автор
Федяева Анастасия
