# ./cards/views.py
from django.http import HttpResponse
from django.shortcuts import render



def main(request):
    return HttpResponse("Привет, мир!")

def card_by_id(request, card_id):
    if card_id > 10:
        return HttpResponse("Такой карточки нет", status=404)
    return HttpResponse(f"Карточка с ID {card_id}") # вернет страницу с надписью Вы открыли карточку ...

def get_all_cards(request):
    return render(request, 'cards/catalog.html')



