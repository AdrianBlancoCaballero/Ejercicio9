
class Car:

    def __init__(self, marca, modelo, combustible, cilindrada, wheel):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.wheel = wheel
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_incr(self, x, y):
        self.pos_x = self.pos_x + x
        self.pos_y += y

    def get_pos(self):
        return self.pos_x, self.pos_y


class Wheel:

    def __init__(self, ancho, rodadura, diametro):
        self.ancho = ancho
        self.rodadura = rodadura
        self.diametro = diametro
        self.presion = 0

    def set_pressure(self, presion):
        self.presion = presion

    def print_info(self):
        ret = "Dimensiones de la rueda: " + self.ancho + "/" + self.rodadura + "R" + self.diametro + "\n" + \
               "Presión de los neumáticos: " + self.presion + "bar"
        return ret