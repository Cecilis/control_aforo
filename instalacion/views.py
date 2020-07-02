# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from djongo import models
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.translation import activate
from instalacion.forms import InstalacionForm
from instalacion.models import Instalacion


@login_required(login_url="/login/")
def instalacion(request):
    activate('es')
    if request.method == "POST":
        form = InstalacionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/instalacion/todos')
            except:
                pass
    else:
        form = InstalacionForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                #print(field.name % " | " % error)

                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'instalacion/agregar.html', {'form': form})



@login_required(login_url="/login/")
def todos(request):
    activate('es')
    instalaciones = Instalacion.objects.all()
    for instalacion in instalaciones:
        instalacion.id = str(instalacion._id)
    return render(request, "instalacion/todos.html", {'instalaciones': instalaciones})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    instalacion = get_object_or_404(Instalacion, _id=id)
    form = InstalacionForm(request.POST or None, instance=instalacion)
    return render(request, 'instalacion/editar.html', { 'form' : form })



@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    instalacion = get_object_or_404(Instalacion, _id=id)
    form = InstalacionForm(request.POST or None, instance=instalacion)
    print(form.__dict__)
    if form.is_valid():
        form.save()
        return redirect("/instalacion/todos")
    return render(request, 'instalacion/editar.html', { 'form' : form })


@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    try:
        instalacion = Instalacion.objects.get(_id=id)
        instalacion.delete()
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return redirect("/instalacion/todos")