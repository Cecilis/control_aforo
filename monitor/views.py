from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

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
def monitor_fs(request):
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