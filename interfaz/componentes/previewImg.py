import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from logica.getDataLogic import *
from PIL import Image, ImageTk
import urllib.request
import io


class PhotoImageLabel(tb.Label):
    max_size = (300,300)
    def __init__(self, parent, local=False, **kwargs):
        if local == False:
            with urllib.request.urlopen(kwargs['image']) as u:
                raw_data = u.read()
            # image = Image.open(kwargs['image'])
            image = Image.open(io.BytesIO(raw_data))
            image.thumbnail(self.max_size)
            self._image = ImageTk.PhotoImage(image)
            
        else:
            image = Image.open(kwargs['image'])
            image.thumbnail(self.max_size)
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
        self.maincontainer = tb.Frame(master=self.newWindow)
        self.maincontainer.pack(**self.common_options_pack)
        self.labeltext = tb.LabelFrame(master=self.maincontainer, text=f'{self.original_data["nombre"]}: {self.original_data["modelo"]}')
        self.labeltext.pack(**self.common_options_pack)


    def show_image(self):
        if self.original_data['imagen'] != '':
            self.photo_label = PhotoImageLabel(self.labeltext, image=self.original_data['imagen'],local=False)
            self.photo_label.pack()
        else:
            self.photo_label = PhotoImageLabel(self.labeltext, image="data/imgs/noimage.png",local=True)
            self.photo_label.pack()
        # self.url_lbl = tb.Label(master=self.labeltext, text=f'URL: {self.original_data["imagen"]}')
        # self.url_lbl.pack()