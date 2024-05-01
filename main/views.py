from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.
from .serializers import *
from rest_framework import viewsets
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class RigViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListRigsSerializers
    def get_queryset(self):
        return Rig.objects.filter(box_rigs__reserved=False)


class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializers
    queryset = Package.objects.all()


def reader(request):
    return JsonResponse({"ok":"data"})



def index(request):
    barcode = request.GET.get("code")
    print("barcode",barcode)
    if barcode:
        try:
            _get = Package.objects.get(bar_code=barcode)
            if _get.box.reserved == True:
                print("okeyy")
            messages.warning(request,f"""
                {barcode}
            """)
            return HttpResponseRedirect(reverse('index'))
        except Exception as e: 
            print(e)
            messages.warning(request,"Gonderilen barkod yanlisdir zehmet olmasa texniki xidmet ile elaqe saxlayin")
    return render(request,"index.html")


def delivery(request):
    
    barcode = request.GET.get("code")
    print("barcode",barcode)
    if barcode:
        try:
            _get = Package.objects.get(bar_code=barcode)
            if _get.box.reserved == True:
                print("okey")
            messages.warning(request,f"""
                {barcode}
            
            """)
            return HttpResponseRedirect(reverse('index'))
        except Exception as e: 
            print(e)
            messages.warning(request,"Gonderilen barkod yanlisdir zehmet olmasa texniki xidmet ile elaqe saxlayin")
    return render(request,"delivery.html")


def client(request):
    return render(request,"client.html")


def client_bar_code(request):
    barcode = request.GET.get("code")
    if barcode:
        try:
            _get = Package.objects.get(bar_code=barcode)
            if _get.box.reserved == True and _get.status == True:
                ...
            return redirect("index")
        except: messages.warning(request,"Gonderilen barkod yanlisdir zehmet olmasa texniki xidmet ile elaqe saxlayin")
    return render(request,"delivery.html")