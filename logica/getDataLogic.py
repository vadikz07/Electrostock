import json
from logica.constants_data import *
from logica.BrowserLogic import validate_url

filepath_json = "data/itemlists.json"


def getData() -> list:
    with open(file="data/itemlists.json", mode="r") as file:
        json_content = json.load(file)
    return json_content


def saveData(datadict_to_insert: dict) -> bool:
    # comprobar si existe el fichero json, si esta, leerlo
    try:
        with open(filepath_json, "r") as file:
            contents = json.load(file)
    except FileNotFoundError:
        contents = {}

    # actualizar variable contents con datadict_to_insert
    contents.append(datadict_to_insert)

    # guardar datos en json actual
    try:
        with open(filepath_json, "w") as json_file:
            json.dump(contents, json_file)
        print(f"Datos insertados en {filepath_json}")
        return True
    except Exception:
        print(f"Ha habido un error.")
        return False


def validateData(datadict: dict):
    b_nombre_ok = 3 <= len(datadict["nombre"]) <= 30
    b_modelo_ok = 3 <= len(datadict["modelo"]) <= 30
    b_cantidad_ok = (
        1 <= int(datadict["cantidad"]) <= 999 and type(datadict["cantidad"]) == int
    )
    b_cantidadAviso_ok = (
        1 <= int(datadict["cantidadAviso"]) <= 999
        and type(datadict["cantidadAviso"]) == int
    )
    b_cantidadMaxima_ok = (
        1 <= int(datadict["cantidadMaxima"]) <= 999
        and type(datadict["cantidadMaxima"]) == int
    )
    b_datasheet_ok = validate_url(datadict["datasheet"])
    b_notas_ok = 5 <= len(datadict["notas"]) <= MAX_LEN_NOTES_FULL
    b_localizacion_ok = (
        1 <= int(datadict["localizacion"]) <= 99
        and type(datadict["localizacion"]) == int
    )

    # # DEBUG
    # print(type(datadict["localizacion"]))
    # print(f"nombre {b_nombre_ok}")
    # print(f"modelo {b_modelo_ok}")
    # print(f"cant {b_cantidad_ok}")
    # print(f"cantwarn {b_cantidadAviso_ok}")
    # print(f"cantmax {b_cantidadMaxima_ok}")
    # print(f"dsheet {b_datasheet_ok}")
    # print(f"notas {b_notas_ok}")
    # print(f"local {b_localizacion_ok}")

    if (
        b_nombre_ok
        and b_modelo_ok
        and b_cantidad_ok
        and b_cantidadAviso_ok
        and b_cantidadMaxima_ok
        and b_datasheet_ok
        and b_notas_ok
        and b_localizacion_ok
    ):
        print("datos validos")
        return True
    else:
        print("datos no son validos")
        return False
