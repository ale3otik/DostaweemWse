from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import render

def index(request):
    return render(request,'index.html', dict())

def order_info(request):
    query_dict = request.GET
    try:
        order_id = query_dict['order_id']
    except:
        order_id = None
    
    if order_id is None:
        return HttpResponse("<a href='/index'> На главную <a/> <br/><br/>" 
            + 'Пожалуйста, введите корректный номер заказа')    

    context = {'order_id' : order_id}
    return render(request,'order_info.html', context)

def make_order(request):
    return render(request,'make_order.html', dict())