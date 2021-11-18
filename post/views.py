from django.http import HttpResponse
import random

def random_num(request):
    return HttpResponse(random.randint(1, 10))
