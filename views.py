#django
from django.http import HttpResponse
#utilities
from datetime       import datetime

import json

def holaMundo(request):
    now  = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello World Hotra del servidor : {}'.format(now))

def hi(request):
    #import pdb; pdb.set_trace()
    print(request.META['QUERY_STRING'])
    queryString = request.META['QUERY_STRING']
    numbers     = queryString[(queryString.find('=')+ 1):]
    numbersL    = [int(n) for n in numbers.split(',')]
    numgersL    = numbersL.sort()
    print(numbersL)
    data = {
        'status'  : 'ok',
        'numbers' : numbersL,
        'message' : 'Integrers sorted successfuly'
    }
    return HttpResponse(json.dumps(data, indent = 4 ), content_type='application/json')
