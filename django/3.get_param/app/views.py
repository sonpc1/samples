from django.http import HttpResponse

def login(request):
    name = request.GET.get('name','')
    request.session['name'] = name
    return HttpResponse('Logged is as:', name)
    
def index(request): 
    name = request.session.get('name', '')
    return HttpResponse('Hello ' + name)
   
