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
