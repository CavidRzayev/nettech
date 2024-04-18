from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def reader(request):
    return JsonResponse({"ok":"data"})