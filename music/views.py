from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>Pagina Principal de la musica</H1>");
