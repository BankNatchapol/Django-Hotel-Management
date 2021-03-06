from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import connection

from roomtype.models import *
import json

# Create your views here.
class RoomTypeList(View):
    def get(self, request):
        roomtype = list(RoomType.objects.all().values())        
        data = dict()
        data['roomtype'] = roomtype
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class RoomTypeDetail(View):
    def get(self, request, pk):
        roomtype = get_object_or_404(RoomType, pk=pk)
        data = dict()
        
        data['roomtype'] = model_to_dict(roomtype)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class RoomTypeUpdate(View):
    def post(self, request, pk): 
        
        data = dict()
        roomtype = RoomType.objects.get(pk=pk)
        request.POST = request.POST.copy()
        
        request.POST['type'] = pk
        request.POST['number'] =  reFormatNumber(request.POST['roomtype[number]'])
        request.POST['available'] = reFormatNumber(request.POST['roomtype[available]'])
        request.POST['price'] = reFormatNumber(request.POST['roomtype[price]'])
        request.POST['exprice'] = reFormatNumber(request.POST['roomtype[exprice]'])
        
        

        form = RoomTypeForm(instance=roomtype, data=request.POST)
        if form.is_valid():
            reservation = form.save()

            data['roomtype'] = model_to_dict(reservation)
        else:
            data['error'] = 'form not valid!'

        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [name[0].replace(" ", "_").lower() for name in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def reFormatNumber(str):
        if (str == ''):
            return ''
        return str.replace(",", "")