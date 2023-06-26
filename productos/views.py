from django.shortcuts import render

# Create your views here.
def home(resquest):
    return render(resquest,'productos/home.html')
def contacto(resquest):
    return render(resquest,'productos/contacto.html')
def nosotros(resquest):
    return render(resquest,'productos/nosotros.html')
def reg(resquest):
    return render(resquest,'productos/reg.html')
def registro(resquest):
    return render(resquest,'productos/registro.html')
def servicios(resquest):
    return render(resquest,'productos/servicios.html')