from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import activate

from instalacion.forms import InstalacionForm, InstalacionAddForm
from instalacion.models import Instalacion


@login_required(login_url="/login/")
def instalacion(request):
    if request.method == "POST":
        form = InstalacionAddForm(request.POST)
        if form.is_valid():
            try:
                instalacion = form.save()
                return redirect('/instalacion/editar/' + str(instalacion.id) + '/')

            except Exception as e:
                print('%s (%s)' % (e, type(e)))
                pass
    else:
        form = InstalacionAddForm()
        # for field in form:
        #     if field.name == 'monitor':
        #         print(field)
        #     else:
        #         print(field.name)
    if form.errors:
        print('Errores en nt mo')
        for field in form:
            for error in field.errors:
                print(field.name)
                print(" | ")
                print(error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'instalacion/agregar.html', {'instalacion': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    instalaciones = Instalacion.objects.all()
    return render(request, "instalacion/todos.html", {'instalaciones': instalaciones})



@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    instalacion = Instalacion.objects.get(id=id)
    try:
        form = InstalacionForm(instance=instalacion)
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return render(request, 'instalacion/editar.html', {'instalacion': form})


@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    print('one')
    instalacion = Instalacion.objects.get(id=id)
    try:
        form = InstalacionForm(request.POST, instance=instalacion)
        if form.is_valid():
            form.save()
            return redirect("/instalacion/todos")
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    if form.errors:
        print('Errores en nt mo')
        for field in form:
            for error in field.errors:
                print(field.name)
                print(" | ")
                print(error)
    return render(request, 'instalacion/editar.html', {'instalacion': form})


@login_required(login_url="/login/")
def eliminar(request, id=None):
    activate('es')
    instalacion = Instalacion.objects.get(id=id)
    instalacion.delete()
    return redirect("/instalacion/todos")
