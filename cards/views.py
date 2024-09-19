from django.shortcuts import render
# ./cards/views.py
from django.http import HttpResponse

def main(request):
    return HttpResponse("Привет, мир!")

def card_by_id(request, card_id):
    if card_id > 10:
        return HttpResponse("Такой карточки нет", status=404)
    return HttpResponse(f"Карточка с ID {card_id}") # вернет страницу с надписью Вы открыли карточку ...

def get_all_cards(request):
    return HttpResponse("Все карточки") # вернет страницу с надписью Все карточки


