# ./cards/views.py
from django.http import HttpResponse
from django.shortcuts import render

info = {
    "users_count": 100500,
    "cards_count": 200600,
    "menu": ["Главная", "О проекте", "Каталог"],
}


def main(request):
    return HttpResponse("Привет, мир!")

def card_by_id(request, card_id):
    if card_id > 10:
        return HttpResponse("Такой карточки нет", status=404)
    return HttpResponse(f"Карточка с ID {card_id}") # вернет страницу с надписью Вы открыли карточку ...

def get_all_cards(request):
    """
        Принимает информацию о проекте (словарь info)
        Возвращает шаблон по адресу templates/cards/catalog.html
        :param request:
        :return:
    """
    return render(request, 'cards/catalog.html', context=info)



