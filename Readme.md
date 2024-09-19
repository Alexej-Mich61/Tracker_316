# Django. Учебный проект "Tracker_316"
## Создание проекта
### 
1. Создал репозиторий
2. Создал проект Tracker_316
3. Установка зависимости 'pip install django==4.2'
4. Сохранил зависимости в файл 'requirements.txt' командой 'pip freeze > requirements.txt' Для возможности сделать Гитклон

Развернуть проект на локальной машине:
- Склонировать репозиторий командой 'git clone'
- Перейти в папку проекта 'cd Tracker_316'
- Создать виртуальное окружение 'python -m venv venv'
- Активировать виртуальное окружение 'source venv/bin/activate'
- Установить зависимости 'pip install -r requirements.txt'

### Создание Django project
1. Создал проект 'django-admin startproject tracker .'
Создаем проект tracker в текущей директории, без создания папок дополнительных с именем проекта.

2. Запуск проекта 'python manage.py runserver' В терминале на одном уровне с manage.py  Остановить сервер Ctrl+C

Команды терминала:
- python manage.py runserver - запуск сервера
- cd - смена директории
- cd.. - переход на 1 уровень вые
- ls - просмотр содержимого директории
- pwd показать текущую директорию

3. Создаю приложение 'python manage.py startapp cards'
После создания приложения регистрируем его в файле settings.py в разделе INSTALLED_APPS
Без этого приложение не будет работать

### Создали первое представление 
# ./cards/views.py
from django.http import HttpResponse
def main(request):
    return HttpResponse("Привет, мир!")
### Создали первый URL 
чтобы приложение заработало, его надо зарегистрировать в urls.py конфигурации проекта

path('', views.main),

Теперь при переходе на главную страницу сайта видно Привет мир

### Создаем детальное представление карточки по ее ID
Для этого создаем новый маршрут с конвертом int, который будет принимать ID карточки

    path('admin/', admin.site.urls),
    path('', views.main),
    path('cards/<int:card_id>/', views.card_by_id, name='card_detail'),

а также функцию, которая будет обрабатывать запрос и возвращать страницу с детальной информацией о карточке

def card_by_id(request, card_id):
    if card_id > 10:
        return HttpResponse("Такой карточки нет", status=404)
    return HttpResponse(f"Карточка с ID {card_id}")

### include и собственный файл urls.py для приложения cards
1. Создал еще одно представление 'get_all_cards' в файле 'views.py'
2. Создал файл urls.py в директории приложения cards
3. Зарегистрировали новый файл 'urls.py' в файле urls.py конфигурации проекта с помощью функции include
4. Зарегистрировали маршруты без префикса 'cards/' в файле 'urls.py' приложения 'cards'
5. Удалили маршруты cards/ из файла urls.py конфигурации проекта
