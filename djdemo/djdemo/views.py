from django.http import HttpResponse

def notfound(request):
    return HttpResponse("File not found")

def hello(request):
    return HttpResponse("Hello world")

import datetime
def time(request):
    now=datetime.datetime.now()
    html="<html><body>It's now %s.</body></html>" %now
    return HttpResponse(html)

