import json

filepath_json = 'data/itemlists.json'

def getData() -> list:
    with open(file='data/itemlists.json', mode='r') as file:
        json_content = json.load(file)
    return json_content
        
def saveData(datadict_to_insert:dict):
    #comprobar si existe el fichero json, si esta, leerlo
    try:
        with open(filepath_json, 'r') as file:
            contents = json.load(file)
    except FileNotFoundError:
        contents = {}
    
    #actualizar variable contents con datadict_to_insert
    contents.append(datadict_to_insert)

    #guardar datos en json actual
    try:
        with open(filepath_json, 'w') as json_file:
            json.dump(contents, json_file)
        print(f'Datos insertados en {filepath_json}')
    except Exception:
        print(f'Ha habido un error.')