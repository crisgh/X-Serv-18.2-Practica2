from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from models import URL
from django.shortcuts import redirect # Redireccion

# Create your views here.

@csrf_exempt
def acorta(request):

    if request.method == 'GET':

        template = get_template('plantilla.html')
        context = ({})
        return HttpResponse(template.render(context))

    elif request.method == 'POST':

        url_original = request.POST['original']
        print str(url_original)
        if not url_original.find("http://"):
            #print "tiene http://"
            pass
        elif not url_original.find("https://"):
            #print "Tiene el https, no hace falta ponerlo"
            pass
        else:
            #print "No lo tiene, ponemos el http://"
            url_original = "http://" + url_original

        try:

            pages = URL.objects.all()
            page = URL.objects.get(original=url_original)
            cortada = len(pages) + 1

            #page = URL.objects.get(original=url_original)
            template = get_template('realizada.html')
            context = ({'original':page.original, 'cortada':page.cortada})
            respuesta = template.render(context)

        except URL.DoesNotExist:
            pages = URL.objects.all()

            corta = len(pages) + 1
            url_new = URL(original=url_original, cortada=corta)
            url_new.save()
            template = get_template('acortada.html')
            context = ({'original':url_original, 'cortada':corta})
            respuesta =  template.render(context)

        return HttpResponse(respuesta)

def redirection(request, pagina):
    try:
        page = URL.objects.get(cortada= pagina)
        if page == page.original :
            return redirect(str(page.original))
#            respuesta = "<html><h3> Pinche en el siguiente enlace para el redireccionamiento :<h3> "
#            respuesta +="<l><a href = '"+str(page.original)+"'>"+str(page.original)+"</a></l></body></html>"
#            return HttpResponse(respuesta)
        else:
    # Seria para la pagina corta : page = URL.objects.get(corta = pagina)
            #respuesta = "<html><body> Pinche en el siguiente enlace para el redireccionamiento : "
            #respuesta +="<html><a href = '"+str(page.original)+"'>"+str(page.original)+"</a></body></html>"
            #return HttpResponse(respuesta) -- Esto es para tener un li
            return redirect(str(page.original))
    except URL.DoesNotExist:
        respuesta = "<html><body><h1>Pagina no encontrada, intentelo con otra url.</h1></body></html>"
        return HttpResponse(respuesta)
def mostrar(request):

    Lista = URL.objects.all()
    if not Lista :
        respuesta = "<html><h2><body>No hay urls aun.</body></h2></html>"
        return HttpResponse(respuesta)
    else:
        respuesta = "<html><title>Urls</title><h3><b><i>Tenemos las siguientes urls : </b></i></h3></html>"
        respuesta += "<ol>"
        for page in Lista:
            respuesta += "<li><a href = '"+str(page.original)+"'>"+str(page.original)+"</a>"
        respuesta += "</ol>"

        return HttpResponse(respuesta)
def error(request):
    respuesta ="<html><title>Error</title><h3> Tienes que poner una url valida </h3>"
    respuesta +="<a href = '/acorta'>Acortar Url<br></a>"
    respuesta +="<a href='/mostrar'> Mostrar Url<br></a>"
    respuesta += "o introduce : 127.0.0.1:8000/numero<br></html>"

    return HttpResponse(respuesta)
