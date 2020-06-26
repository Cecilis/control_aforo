from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import activate
from cliente.forms import ClienteForm
from cliente.models import Cliente


#TODO: ELIMINAR: Está solo de referencia de los estilos, no incluir en la versión final
def mng(request):
    context = {'foo': 'bar'}
    return render(request, 'cliente/manage.html', context)


@login_required(login_url="/login/")
def cliente(request):
    activate('es')
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cliente/todos')
            except:
                pass
    else:
        form = ClienteForm()
    if form.errors:
        for field in form:
            for error in field.errors:
                print(field.name % " | " % error)
        # for error in form.non_field_errors:
        #     print('NFE | ')
        #     print(error)
    return render(request, 'cliente/agregar.html', {'cliente': form})


@login_required(login_url="/login/")
def todos(request):
    activate('es')
    #TODO: Bad Request
    clientes = Cliente.objects.all()
    return render(request, "cliente/todos.html", {'clientes': clientes})


@login_required(login_url="/login/")
def editar(request, id):
    activate('es')
    #TODO: Ajustar el try
    cliente = Cliente.objects.get(id=id)
    try:
        form = ClienteForm(instance=cliente)
    except Exception as e:
        print('%s (%s)' % (e, type(e)))
        pass
    return render(request, 'cliente/editar.html', {'cliente': form})

@login_required(login_url="/login/")
def actualizar(request, id):
    activate('es')
    #TODO: Ajustar Try, falta cao bad request
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect("/cliente/todos")
    return render(request, 'cliente/editar.html', {'cliente': form})

@login_required(login_url="/login/")
def eliminar(request, id):
    activate('es')
    #TODO: Enviar confirmación de eliminación
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("/cliente/todos")