# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GQ74F8cm_JrNTLb_aIe_ufOZkLl9TQpS
"""

import numpy as np
import datetime

precios = {'PLATINUM':120.000, 'GOLD': 80.000, 'SILVER': 50.000}
asientos = np.zeros((11, 11), dtype=object)

compradores = {}

def mostrar_menu():
  print("----- CONCIERTO VIP MICHAEL JAM -----")
  print("1. Comprar Entradas")
  print("2. Ver listado de asistentes")
  print("3. Mostrar ganancias totales")
  print("4. Salir")

def comprar_entradas():
    entrada = int(input("Ingrese el número de la entrada (1-100"))
    asientos = input("Ingrese el tipo de entrada (PLATINUM, GOLD, SILVER)").upper()

    if entrada < 1 or entrada > 100 or tipo not in precios:
        print("Opción inválida. Intente nuevamente.")
        return

    fila = 10 - entrada

    columna = ord(entrada)

    if entrada[fila, columna] != 0:
        print("La entrada seleccionada no está disponible.")
        return

    run = input("Ingrese el RUN del comprador (sin guion ni puntos): ")

    if run in compradores:
        print("El RUN ingresado ya ha realizado una compra.")
        return

    entrada[fila, columna] = 'X'
    compradores[run] = asientos

    print("Operación realizada correctamente.")

def mostrar_asientos_disponibles():