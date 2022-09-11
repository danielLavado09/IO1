# Se importa libreria para acceder y autorizar acceso al API de Google.
from google.oauth2.service_account import Credentials

# Se importa la libreria Gspread.
import gspread

# Configuración inicial de Gspread.
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'clave.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
sh = gc.open("gspread_io1")

hojaEstudiantes = sh.worksheet("Estudiantes")
hojaNotas = sh.worksheet("Notas")


def agregarEstudiante():
    while True:
        print("=======||||AGREGAR ESTUDIANTE||||=======")
        print("Ingrese el nombre del estudiante: ", end="")
        nombre = str(input())
        print("Ingrese el apellido del estudiante: ", end="")
        apellido = str(input())
        print("Ingrese el correo del estudiante: ", end="")
        correo = str(input())
        print("Ingrese el promedio del estudiante: ", end="")
        promedio = int(input())

        if verificarCorreo(correo):
            # Array con los datos.
            datos = [nombre, apellido, correo, promedio]
            print("Estudiante agregado.")

            # Se insertan los datos en la hoja de cálculo.
            hojaEstudiantes.append_row(datos)
        else:
            print("El estudiante ya se encuentra registrado.")

        print('Desea agregar mas estudiantes? (si, no): ', end="")
        option = str(input())

        if option == 'no':
            break


def verificarCorreo(correo):
    # Con el método find() se encuentra la celda deseada.
    if hojaEstudiantes.find(correo) == None:
        return True
    else:
        return False


def eliminarEstudiante():
    while True:
        print("=======||||ELIMINAR ESTUDIANTE||||=======")
        print("Ingrese el correo del estudiante a eliminar: ", end="")
        nombre = str(input())
        try:
            # Haciendo uso del objeto celda, se elimina el registro.
            cell = hojaEstudiantes.find(nombre)
            hojaEstudiantes.delete_rows(cell.row)
            hojaNotas.delete_rows(cell.row)

            print("Estudiante eliminado.")
            
        except AttributeError:
            print("No existe el correo ingresado.")

        print('Desea eliminar mas estudiantes? (si, no): ', end="")
        option = str(input())

        if option == 'no':
            break


def imprimirEstudiantes():
    print("=======||||REGISTROS||||=======")
    print("Lista de Diccionarios")
    print(hojaEstudiantes.get_all_records())
    print("Lista de Listas")
    print(hojaEstudiantes.get_all_values())

    # Haciendo uso del método .get_all_values() se imprimen los correos registrados.
    print("=======||||CORREOS REGISTRADOS||||=======")
    for i in range(1, len(hojaEstudiantes.get_all_values())):
        print("Correo: " + hojaEstudiantes.get_all_values()[i][2])


def enviarNotas():
    promedio = 0
    numeroDeDatos = len(hojaEstudiantes.col_values(4))

    # Dando estilo con el método .format().
    hojaNotas.format('A1:B100', {'textFormat': {'bold': True}})

    for i in range(1, numeroDeDatos):
    
        # Insertando celdas con el método .update_cell().
        hojaNotas.update_cell(i + 1, 1, hojaEstudiantes.col_values(4)[i])
        promedio += int(hojaEstudiantes.col_values(4)[i])

    promedio = promedio / (numeroDeDatos - 1)

    hojaNotas.update_cell(2, 2, promedio)
    print("=======||||NOTAS ENVIADAS||||=======")
    print("Revisar la hoja de Notas.")


def menu():
    # Menú de opciones.
    
    while True:
        print("=======||||ADMINISTRAR ESTUDIANTES||||=======")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Leer")
        print("4. Enviar notas")
        print("5. Salir")
        print("Seleccione opcion: ", end="")
        opcion = int(input())

        if opcion == 1:
            agregarEstudiante()
        elif opcion == 2:
            eliminarEstudiante()
        elif opcion == 3:
            imprimirEstudiantes()
        elif opcion == 4:
            enviarNotas()
        elif opcion == 5:
            break
        else:
            print("Opcion invalida, intente nuevamente")


menu()