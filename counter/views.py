from django.shortcuts import render
from django.utils import timezone


def index(request):
    """トップページのビュー"""
    print("localtime: ", timezone.localtime())
    print("timezone: ", timezone.now())
    return render(request, "counter/index.html")