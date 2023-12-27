from tkinter import *
import ttkbootstrap as tb
from logica.getDataLogic import *


class PreviewWindow:
    x_padd = 5

    def __init__(self, par, uuid_to_modify, popmanagerRef=None) -> None:
        self.uuid_to_modify = uuid_to_modify
        self.root = par
        self.original_data = retrieve_item(uuid_target=self.uuid_to_modify)
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title(f"Imagen previa de:TEST")
        #TODO: Completar interfaz para imagen del objeto, usando original_data['imagen']
        #TODO: Utilizar try except para no cargar la imagen en caso de que no exista el campo original_data['imagen']
        
        
        