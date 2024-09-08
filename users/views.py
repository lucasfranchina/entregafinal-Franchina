from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import ProfileForm
from .models import Profile


def login_request(request):
    
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return render(request, 'appventas/padre.html')

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'appventas/padre.html')
            
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

def custom_logout(request):
    logout(request)
    return redirect('inicio')

def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            
            request.user.email = form.cleaned_data['email']
            request.user.save()
            profile.save()
            return redirect('inicio')
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, 'users/editar_usuario.html', {'form': form})

# def editar_perfil(request):
#     usuario = request.user

#     if request.method == 'POST':
#         miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
#         if miFormulario.is_valid():
#             if miFormulario.cleaned_data.get('imagen'):
#                 if Imagen.objects.filter(user=usuario).exists():
#                     usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
#                     usuario.imagen.save()
#                 else:
#                     avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
#                     avatar.save()
#             miFormulario.save()

#             return render(request, 'appventas/padre.html')
#     else:
#         miFormulario = UserEditForm(instance=usuario)
    
#     return render(request, 'users/editar_usuario.html', {"mi_form": miFormulario, "usuario": usuario})