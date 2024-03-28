from datetime import datetime
import logging
from django.http import HttpResponse
from djangoProject.ad.myapp.models import Client

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

def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()

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
                <a href='/'>Home</a>
                <a href='/about/'>About</a>
                <a href='/clients'>Clients</a>
            <h1>Clients list</h2>
            <table>
            <tr>
                <td>Name</td>
                <td>E-mail</td>
                <td>Phone</td>
                <td>Address</td>
            </tr>
            """
    for client in clients:
        html += """<tr>
                 f<td>{client.client_name}</td>
                 f<td>{client.email}</td>
                 f<td>{client.phone}</td>
                 f<td>{client.address}</td>
                 </tr>"""
    html += """</table>"""
    logger.info(f'посещение страницы Clients в: {datetime.now()}')
    return HttpResponse(html)