from operaciones import *
from os import system
import sys

if __name__ == '__main__':
    try:
        obj = Operaciones()
        while True:
            print('-------------Menu-----------------')
            print('------ 1. Crear Persona ----------')
            print('------ 2. Actualizar Persona -----')
            print('------ 3. Eliminar Persona -------')
            print('------ 4. Leer Personas ----------')
            print('------ 5. Salir ------------------')
            print('\n')
            op = input('Elija una opcion: ')
            if op == '1': #create
                system("cls")
                nombre = input('Ingrese Nombre: ')
                edad = input('Ingrese Edad: ')
                telefono = input('Ingrese Telefono: ')
                casado = input('Ingrese si esta casado (SI = 1, NO = 0): ')
                val = obj.Validaciones(nombre, edad, telefono, casado)
                if val:
                    opc = obj.CreatePersona(nombre, int(edad), int(telefono), bool(casado))
                    if opc :
                        print('Se a creado la Persona Satisfactoriamente...')
                        input('Presione una tecla para continuar...')
                    else:
                        print('Ha ocurrido un error al crear la Persona')
                        input('Presione una tecla para continuar...')
                else:
                    print('Porfavor, Ingrese datos validos...')
                    input('Presione una tecla para continuar...')
                system("cls")
                continue
            elif op == '2':#update
                system("cls")
                obj.PrintPersonas()
                nombre = input('Ingrese Nombre: ')
                edad = input('Ingrese Edad: ')
                telefono = input('Ingrese Telefono: ')
                casado = input('Ingrese si esta casado (SI = 1, NO = 0): ')
                val = obj.Validaciones(nombre, edad, telefono, casado)
                if val:
                    opc = obj.UpdatePersona(nombre, int(edad), int(telefono), bool(casado))
                    if opc :
                        print('Se actualizo la Persona correctamente.')
                        input('Presione una tecla para continuar...')
                    else:
                        print('Ha ocurrido un error al actualizar, Revise si el nombre de la persona a actualizar exista.')
                        input('Presione una tecla para continuar...')
                else:
                    print('Porfavor, Ingrese datos validos...')
                    input('Presione una tecla para continuar...')
                system("cls")
                continue
            elif op == '3':#delete
                system("cls")
                obj.PrintPersonas()
                nombre = input('Ingrese el Nombre de la Persona a Eliminar: ')
                opc = obj.DeletePersona(nombre)
                if opc:
                    print('Se Elimino la Persona correctamente.')
                    input('Presione una tecla para continuar...')
                else:
                    print('Ha ocurrido un error al Eliminar la Persona. Asegurase que la Persona Exista...')
                    input('Presione una tecla para continuar...')
                system("cls")
                continue
            elif op == '4':#read
                system("cls")
                obj.PrintPersonas()
                print('\n')
                input('Presione una tecla para continuar...')
                system("cls")
                continue
            elif op == '5':
                print('Saliendo del Programa...')
                sys.exit()
                break
            else:
                print('No se encontro opcion, Ingrese un dato valido...')
                input('Presione una tecla para continuar...')
                system("cls")
    except Exception as e:
        print(str(e))