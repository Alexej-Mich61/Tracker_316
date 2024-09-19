from django.shortcuts import render
# ./cards/views.py
from django.http import HttpResponse

def main(request):
    return HttpResponse("Привет, мир!")
