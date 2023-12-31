import json
from logica.constants_data import *
from logica.BrowserLogic import validate_url
from interfaz.componentes.warning import WarningWindow

filepath_json = "data/itemlists.json"

def delete_item(uuid_to_delete:str, appendNew=False, appendData={}, par=None, popmanagerRef=None, wrnMessage='¿Seguro que quieres borrar esta entrada?'):
    answer = WarningWindow(par=par,msg=wrnMessage).return_response()
    if answer:    
        print(f'Buscando item {uuid_to_delete}')
        data_to_keep = []
        #FIXME: Sustituir por popmanager.allitems
        full_data = popmanagerRef.all_items
        for d in full_data:
            if d['uuid'] != uuid_to_delete:
                data_to_keep.append(d)
        if not appendNew:
            overwrite_db(data_to_keep)
        else:
            data_to_keep.append(appendData)
        overwrite_db(data_to_keep)
    

def modify_item(uuid_to_modify:str, new_data:dict, popmanagerRef=None):
    print(f'Modificando contenidos del objeto {uuid_to_modify}')
    #buscar en el fichero json el UUID del objeto
    item_to_mod = popmanagerRef.retrieve_item(uuid_to_modify)
    for entry in item_to_mod: #entry es 'uuid' 'nombre' 'modelo' ... etc
        try:
            item_to_mod[entry] = new_data[entry]
            print(f'{entry.upper()} -> Valor actualizado')
        except KeyError:
            print(f'{entry.upper()} -> Valor vacio, no se actualiza')
    delete_item(uuid_to_modify, appendNew=True, appendData=item_to_mod,wrnMessage='¿Quieres actualizar los datos?', popmanagerRef=popmanagerRef)
    
    
def overwrite_db(newdata:list):
    with open(filepath_json, 'w') as json_file:
        json.dump(newdata, json_file)

def getData() -> list:
    print('Cargando datos del fichero JSON')
    with open(file="data/itemlists.json", mode="r") as file:
        json_content = json.load(file)
    return json_content


def saveData(datadict_to_insert: dict, popmanagerRef=None) -> bool:
    # comprobar si existe el fichero json, si esta, leerlo
    popmanagerRef.all_items.append(datadict_to_insert)
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
        b_maker_ok = 3 <= len(datadict["fabricante"]) <= 15
    try:
        b_cantidad_ok = 1 <= int(datadict["cantidad"]) <= 999
    except ValueError:
        b_cantidad_ok = False
    try:
        b_cantidadAviso_ok = 0 <= int(datadict["cantidadAviso"]) <= 999
    except ValueError:
        b_cantidadAviso_ok = False

    if datadict["datasheet"] == "":
        b_datasheet_ok = True
    else:
        b_datasheet_ok = validate_url(datadict["datasheet"])

    b_notas_ok = 5 <= len(datadict["notas"]) <= MAX_LEN_NOTES_FULL or datadict['notas'] == ''

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
    print(f"dsheet {b_datasheet_ok}")
    print(f"notas {b_notas_ok}")
    print(f"local {b_localizacion_ok}")

    if (
        b_nombre_ok
        and b_modelo_ok
        and b_maker_ok
        and b_cantidad_ok
        and b_cantidadAviso_ok
        and b_datasheet_ok
        and b_notas_ok
        and b_localizacion_ok
    ):
        print("datos validos")
        return True
    else:
        print("datos no son validos")
        return False

def get_container_size(num): 
    # tuples => minimo maximo
    xxl = (1,8) 
    l = (9,32)
    m = (33,50)
    s = (51,99)
    match num:
        case num if xxl[0]<= num <= xxl[1]:
            return "XL"
        case num if l[0]<= num <= l[1]:
            return "GRANDE"
        case num if m[0]<= num <= m[1]:
            return "MEDIANO"
        case num if s[0]<= num <= s[1]:
            return "PEQUEÑO"
        case _:
            return "INPUT NO VALIDO"