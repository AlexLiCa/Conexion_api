
import requests

url = "http://127.0.0.1:5000//api/tasks"

def show_task():
    try:
        response = requests.get(url)
        return response.json()['tasks']
    except requests.exceptions.HTTPError as err:
        print("Error")
        raise SystemExit(err)
    except requests.exceptions.ChunkedEncodingError as err:
        print(f"---Error:   {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"---JSON CODE ERROR:   {err}")


def create_task(tarea):
    try:
        response = requests.post(url, json={"name": tarea})
        print(response)
    except requests.exceptions.HTTPError as err:
        print("error")
        raise SystemExit(err)
    except:
        print("error")



while salida:
    print(""
    "1<-- Mostrar Tareas\n"
    "2<-- Agregar tareas\n"
    "3<-- Salir\n"
    "")
    try:
        opc = int(input("Eliga una opcion: "))
    except ValueError as e:
        opc = 0
    if opc == 1:
        data = show_task()
        for task in data:
            print(task)
    if opc == 2:
        data = create_task(input("Ingresa la tarea:\n"))
        for task in data:
            print(task)
    if opc == 3:
        salida = False
        print("adios =)")
    else:
        print("no es una opcion")


