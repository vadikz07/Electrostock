import json
from logica.constants_data import *
from logica.BrowserLogic import validate_url

filepath_json = "data/itemlists.json"

def delete_item(uuid_to_delete:str, appendNew=False, appendData={}):
    print(f'Buscando item {uuid_to_delete}')
    data_to_keep = []
    full_data = getData()
    for d in full_data:
        if d['uuid'] != uuid_to_delete:
            data_to_keep.append(d)
    if not appendNew:
        overwrite_db(data_to_keep)
    else:
        data_to_keep.append(appendData)
    overwrite_db(data_to_keep)

def modify_item(uuid_to_modify:str, new_data:dict):
    #TODO: Completar funcion para modificar objetos
    print(f'Modificando contenidos del objeto {uuid_to_modify}')
    #buscar en el fichero json el UUID del objeto
    item_to_mod = retrieve_item(uuid_to_modify)
    for entry in item_to_mod: #entry es 'uuid' 'nombre' 'modelo' ... etc
        try:
            item_to_mod[entry] = new_data[entry]
            print(f'{entry.upper()} -> Valor actualizado')
        except KeyError:
            print(f'{entry.upper()} -> Valor vacio, no se actualiza')
    delete_item(uuid_to_modify, appendNew=True, appendData=item_to_mod)
    
    
def retrieve_item(uuid_target:str) -> dict:
    full_data = getData()
    for d in full_data:
        if d['uuid'] == uuid_target:
            return d
    return {}
    
def overwrite_db(newdata:list):
    with open(filepath_json, 'w') as json_file:
        json.dump(newdata, json_file)

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
    if datadict["fabricante"] == '':
        b_maker_ok = True
    else:
        b_maker_ok = 3 <= len(datadict["fabricante"]) <= 30
    try:
        b_cantidad_ok = 1 <= int(datadict["cantidad"]) <= 999
    except ValueError:
        b_cantidad_ok = False
    try:
        b_cantidadAviso_ok = 1 <= int(datadict["cantidadAviso"]) <= 999
    except ValueError:
        b_cantidadAviso_ok = False
    try:
        b_cantidadMaxima_ok = 1 <= int(datadict["cantidadMaxima"]) <= 999
    except ValueError:
        b_cantidadMaxima_ok = False

    if datadict["datasheet"] == "":
        b_datasheet_ok = True
    else:
        b_datasheet_ok = validate_url(datadict["datasheet"])

    b_notas_ok = 5 <= len(datadict["notas"]) <= MAX_LEN_NOTES_FULL

    try:
        localizacion_var = int(datadict["localizacion"])
    except ValueError:
        localizacion_var = 0

    b_localizacion_ok = (
        1 <= localizacion_var <= 99 and type(datadict["localizacion"]) == int
    )

    # DEBUG
    print(type(datadict["localizacion"]))
    print(f"nombre {b_nombre_ok}")
    print(f"modelo {b_modelo_ok}")
    print(f"maker {b_maker_ok}")
    print(f"cant {b_cantidad_ok}")
    print(f"cantwarn {b_cantidadAviso_ok}")
    print(f"cantmax {b_cantidadMaxima_ok}")
    print(f"dsheet {b_datasheet_ok}")
    print(f"notas {b_notas_ok}")
    print(f"local {b_localizacion_ok}")

    if (
        b_nombre_ok
        and b_modelo_ok
        and b_maker_ok
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
