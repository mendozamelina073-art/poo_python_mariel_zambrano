"""
Programa: Aplicación de Conceptos de POO en Python
Autor: Mariel Zambrano
Descripción:
Este programa aplica los conceptos de Programación Orientada a Objetos:
- Definición de Clase
- Definición de Objeto
- Herencia
- Encapsulación
- Polimorfismo
"""

# ==============================
# Clase base
# ==============================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # Atributo público
        self.__edad = edad        # Atributo privado (Encapsulación)

    # Getter de edad
    def get_edad(self):
        return self.__edad

    # Setter de edad
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser mayor que cero")

    # Método para demostrar polimorfismo
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.__edad}"


# ==============================
# Clase derivada (Herencia)
# ==============================
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método sobrescrito (Polimorfismo)
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.get_edad()}, Carrera: {self.carrera}"


# ==============================
# Programa principal
# ==============================
if __name__ == "__main__":
    # Creación de objetos
    persona = Persona("Carlos", 35)
    estudiante = Estudiante("Mariel", 20, "Tecnologías de la Información")

    # Uso de métodos
    print(persona.mostrar_informacion())
    print(estudiante.mostrar_informacion())

    # Encapsulación en acción
    estudiante.set_edad(21)
    print("Edad actualizada del estudiante:", estudiante.get_edad())

