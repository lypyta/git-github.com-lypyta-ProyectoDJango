from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('',views.contacto,name="contacto"),
    path('',views.nosotros,name="nosotros"),
    path('',views.reg,name="reg"),
    path('',views.registro,name="registro"),
    path('',views.servicios,name="servicios"),
]
