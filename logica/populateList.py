from interfaz.componentes.item import ItemShow
from logica.getDataLogic import getData
from fuzzywuzzy import fuzz
    
class PopulateManager:
    precision_search = 70 #ratio requerido para considerar un match
    def __init__(self, frame, data_dict=None) -> None:
        self.items = getData()
        self.frame = frame
    #TODO: Buscar referencias del itemshow
    def clear_children(self):
        for child in self.frame.winfo_children():
            child.destroy()
    
    def visualize_all(self):
        self.clear_children()
        for data_item in self.items:
            ItemShow(self.frame, data_item,popmanagerRef=self)
    
    def visualize_low_qty(self):
        self.clear_children()
        items_low = [item for item in self.items if item['cantidad'] < item['cantidadAviso']]
        for item_l in items_low:
            ItemShow(self.frame, item_l,warn=True,popmanagerRef=self)
            
    def organize_by(self, sortby:str):
        self.clear_children()
        data_sorted = []
        match sortby:
            case 'num':
                data_sorted = sorted(self.items, key=lambda x: int(x['localizacion']))
            case 'name':
                data_sorted = sorted(self.items, key=lambda x: x['nombre'])    
            case _:
                print('Sort no realizado.')
        for item_s in data_sorted:
            ItemShow(self.frame, item_s, popmanagerRef=self)
            
    def search_item(self,query:str, resolution=precision_search):
        self.precision_search = resolution
        found_results = []
        print(f'Searching for {query}')
        for item_s in self.items:
            comparison_result = fuzz.ratio(query.lower().strip(), item_s['nombre'].lower())
            print(f'Match: {comparison_result}')
            if comparison_result >= self.precision_search:
                found_results.append(item_s)
        self.clear_children()
        for match_ in found_results:
            ItemShow(self.frame, match_, popmanagerRef=self)