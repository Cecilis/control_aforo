# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from rest_framework import views, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from monitor.forms import MonitorForm
from monitor.models import Monitor

from .serializers import MonitorSerializer, MonitorLinkSerializer, MonitorFSSerializer


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def monitor_url(request):
    if request.method == 'GET':
        MWF = request.GET.get('mwf', None)
        MBT = request.GET.get('mwf', None)
        #if MWF is not None and MBT is not None:
        link_info = {"url": "monitor/?c=1;z=9","token": "OWJDWU3ROWJDQOWDKPOQE92IJKDSHFFW8FKFSFIW803923234U2342J3HJ24HJ4B23J4"}
        monitor_link_serializer = MonitorLinkSerializer(data=link_info)
        if monitor_link_serializer.is_valid():
            return JsonResponse(monitor_link_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(monitor_link_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':     #Solicitud de Link por parte del STB
        monitor_data = JSONParser().parse(request)
        monitor_serializer = MonitorSerializer(data=monitor_data)
        if monitor_serializer.is_valid():
            #Consultar en la bd si estan bien ambos valores
            link_info = {"url": "monitor/?c=1;z=9","token": "OWJDWU3ROWJDQOWDKPOQE92IJKDSHFFW8FKFSFIW803923234U2342J3HJ24HJ4B23J4"}
            monitor_link_serializer = MonitorLinkSerializer(data=link_info)
            if monitor_link_serializer.is_valid():
                return JsonResponse(monitor_link_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'monitor_link_serializer':'errors'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'monitor_serializer':'errors'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def show(request):
    if request.method == 'GET':
        camara = request.GET.get('c', None)
        zona = request.GET.get('z', None)
        context = {'camara': camara, 'zona':zona }
        if camara is not None and zona is not None:
            return render(request, 'hzfullscreen.html', context)
        return JsonResponse({'camara': camara, 'zona' : zona, 'error:' : 'parametros erroneos'}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        return render('', 'hzfullscreen.html')
    else:
        return JsonResponse({'error:': 'request method not allowed'}, status=status.HTTP_400_BAD_REQUEST)
    
    
#Las demás
@login_required(login_url="/login/")
def monitor(request):
    activate('es')
    if request.method == "POST":
        form = MonitorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/monitor/todos')
            except Exception as e:
                print('Monitor Error >> %s (%s)' % (e, type(e)))
                pass
    else:
        #return HttpResponseForbidden('allowed only via POST')
        form = MonitorForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(error)
                #print(field.name % " | " % error)

    return render(request, 'monitor/agregar.html', {'form': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    monitores =  Monitor.objects.all()
    for monitor in monitores:
        monitor.id = str(monitor._id)
        #TODO:Split de id camara para ver detalles
        monitor.camara_serial = "ABCD-EFGH-UIYT-LOKK"
        monitor.zona_numero = "0"
    return render(request, "monitor/todos.html", {'form': monitores})



@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    monitor = get_object_or_404(Monitor, _id=id)
    form = MonitorForm(request.POST or None, instance=monitor)
    return render(request, 'monitor/editar.html', { 'form' : form })



@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    monitor = get_object_or_404(Monitor, _id=id)
    form = MonitorForm(request.POST or None, instance=monitor)
    form.id_camara_zona = "AAAA-BBBB-CCCC-DDDD_0"
    print('one')
    if form.is_valid():
        form.save()
        return redirect("/monitor/todos")
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name % " | " % error)
    return render(request, 'monitor/editar.html', { 'form' : form })

@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        monitor = Monitor.objects.get(_id=id)
        monitor.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    #TODO: Enviar mensaje de eliminado
    return redirect("/monitor/todos")