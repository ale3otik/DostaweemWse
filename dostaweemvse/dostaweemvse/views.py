from django.http import HttpResponse
from django.http import QueryDict

def index(request):
    return HttpResponse("<b>Hello, world. You're at the index.<b/>" )

def order_info(request):
    query_dict = request.GET
    try:
        order_id = query_dict['order_id']
    except:
        order_id = None
    
    if order_id is None:
        return HttpResponse('Please type-in correct order_id')    
    return HttpResponse('order id is %s' %  order_id)
