from tkinter import *
from PIL import ImageTk, Image
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.editbar import EditBar


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
    def __init__(self, par, data_dict) -> None:
        item_frame = tb.Frame(master=par, bootstyle='dark', border=10)
        item_frame.pack(side='top', fill='x', expand=True)
        item_frame_lower = tb.Frame(master=par, bootstyle='light')
        item_frame_lower.pack(side='top', fill='x', expand=True)
        
        num_frame = tb.LabelFrame(master=item_frame,text='Cajon', bootstyle='default')
        num_frame.pack(side='left', fill='y')
        
        contents_frame = tb.LabelFrame(master=item_frame, text='Contenidos', bootstyle='default')
        contents_frame.pack(side='left', fill='both', expand=True)

        # INFO FRAME⬇️
        lbl_boxNum = tb.Label(master=num_frame, text=data_dict['localizacion'], font=("Arial", 24, "bold"), padding=md_padd)
        lbl_boxNum.pack(side='left')
        
        lbl_name = tb.Label(master=contents_frame, text=data_dict['nombre'], font=("Arial", 12, "bold"), padding=md_padd)
        lbl_name.grid(column=0, row=0)
        
        lbl_model = tb.Label(master=contents_frame, text=data_dict['modelo'], font=("Arial", 10, "normal"), padding=md_padd)
        lbl_model.grid(column=1, row=0)
        
        
        lbl_notes = tb.Label(master=contents_frame, text=data_dict['notas'], font=("Arial", 10, "normal"), padding=md_padd)
        lbl_notes.grid(column=0, row=1,columnspan=3, sticky='w')
        
        
        additional_frame = tb.Frame(master=item_frame_lower,bootstyle='default')
        additional_frame.pack(side="top", fill='both', expand=True)
        
        #IMG FRAME
        
        #CONTROL FRAME⬇️
        if data_dict['datasheet'] != '':
            btn_dsheet = tb.Button(master=additional_frame, text=data_dict['datasheet'], bootstyle='success')
        else:
            btn_dsheet = tb.Button(master=additional_frame, text='No hay datasheet', bootstyle='warning')
        btn_dsheet.pack(side='left', anchor='w')
        
        amt_fstring = f'{data_dict["cantidad"]}/ {data_dict["cantidadMaxima"]}'
        lbl_cant = tb.Label(master=additional_frame, text=amt_fstring, font=("Arial", 12, "bold"), padding=md_padd)
        lbl_cant.pack(side='left', anchor='center')
        
        lbl_date = tb.Label(master=additional_frame, text=data_dict['fechaInsercion'])
        lbl_date.pack(side='right', anchor='e')
        
        control_frame = tb.Frame(master=item_frame_lower, bootstyle='dark')
        control_frame.pack(side="bottom", fill='both', expand=True)
        EditBar(control_frame,'e')
        #Separador para el siguiente objeto
        sepa = tb.Separator(par, orient="horizontal", bootstyle="dark")
        sepa.pack(side='top', fill='x', pady=4,expand=True)
        
        
        
        
        