from django.shortcuts import render, get_object_or_404, redirect
from redirect.models import Redirect

# Create your views here.


def redirect_view(request, slug):
    redirect_obj = get_object_or_404(Redirect, slug=slug)
    return redirect(redirect_obj.destination)
