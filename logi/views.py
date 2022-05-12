from django.shortcuts import render
import os
from os import remove
from django.shortcuts import redirect


# Create your views here.
def leer_piusi(request):
    ubicacion = "/mnt/c/Users/danon/Downloads/archivo/piusi/"
    contexto={}
    if request.method=='GET':
        def origenarchivos():
            archivos = os.listdir('/mnt/c/Users/danon/Downloads/archivo/piusi/')
            return archivos

        def archivoindividual(totalarchivos):
            for individual in totalarchivos:
                individual = ubicacion+individual

                with open(individual) as f_obj:
                    lines = f_obj.readlines()
                    for line in lines:
                        line = line.split(';')
                        for separador in line:
                            separador = separador.replace("'","")
                            print(separador + " - valror individual de cadena")

        def eliminarleidos(totalarchivos):
            for individual in totalarchivos:
                individual = ubicacion+individual
                print(individual)
                """remove(individual)"""
                print(individual + " - removeOK")

        totalarchivos = origenarchivos()
        archivoindividual(totalarchivos)
        eliminarleidos(totalarchivos)

    if request.method=='POST':
        def origenarchivos():
            archivos = os.listdir('/mnt/c/Users/danon/Downloads/archivo/piusi/')
            return archivos

        def archivoindividual(totalarchivos):
            for individual in totalarchivos:
                individual = ubicacion+individual
                """print(individual)"""

                with open(individual) as f_obj:
                    lines = f_obj.readlines()
                    for line in lines:
                        line = line.split(';')
                        for separador in line:
                            separador = separador.replace("'","")
                            print(separador + " - valror individual de cadena")

        def eliminarleidos(totalarchivos):
            for individual in totalarchivos:
                individual = ubicacion+individual
                print(individual)
                remove(individual)
                print(individual + " - removeOK")

        totalarchivos = origenarchivos()
        archivoindividual(totalarchivos)
        eliminarleidos(totalarchivos)
    
    return redirect("bases:home")