from django.shortcuts import render
from django.utils import timezone


def index(request):
    """トップページのビュー"""
    print("localtime: ", timezone.localtime().date())
    print("timezone: ", timezone.now().date())
    return render(request, "counter/index.html")