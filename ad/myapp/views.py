from datetime import datetime

from django.shortcuts import render
import logging
from django.http import HttpResponse
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    html = """
       <!DOCTYPE html>
       <html lang="en">
           <head>
               <meta charset="UTF-8">
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Мой первый Django-сайт</title>
           </head>
           <body>
               <h1>Добро пожаловать на мой первый Django-сайт!</h1>

               <h2>О сайте</h2>
               <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python.</p>

               <h2>Обо мне</h2>
               <p>Доброго дня, меня зовут Alex. Я учащийся GeekBrains. Меня всегда привлекала разработка. 
               Мои навыки включают Python, Flask и теперь ещё Django.</p>

               <footer>
                   <p>Мои контакты: mail@mail.ru | +77777777777</p>
               </footer>
           </body>
       </html>
       """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)

def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Обо мне</title>
        </head>
        <body>
            <header>
                <h1>Доброго дня! Я Alex</h1>
            </header>

            <main>
                <section>
                    <h2>Опыт работы</h2>
                    <ul>
                        <li>Место работы 1</li>
                        <li>Место работы 2</li>
                        
                    </ul>
                </section>

                <section>
                    <h2>Образование</h2>
                    <ul>
                        <li>Университет: 1 высшее образование</li>
                        <li>Университет: 2 высшее образование</li>
                        <li>Аспирантура: кандидат наук</li>
                    </ul>
                </section>

                <section>
                    <h2>Навыки</h2>
                    <ul>
                        <li>Навык 1</li>
                        <li>Навык 2</li>
                    </ul>
                </section>
            </main>

            <footer>
                <p>Мои контакты: mail@mail.ru | +77777777777</p>
            </footer>
        </body>
    </html>
    """
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)