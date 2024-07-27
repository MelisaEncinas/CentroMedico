from datetime import datetime

class Paciente:
    def __init__(self, nombre, edad, id_paciente):
        self.nombre = nombre
        self.edad = edad
        self.id_paciente = id_paciente

    def __str__(self):
        return (f"- Nombre: {self.nombre} ,- Edad: {self.edad}, - ID: {self.id_paciente}")
    


class Cita:
    def __init__(self, paciente, medico, fecha, hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (f"- Paciente: {self.paciente} ,- Médico: {self.medico}, - Fecha: {self.fecha} ,- Hora: {self.hora}")


class CentroMedico:
    def __init__(self):
        self.pacientes = {}
        self.citas = []

    def registrar_paciente(self, nombre, edad, id_paciente):
        if id_paciente in self.pacientes:
            print("Error: El paciente con este ID ya existe.")
        else:
            self.pacientes[id_paciente] = Paciente(nombre, edad, id_paciente)
            print("Paciente registrado exitosamente.")

    def programar_cita(self, id_paciente, medico, fecha, hora):
        paciente = self.pacientes.get(id_paciente)
        if paciente is None:
            print("Error: Paciente no encontrado.")
        else:
            nueva_cita = Cita(paciente, medico, fecha, hora)
            self.citas.append(nueva_cita)
            print("Cita programada exitosamente.")

    def ver_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in self.pacientes.values():
                print(paciente)

    def ver_citas(self):
        if not self.citas:
            print("No hay citas programadas.")
        else:
            for cita in self.citas:
                print(cita)

    def cancelar_cita(self, id_paciente, fecha, hora):
        for cita in self.citas:
            if (cita.paciente.id_paciente == id_paciente and cita.fecha == fecha and cita.hora == hora):
                self.citas.remove(cita)
                print("Cita cancelada exitosamente.")
                return
        print("Error: Cita no encontrada.")

def mostrar_menu():
    print("Bienvenido al Centro de Gestiones ")
    print("\n--- Menu ---")
    print("1. Registrar nuevo paciente")
    print("2. Programar nueva cita")
    print("3. Ver todos los pacientes")
    print("4. Ver todas las citas")
    print("5. Cancelar una cita")
    print("6. Salir")

def procesar_seleccion(centro_medico):
    while True:
        mostrar_menu()
        seleccion = input("Selecciona una opción: ")

        if seleccion == '1':
            print("--Registro de Paciente--")
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            id_paciente = input("Número de identificación : ")
            centro_medico.registrar_paciente(nombre, edad, id_paciente)

        elif seleccion == '2':
            print("--Registro de Citas Medicas--")
            id_paciente = input("Número de identificación : ")
            medico = input("Nombre del médico: ")
            fecha = input("Fecha de la cita (DD-MM-AAAA): ")
            hora = input("Hora de la cita (HH:MM): ")
            centro_medico.programar_cita(id_paciente, medico, fecha, hora)

        elif seleccion == '3':
            print("--Lista de Pacientes--")
            centro_medico.ver_pacientes()

        elif seleccion == '4':
            print("-- lista de citas")
            centro_medico.ver_citas()

        elif seleccion == '5':
            print("--Cancelar cita medica--")
            id_paciente = input("Número de identificación : ")
            fecha = input("Fecha de la cita (DD-MM-AAAA): ")
            hora = input("Hora de la cita (HH:MM): ")
            centro_medico.cancelar_cita(id_paciente, fecha, hora)

        elif seleccion == '6':
            print("Saliendo. Hasta Luego")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

def main():
    centro_medico = CentroMedico()
    procesar_seleccion(centro_medico)

if __name__ == "__main__":
    main()
