from django.shortcuts import render, HttpResponse
from .forms import ClientesForm
from pyrebase import pyrebase
from django.contrib import auth


config ={

'apiKey': "AIzaSyBpy-7yVY4Nmgt26R-R7i_b7pgQDSo73kE",
    'authDomain': "gaslp-842a6.firebaseapp.com",
    'databaseURL': "https://gaslp-842a6.firebaseio.com",
    'projectId': "gaslp-842a6",
    'storageBucket': "",
    'messagingSenderId': "429233000110",
    'appId': "1:429233000110:web:fbaf86f7f00c501b91a73f"
}

firebase = pyrebase.initialize_app(config) 
auth = firebase.auth()


def login(request):
    return render(request, "core/login.html")


def visitas(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "Credenciales invalidas"
        return render(request,"core/login.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "core/visitas.html",{"e":email})

def visitas2(request):
    return render(request, "core/visitas.html")


def clientes(request):
    cliente_form = ClientesForm()
    return render(request, "core/clientes.html", {'form': cliente_form})

def compras(request):
    return render(request, "core/compras.html")


def ventas(request):
    return render(request, "core/ventas.html")

def reportes(request):
    return render(request, "core/reportes.html")


