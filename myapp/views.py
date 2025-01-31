
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from myapp.models import Items
from django.views.decorators.csrf import csrf_exempt
from myapp.forms import ItemsForm
# Create your views here.

def home_func(request):
    if request.method=='GET':
        return JsonResponse({"msg":"Welcome to home Page"}, status=200)
    return JsonResponse({"msg":"Invalid Request Method"}, status=405)

def path_param_func(request,id):
    if request.method=='GET':
        return JsonResponse({"msg":f"path param is {id}"},status=200)
    return JsonResponse({"msg":"Invalid Request Method"},status=405)

def query_param_func(request):
    if request.method=='GET':
        # name=request.GET.get('name')
        # age=request.GET.get('age')
        # same_keys=request.GET.getlist('name')   """when same keys are present"""
        data=request.GET.dict()
    return JsonResponse({"msg":f"query params are {data} "},status=200)

@csrf_exempt
def insert_data(request):
    if request.method=='POST':
        data=json.loads(request.body)
        # print(data,type(data))
        name,quantity=data['name'],data['quantity']
        item=Items.objects.create(name=name,quantity=quantity)
        item.save()
        return JsonResponse({"id":item.id,'name':item.name,'quantity':item.quantity,'created_at':item.created_at,'updated_at':item.updated_at},status=201)
    return JsonResponse({"msg":"Invalid Request method"},status=405)

@csrf_exempt
def insert_form_data(request):
    if request.method=='POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            item=form.save()
            return JsonResponse({"id":item.id,"name":item.name,"quantity":item.quantity,"price":item.price,"description":item.description,"created_at":item.created_at,"updated_at":item.updated_at},status=201)
        err=form.errors
        return JsonResponse(err)
    return JsonResponse({"msg":"Invalid Request Method"},status=405)

def raw_html(request):
    s="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Views</title>
</head>
<body>
<h1> This is from Views</h1>
</body>
</html>
        """
    return HttpResponse(s)

def html(request):
    return render(request,'index.html')

# def redirect_func(request):

