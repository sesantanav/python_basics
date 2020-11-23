# Programación Orientada o Objetos con Python

# Clases

class NuevaClase:
    pass

class Persona:

    def __init__(self):
        self._nombre = ""
        self._edad = 0

    # Metódods de la clase
    # setters
    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    # getters
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getInfo(self):
        print("Nombre : " + self._nombre )
        print("Edad : {e}".format(e=self._edad))

class Estudiante(Persona):
    
    def __init__(self):
        Persona.__init__(self)
        self.carrera = ""

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCarrera(self):
        return self.carrera

    def infoEstudiante(self):
        print("El nombre del estudiante es: " + self.getNombre() )
        print("La edad del estudiante es: " + self.getEdad())
        print("La carrera del estudiante es: " + self.carrera)


persona = Persona()

persona.setEdad(25)
persona.setNombre("Gonzalo")

print("El nombre es: " + persona.getNombre())

nombre = persona.getNombre()
print("Otra forma de obtener el nombre: " + nombre)
print("Nombre de la persona es {n}".format(n=nombre))

estudiante = Estudiante()
estudiante.setNombre("Favio")
estudiante.setEdad(25)
estudiante.getInfo()
estudiante.infoEstudiante()

