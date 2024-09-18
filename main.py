from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        'request': request,
        'name': 'Denis Ivanov',
        'email': 'my@501lab.ru',
        'github': 'https://github.com/dnb8866',
        'linkedin': 'https://www.linkedin.com/in/denis-ivanov-a1391b327/',
        'about': '''В свободное время читаю книги, пишу pet-проекты, хожу в тренажерный зал.
        
        Книги:
        1. Юн Цуй - Рецепты Python, 2024 
        2. Элис Жао - SQL Pocket Guide, 2024 
        3. Фишерман Л. В. - Git. Практическое руководство, 2021 
        4. Адитья Бхаргава - Грокаем Алгоритмы, 2017
        5. Марк Лутц - Изучаем Python (5-е издание). 
        ''',
        'programming_languages': ['Python'],
        'framework_and_tools': ['FastAPI', 'Aiogram', 'Django', 'SQLAlchemy[asyncpg, psycopg]', 'Asyncio', 'Git', 'Docker'],
        'education': [
            {
                'name': 'Сибирский государственный аэрокосмический университет им. академика М. Ф. Решетнева, 2010',
                'specified': 'Экономический факультет, Экономика и управление на предприятии машиностроения'
            }
        ],
        'projects': [
            {
                'name': 'Управление личными и семейными финансами',
                'url': 'https://t.me/family_finances_app_bot',
                'stack': ['Aiogram', 'Psycopg', 'PostgreSQL', 'Docker'],
                'description': 'Создание и управление учётными системами для управления личными и семейными финансами'
            },
            {
                'name': 'Мониторинг цен криптовалют',
                'url': 'https://t.me/MyCryptoInformer_bot',
                'stack': ['Aiogram', 'FastAPI', 'SQLAlchemy', 'PostgreSQL', 'Asyncio', 'RabbitMQ', 'Docker', 'Микросервисы'],
                'description': 'Создание и управление учётными системами для управления исходными данными в сфере бизнеса'
            },
            {
                'name': 'Интервальные повторения',
                'url': 'https://t.me/app_spaced_repetition_bot',
                'stack': ['Aiogram', 'FastAPI', 'SQLAlchemy', 'Asyncio', 'RabbitMQ'],
                'description': 'Создание и управление учётными системами для управления исходными данными в сфере бизнеса'
            }
        ],
        'experience': [
            {
                'name': 'Менеджер по работе с клиентами крупного и среднего бизнеса, Росбанк',
                'period': 'Сентябрь 2023 - Июль 2024',
                'description': [
                    'Управление продажами',
                    'Финансовый анализ',
                    'Структурирование сделок',
                    'Переговоры на уровне первых лиц'
                ]
            },
            {
                'name': 'Менеджер по работе с клиентами крупного и среднего бизнеса, Сбер',
                'period': 'Февраль 2017 - Сентябрь 2023',
                'description': [
                    'Управление продажами',
                    'Финансовый анализ',
                    'Структурирование сделок',
                    'Переговоры на уровне первых лиц'
                ]
            },
            {
                'name': 'Менеджер по работе с клиентами малого бизнеса, Альфа-банк',
                'period': 'Февраль 2013 - Май 2017',
                'description': [
                    'Управление продажами',
                    'Переговоры на уровне первых лиц'
                ]
            },
            {
                'name': 'Территориальный специалист, Билайн',
                'period': 'Август 2010 - Декабрь 2013',
                'description': [
                    'Управление продажами на закрепленной территории',
                    'Обучение, мотивация и контроль знаний персонала',
                    'Переговоры с собственниками бизнеса и ответственными лицами дилеров'
                ]
            },
        ]
    }
    return templates.TemplateResponse('index.html', context)
