from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import render
from .models.service import Service

def index(request):
    return render(request,'index.html', dict())

def get_order_info(request):
    service = Service()
    return render(request,'get_order_info.html', dict())

def order_info(request):
    service = Service()
    query_dict = request.GET
    try:
        order_id = query_dict['order_id']
    except:
        order_id = None
    
    if order_id is None:
        return HttpResponse("<a href='/index'> На главную <a/> <br/><br/>" 
            + 'Пожалуйста, введите корректный номер заказа')    

    order_info_dict = service.get_order_info(order_id)
    
    '''
    order_info_dict =  {
        'source' : 'Москва',
        'target' : 'Казахстан',
        'route'  : ['Москва - Долгопрудный', 
                    'Долгопрудный - Лобня' , 
                    'Лобня - Казахстан', 
                    'Казахстан'],
        'position' : 2,
        'weight' : 13.3,
    }
    '''

    if order_info_dict is None:
        return HttpResponse("<a href='/index'> На главную <a/> <br/><br/>" 
            + 'Заказ №<b> %s </b> не найден :(' % order_id)    
    
    order_info_dict['order_id'] = order_id
    return render(request,'order_info.html', order_info_dict)

def make_order_form(request):
    return render(request,'make_order_form.html', dict())

def make_order(request):
    service = Service()

    success, response = service.make_order(request.GET)
    #success = True
    #created_order_id = 12
    #reason_of_failure = 'Wrong target address'
    if success:
        created_order_id = response
        return render(request,'make_order_success.html', {'order_id' : created_order_id})
    else :
        reason_of_failure = response
        return render(request,'make_order_failure.html', {'reason' : reason_of_failure})
        