import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from logica.getDataLogic import *
from PIL import Image, ImageTk


class PhotoImageLabel(tb.Label):
    def __init__(self, parent, **kwargs):
        image = Image.open(kwargs['image'])
        self._image = ImageTk.PhotoImage(image)
        
        kwargs['image'] = self._image
        super().__init__(parent, **kwargs)
        

class PreviewWindow:
    x_padd = 5
    common_options_pack = {'side':'top', 'expand':True,'fill':'both','padx':5, 'pady':10}
    def __init__(self, par, uuid_to_modify, popmanagerRef=None) -> None:
        self.uuid_to_modify = uuid_to_modify
        self.root = par
        self.original_data = retrieve_item(uuid_target=self.uuid_to_modify)
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.title('Imagen')
        self.newWindow.geometry('400x600')
        self.maincontainer = tk.Frame(master=self.newWindow)
        self.maincontainer.pack(**self.common_options_pack)
        self.labeltext = tb.Label(master=self.maincontainer, text='Vista previa')
        self.labeltext.pack()

    def show_image(self):
        self.photo_label = PhotoImageLabel(self.labeltext, image='data/imgs/Retro.png')
        self.photo_label.pack()