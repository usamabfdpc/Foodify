from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from foodify.models import RecipeeCategory

# Create your views here.

def change_category_display(request):
    cid = int(request.POST['cid'])
    instances = RecipeeCategory.objects.all().order_by('-id')
    currenet_instance = instances[cid]
    currenet_instance_json = serializers.serialize("json",[currenet_instance])
    print(f"Before save  {currenet_instance} status : ",currenet_instance.status)
    if currenet_instance.status:
        currenet_instance.status = False
    else:
        currenet_instance.status = True

    currenet_instance.save()

    return JsonResponse({'status':'saved','category':currenet_instance_json})

def delete_category_display(request):
    
    return JsonResponse({'status':1})