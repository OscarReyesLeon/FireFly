from django.shortcuts import render
import os
from os import remove
from django.shortcuts import redirect
from .models import *


# Create your views here.
def preguardarbd(cadenaresult):
    DieselPiusiCar.objects.create(stockinliter = cadenaresult[0], tanklevel = cadenaresult[1], tankporcentage = cadenaresult[2], date = cadenaresult[3], dispenseliters = cadenaresult[4], odometer = cadenaresult[5], presetvolume = cadenaresult[6], vehicleplate = cadenaresult[7], drivername = cadenaresult[8], partnumber = cadenaresult[9], workorder = cadenaresult[10], dispenseridentifier = cadenaresult[11],  time = cadenaresult[12], dispensername = cadenaresult[13])
    
def remplaceclean(separador):
    if separador == "''":
        return "vacio"
    else:
        separador = separador.replace("'","")
        return separador

def separador(lines):
    for line in lines:
        line = line.split(';')
        cadenaresult = []
        reloj = 0
        for separador in line:
            separador2 = remplaceclean(separador)
            # print(separador2 + " - valror individual de cadena")
            reloj = reloj + 1
            # print(reloj)
            cadenaresult.append(separador2)
        # print("================================================================")
        # print('\n'.join(map(str, cadenaresult)))
        # print("================================================================")
        # print(cadenaresult[1])
        preguardarbd(cadenaresult)
        

def leer_piusi(request):
    ubicacion = "/home/piusi/"
    contexto={}
    if request.method=='GET':
        def origenarchivos():
            archivos = os.listdir('/home/piusi/')
            return archivos

        def archivoindividual(totalarchivos):
            for individual in totalarchivos:
                individual = ubicacion+individual

                with open(individual) as f_obj:
                    lines = f_obj.readlines()
                    print(lines)
                    separador(lines)


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
        pass

        totalarchivos = origenarchivos()
        archivoindividual(totalarchivos)
        eliminarleidos(totalarchivos)
    
    return redirect("bases:home")