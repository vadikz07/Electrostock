from data.itemlists import items
import ast

class InsertionManager:
    props_query = ['localizacion', 'nombre', 'modelo', 'fabricante', 'cantidad', 'cantidadAviso', 'cantidadMaxima','datasheet','imagen','notas','fechaInsercion']
    def __init__(self) -> None:
        self.current_object = {}
        self.data = []
    
    def wizard_cli(self) -> dict:
        print('Nuevo objeto, inserta los siguientes datos: ')
        for prop in self.props_query:
            result = input(f'{prop.upper()}: ').upper()
            self.current_object[prop] = result
        self.insert_to_data(self.current_object)
        
    def insert_to_data(self, datadict):
        #lectura del fichero actual
        with open("data/itemlists.py", 'r') as file:
            content = file.read()
            self.data = ast.literal_eval(content)
            
        #insercion del nuevo objeto en el fichero items.py
        print('Insercion')
        print(self.data)
        
        
        
             
            