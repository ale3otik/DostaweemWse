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
        return HttpResponse('Please type-in correct order_id')    
    return HttpResponse('order id is %s' %  order_id)

def make_order(request):
    new_order_id = 1
    return HttpResponse('Order created, order id is %s' % new_order_id)