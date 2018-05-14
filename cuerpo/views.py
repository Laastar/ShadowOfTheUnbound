from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from datetime import time, datetime
from django.contrib import messages, sessions
from cuerpo.models import User, Opiniones, Producto, Cita
from cuerpo.forms import SignUpForm, LoginForm, CitasForm, OpinionForm, RecuperarForm

# Create your views here. Ba

def index(request):
    return render(request, 'cuerpo/index.html', {})


def servicios(request):
    return render(request, 'cuerpo/servicios.html', {})


def manicura(request):
    return render(request, 'cuerpo/manicura.html', {})


def manicura_conv(request):
    return render(request, 'cuerpo/manicura_convencional.html', {})


def tratamiento(request):
    return render(request, 'cuerpo/tratamiento.html', {})


def extensiones(request):
    return render(request, 'cuerpo/extensiones.html', {})


def cortes(request):
    return render(request, 'cuerpo/cortes.html', {})


def tintes(request):
    return render(request, 'cuerpo/tintes.html', {})


def pedicure(request):
    return render(request, 'cuerpo/pedicure.html', {})


def depilaciones(request):
    return render(request, 'cuerpo/depilaciones.html', {})


def menuproductos(request):
    return render(request, 'cuerpo/menuproductos.html', {})


def cabello(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/cabello.html', {'productos' : productos})


def perfumes(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/perfumes.html', {'productos' : productos})


def lociones(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/lociones.html', {'productos' : productos})


def cuidado(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/cuidado.html', {'productos' : productos})


def barnices(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/barnices.html', {'productos' : productos})


def maquillaje(request):
    productos = Producto.objects.all()
    return render(request, 'cuerpo/maquillaje.html', {'productos' : productos})


def vercitas(request):
    usuario = request.session.get('USUARIO_LOGEADO')
    if not usuario or usuario == "":
        messages.info(request, 'Inicia sesión')
        form = CitasForm()
        return render(request, 'cuerpo/citas.html', {'form': form})
    else:
        try:
            citas = Cita.objects.filter(username=usuario)
            return render(request, 'cuerpo/vercitas.html', {'citas': citas})
        except User.DoesNotExist:
            messages.info(request, 'Información errónea')


def unete(request):
    return render(request, 'cuerpo/unete.html', {})


def opiniones(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.save()
            return redirect('opiniones')
    else:
        form = OpinionForm()
    return render(request, 'cuerpo/opiniones.html', {'form' : form})


def contacto(request):
    return render(request, 'cuerpo/contacto.html', {})


def tips(request):
    return render(request, 'cuerpo/tips.html', {})


def recuperar(request):
    if request.method == 'POST':
        form = RecuperarForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                usuario = User.objects.get(email=user.email)
                passwd = usuario.password1
                correo = usuario.email
                email = EmailMessage('Recuperacion de contraseña', 'Contraseña: ' + passwd, to=[correo])
                email.send()
                return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Infromación errónea')
                redirect('login')
    else:
        form = RecuperarForm()
    return render(request, 'cuerpo/recuperacion.html', {'form': form})


def cerrar(request):
        request.session['USUARIO_LOGEADO'] = ""
        messages.info(request, 'Se ha cerrado la sesion')
        return redirect('login')


def login(request):
    USUARIO_LOGEADO = request.session.get('USUARIO_LOGEADO')
    if not USUARIO_LOGEADO:
        request.session['USUARIO_LOGEADO'] = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            try:
                usuario = User.objects.get(username=user.username)
                if (USUARIO_LOGEADO != ""):
                    messages.info(request, 'Usuario ya esta logeado')
                elif (user.password != usuario.password1):
                    messages.info(request, 'Informacion erronea')
                else:
                    request.session['USUARIO_LOGEADO'] = user.username
                    messages.info(request, 'Bienvenid@ ' + user.username)
                    return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Infromación errónea')
                redirect('login')
    else:
        form = LoginForm()
    return render(request, 'cuerpo/login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            if(user.password1 != user.password2):
                messages.info(request, 'Contraseñas no concuerdan.')
            else:
                user.save()
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'cuerpo/registro.html', {'form': form})


def citas(request):
    usuario = request.session.get('USUARIO_LOGEADO')
    if not usuario or usuario == "":
        messages.info(request, 'Inicia sesión')
        redirect('login')
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=usuario)
                instance = form.save()
                instance.username = user.username
                instance.email = user.email
                if(instance.hora > time(19,00)):
                    messages.info(request, 'Información errónea')
                elif(instance.hora < time(9,00)):
                    messages.info(request, 'Información errónea')
                else:
                    instance.save()
                    messages.info(request, usuario + " ya se agendó tu cita")
                    return render(request, 'cuerpo/index.html', {})
            except User.DoesNotExist:
                messages.info(request, 'Información errónea')
    else:
        form = CitasForm()
    return render(request, 'cuerpo/citas.html', {'form': form})
