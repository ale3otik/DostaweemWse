from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import render

def index(request):
    return render(request,'index.html', dict())

def get_order_info(request):
    return render(request,'get_order_info.html', dict())

def order_info(request):
    query_dict = request.GET
    try:
        order_id = query_dict['order_id']
    except:
        order_id = None
    
    if order_id is None:
        return HttpResponse("<a href='/index'> На главную <a/> <br/><br/>" 
            + 'Пожалуйста, введите корректный номер заказа')    

    id_found = False
    if not id_found:
        return HttpResponse("<a href='/index'> На главную <a/> <br/><br/>" 
            + 'Заказ №<b> %s </b> не найден :(' % order_id)    

    context = {'order_id' : order_id}
    return render(request,'order_info.html', context)

def make_order_form(request):
    return render(request,'make_order_form.html', dict())

def make_order(request):
    
    success = True
    created_order_id = 12
    reason_of_failure = 'Wrong target address'

    if success:
        return render(request,'make_order_success.html', {'order_id' : created_order_id})
    else :
        return render(request,'make_order_failure.html', {'reason' : reason_of_failure})