from django.shortcuts import render
from .models import pages
from django.utils import timezone
from .forms import SearchForm
from django.shortcuts import redirect
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def main(request):
	return render(request, 'home/main.html', {})

def home(request):
	temas = pages.objects.all().order_by('-fecha_creacion')[:9]

	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'home/index.html', { 'temas': temas })

def cursos(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/menu.html', {})

def search(request, tema):
	if request.method == "POST":
		busque = request.POST.get('tema_search')
		if busque:
			return redirect('search', tema=busque)

	
	busqueda = pages.objects.filter(titulo__contains=tema)
	temabuscado = tema
	longi_tema = len(tema)
	if longi_tema > 3:
		fintema = int(longi_tema / 2)
		mitad1 = tema[0:fintema]
		mitad2 = tema[fintema: longi_tema]
		busqueda |= pages.objects.filter(titulo__contains=mitad1)
		busqueda |= pages.objects.filter(titulo__contains=mitad2)
	else:
		temabuscado = tema

	return render(request, 'pages/search.html', { 'busqueda': busqueda, 'tema': temabuscado})

#Temas de recurso de aprendizaje

def clases(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/clases.html', {})

def pizarron(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron.html', {})

def pizarron_pequeño(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron/pizarron_pequeño.html', {})

def pizarron_mediano(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron/pizarron_mediano.html', {})

def pizarron_grande(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron/pizarron_grande.html', {})

def pizarron_edicion_final(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron/edicion_final.html', {})

def pizarron_clase(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron/clase.html', {})

def cuaderno(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/cuaderno.html', {})

def entorno_de_grabacion(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/cuaderno/entorno_de_grabacion.html', {})

def cuaderno_clase(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/cuaderno/clase.html', {})

def captura_de_pantalla(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/captura_de_pantalla.html', {})

def material_de_estudios(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/captura_de_pantalla/material_de_estudios.html', {})

def grabacion_en_SMRecorder(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/captura_de_pantalla/grabacion_en_SMRecorder.html', {})

def captura_clase_final(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/captura_de_pantalla/clase_final.html', {})

def presentacion_estatica(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/presentacion_estatica.html', {})

def lista_de_aplicaciones(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/presentacion_estatica/lista_de_aplicaciones.html', {})

def multipantalla(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/multipantalla.html', {})

def dimensiones_estructura_costo(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/multipantalla/dimensiones_estructura_costo.html', {})

def estudio(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/multipantalla/estudio.html', {})

def plumones(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/multipantalla/plumones.html', {})

def aula(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/aula.html', {})

def dispositivos_y_camara(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/aula/dispositivos_y_camara.html', {})

def camara_y_material_de_apoyo(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/aula/camara_y_material_de_apoyo.html', {})

def aula_edicion_final(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/aula/edicion_final.html', {})

def pizarron_de_cristal(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal.html', {})

def pizarron_de_cristal_01(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_01.html', {})

def pizarron_de_cristal_02(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_02.html', {})

def pizarron_de_cristal_03(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_03.html', {})

def pizarron_de_cristal_04(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_04.html', {})

def pizarron_de_cristal_05(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_05.html', {})

def pizarron_de_cristal_06(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_06.html', {})

def pizarron_de_cristal_07(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_07.html', {})

def pizarron_de_cristal_08(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_08.html', {})

def pizarron_de_cristal_09(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_09.html', {})

def pizarron_de_cristal_10(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_10.html', {})

def pizarron_de_cristal_11(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_11.html', {})

def pizarron_de_cristal_12(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_12.html', {})

def pizarron_de_cristal_13(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_13.html', {})

def pizarron_de_cristal_14(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_14.html', {})

def pizarron_de_cristal_15(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_15.html', {})

def pizarron_de_cristal_16(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_16.html', {})

def pizarron_de_cristal_17(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_17.html', {})

def pizarron_de_cristal_18(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return	render(request, 'pages/primernivel/clases/pizarron_de_cristal/0101_18.html', {})

def imagenes(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/imagenes.html', {})

def imagen_01(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/imagenes/imagen_01.html', {})

def imagen_02(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/imagenes/imagen_02.html', {})

def download_imagen(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'recursos_aprendizaje_imagenes.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def forosychats(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/forosychats.html', {})

def chats(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/forosychats/chats.html', {})

def chat_depure(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/forosychats/chats/chats_01.html', {})

def chat_administrador(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/forosychats/chats/chats_02.html', {})

def chat_cliente(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/forosychats/chats/chats_03.html', {})

def videoconferencias(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/videoconferencias.html', {})

def videoconferencias_01(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/videoconferencias/videoconferencia_01.html', {})

def videoconferencias_02(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/videoconferencias/videoconferencia_02.html', {})

def videoconferencias_03(request):
	if request.method == "POST":
		busqueda = request.POST.get('tema_search')
		if busqueda:
			return redirect('search', tema=busqueda)

	return render(request, 'pages/primernivel/videoconferencias/videoconferencia_03.html', {})