from interfaz.componentes.item import ItemShow
from data.itemlists import items
    
class PopulateManager:
    def __init__(self, frame, data_dict=items) -> None:
        self.items = data_dict
        self.frame = frame
    
    def clear_children(self):
        for child in self.frame.winfo_children():
            child.destroy()
    
    def visualize_all(self):
        self.clear_children()
        for data_item in items:
            ItemShow(self.frame, data_item)
    
    def visualize_low_qty(self):
        self.clear_children()
        items_low = [item for item in items if item['cantidad'] < item['cantidadAviso']]
        for item_l in items_low:
            ItemShow(self.frame, item_l,warn=True)