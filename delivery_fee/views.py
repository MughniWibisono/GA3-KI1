from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from deliver_fee.models import Task
import datetime

def show_fee(request):
    delivery_fee_price = Task.objects.all()
    context = {
        'list_item': delivery_fee_price,
    }
    return render(request, "R_delivery_fee.html",context)

def add_fee(request):
    if request.method == "POST":
        province = request.POST.get("province")
        motorate = request.POST.get("motorate")
        carrate = request.POST.get("carrate")
        Task.objects.create(
            user=request.user,
            province=province,
            motorate=motorate,
            carrate=carrate,
        )
        return HttpResponseRedirect(reverse("delivery_fee:show_fee"))
    return render(request, "C_delivery_fee.html")

def change_fee(request):
    if request.method == "PUT":
        task = Task.objects.get(user=request.user, id=id)
        task.save()
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "province": task.province,
                    "motorate": task.motorate,
                    "carrate": task.carrate,
                },
            },
            status=200,
        )

def delete_fee(request, id):
    if request.method == "DELETE":
        task = Task.objects.get(user=request.user, id=id)
        task.delete()
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "province": task.province,
                    "motorate": task.motorate,
                    "carrate": task.carrate,
                },
            },
            status=200,
        )
