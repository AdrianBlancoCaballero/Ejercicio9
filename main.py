# Ejercicio 9

import persistencia_pickle as pp
import car_class
import random as rd

FILE = "coches_obj.txt"
lista = pp.retrieve(FILE)
if lista == None:
    lista = []


while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    ancho = input("Ancho del neumático: ")
    rodadura = input("Perfil del neumático: ")
    diametro = input("Diametro de llanta: ")

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    coche = car_class.Car(marca, modelo, combustible, cilindrada, wheel)

    coche.wheel.set_pressure(input("Presión de los neumáticos (en bar): "))

    lista.append(coche)

    coche.move_to(rd.random()*100, rd.random()*600)
    print("Posición: ", coche.get_pos())
    coche.move_incr(rd.random()*10, rd.random()*60)
    print("Posición: ", coche.get_pos())

    del (coche)
    del (wheel)


pp.store(lista, FILE)
lista = []
print(lista)
lista = pp.retrieve(FILE)


for car in lista:
    print("Marca: ", car.marca)
    print("Modelo: ", car.modelo)
    print("Combustible: ", car.combustible)
    print("Cilindrada: ", car.cilindrada)
    print(car.wheel.print_info())
    print("Posición: ", car.get_pos(), "\n")