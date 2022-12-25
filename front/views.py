from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def service_worker(request):
    sw_path = settings.BASE_DIR / "front/static" / "sw.js"
    response = HttpResponse(open(sw_path).read(), content_type='application/javascript')
    return response



def pagelogout(request):
    if request.method == "POST":
        logout(request)

        return redirect('home')


def my_game(request):
    return render(request,'index.html')
def third_page(request):
    return render(request,'geogebra.html')