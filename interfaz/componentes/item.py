from tkinter import *
from PIL import ImageTk, Image
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.editbar import EditBar
from logica.getContainerSize import get_container_size
from logica.BrowserLogic import open_dsheet_url
from logica.constants_data import *

"""
data_arr ejemplo de estructura:
{
    "nombre": "leds",                                           x
    "modelo": "LED-567",                                        x
    "cantidad": 30,                                             x
    "cantidadAviso": 5,                                         
    "cantidadMaxima": 100,                                      x
    "datasheet": "www.dsheet.com/56789/data.php",               x
    "imagen": "https://.....jpg",                               x
    "notas": "leds de varios colores",                          x
    "fechaInsercion": "8 abril 2021",                           x
    "localizacion": 23                                          x
  }

"""
md_padd = 10

class ItemShow:
    def __init__(self, par, data_dict, isEmpty=False, boxnum=0, warn=False) -> None:
        self.isEmpty = isEmpty
        self.boxnum = boxnum
        self.warn = warn
        self.maxlennotes = MAX_LEN_NOTES
        item_frame = tb.Frame(master=par, bootstyle='dark', border=10)
        item_frame.pack(side='top', fill='x', expand=True)
        item_frame_lower = tb.Frame(master=par, bootstyle='light')
        item_frame_lower.pack(side='top', fill='x', expand=True)
        
        num_frame = tb.LabelFrame(master=item_frame,text='Cajon', bootstyle='default')
        num_frame.pack(side='left', fill='y')
        
        contents_frame = tb.LabelFrame(master=item_frame, text='Contenidos', bootstyle='default')
        contents_frame.pack(side='left', fill='both', expand=True)

        # INFO FRAME⬇️
        if not self.isEmpty:    #si no esta vacio, generar contenido para infoframe
            var_box_num = data_dict['localizacion']
            var_name = data_dict['nombre']
            var_model = data_dict['modelo']
            var_fabricante = data_dict['fabricante']
            var_notas = data_dict['notas']
        else: #VALORES PARA VACIO
            var_box_num = self.boxnum
            var_name = "VACIO"
            var_model = ""
            var_fabricante = ""
            var_notas = get_container_size(var_box_num)
            
            
        color = 'orange' if self.warn else 'white'
        lbl_boxNum = tb.Label(master=num_frame, text=var_box_num, font=("Arial", 24, "bold"), padding=md_padd, foreground=color)
        lbl_boxNum.pack(side='left')
        
        lbl_name = tb.Label(master=contents_frame, text=var_name, font=("Arial", 12, "bold"), padding=md_padd, foreground=color)
        lbl_name.grid(column=0, row=0)
        
        lbl_model = tb.Label(master=contents_frame, text=var_model, font=("Arial", 10, "normal"), padding=md_padd)
        lbl_model.grid(column=1, row=0)
        
        lbl_fabricante = tb.Label(master=contents_frame, text=var_fabricante, font=("Arial", 10, "italic"), padding=md_padd)
        lbl_fabricante.grid(column=2, row=0, sticky='e')
        
        formatted_notes = f'{var_notas[0:self.maxlennotes]}... (Leer mas)' if len(var_notas) > self.maxlennotes else var_notas
        lbl_notes = tb.Label(master=contents_frame, text=formatted_notes, font=("Arial", 10, "normal"), padding=md_padd)
        lbl_notes.grid(column=0, row=1,columnspan=3, sticky='w')
        
        additional_frame = tb.Frame(master=item_frame_lower,bootstyle='default')
        additional_frame.pack(side="top", fill='both', expand=True)
        
        #IMG FRAME
        
        #CONTROL FRAME⬇️
        if not self.isEmpty:   
            if data_dict['datasheet'] != '':
                btn_dsheet = tb.Button(master=additional_frame, text=data_dict['datasheet'], bootstyle='success')
                if self.isEmpty:
                    btn_dsheet.config(state='disabled')
            else:
                btn_dsheet = tb.Button(master=additional_frame, text='No hay datasheet', bootstyle='warning')
            btn_dsheet.pack(side='left', anchor='w')
            btn_dsheet.config(command=lambda: open_dsheet_url(data_dict['datasheet']))
            
            amt_fstring = f'{data_dict["cantidad"]}/ {data_dict["cantidadMaxima"]}'
            lbl_cant = tb.Label(master=additional_frame, text=amt_fstring, font=("Arial", 12, "bold"), padding=md_padd, foreground=color)
            lbl_cant.pack(side='left', anchor='center')
            
            lbl_date = tb.Label(master=additional_frame, text=data_dict['fechaInsercion'])
            lbl_date.pack(side='right', anchor='e')
            
            
            
        control_frame = tb.Frame(master=item_frame_lower, bootstyle='dark')
        control_frame.pack(side="bottom", fill='both', expand=True)
        EditBar(par=control_frame,stickto='e',isEmpty=isEmpty,objectdata=data_dict)
        #Separador para el siguiente objeto
        sepa = tb.Separator(par, orient="horizontal", bootstyle="dark")
        sepa.pack(side='top', fill='x', pady=4,expand=True)
        
