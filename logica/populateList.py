from interfaz.componentes.item import ItemShow
from data.itemlists import items
    
class PopulateManager:
    def __init__(self, frame, data_dict=items) -> None:
        self.items = data_dict
        self.frame = frame
        self.visualize_all()
    
    def visualize_all(self):
        print('Generando lista')
        for data_item in items:
            ItemShow(self.frame, data_item, isEmpty=False)