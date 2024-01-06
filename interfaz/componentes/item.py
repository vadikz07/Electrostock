from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.editbar import EditBar
from logica.getDataLogic import get_container_size
from logica.BrowserLogic import open_dsheet_url
from logica.constants_data import *
from datetime import datetime

"""
data_arr ejemplo de estructura:
{
    "uuid" : "550e8400-e29b-41d4-a716-446655440000"
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
    all_items = []
    def __init__(self, par, data_dict, isEmpty=False, boxnum=0, warn=False, popmanagerRef=None) -> None:
        self.isEmpty = isEmpty
        self.boxnum = boxnum
        self.warn = warn
        self.maxlennotes = MAX_LEN_NOTES
        self.popmanager = popmanagerRef
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
            var_notas = ""
            
            
        color = 'orange' if self.warn else 'white'
        lbl_boxNum = tb.Label(master=num_frame, text=var_box_num, font=("Arial", 24, "bold"), padding=md_padd, foreground=color)
        lbl_boxNum.pack(side='top')
        lbl_boxnumSize = tb.Label(master=num_frame, text=get_container_size(data_dict['localizacion']), font=("Arial", 7, "normal"))
        lbl_boxnumSize.pack(side='bottom')
        if get_container_size(data_dict['localizacion']) == 'INPUT NO VALIDO':
            lbl_boxnumSize.config(text=get_container_size(var_box_num))
        
        lbl_name = tb.Label(master=contents_frame, text=var_name, font=("Arial", 12, "bold"), padding=md_padd, foreground=color)
        lbl_name.grid(column=0, row=0)
        
        lbl_model = tb.Label(master=contents_frame, text=var_model, font=("Arial", 10, "normal"), padding=md_padd)
        lbl_model.grid(column=1, row=0, sticky='e')
        
        lbl_fabricante = tb.Label(master=contents_frame, text=var_fabricante, font=("Arial", 10, "italic"), padding=md_padd)
        lbl_fabricante.grid(column=2, row=0, sticky='e')
        
        contents_frame.grid_columnconfigure(0, weight=0)
        contents_frame.grid_columnconfigure(1, weight=20)
        contents_frame.grid_columnconfigure(2, weight=10)
        
        formatted_notes = f'{var_notas[0:self.maxlennotes]}... (Leer mas)' if len(var_notas) > self.maxlennotes else var_notas
        lbl_notes = tb.Label(master=contents_frame, text=formatted_notes, font=("Arial", 10, "normal"), padding=md_padd)
        lbl_notes.grid(column=0, row=1,columnspan=3, sticky='w')
        
        additional_frame = tb.Frame(master=item_frame_lower,bootstyle='default')
        additional_frame.pack(side="top", fill='both', expand=True)
        
        #IMG FRAME
        
        #CONTROL FRAME⬇️
        if not self.isEmpty:   #Si tiene contenidos
            if data_dict['datasheet'] != '':
                btn_dsheet = tb.Button(master=additional_frame, text=data_dict['datasheet'], bootstyle='success')
                if self.isEmpty:
                    btn_dsheet.config(state='disabled')
            else:
                btn_dsheet = tb.Button(master=additional_frame, text='No hay datasheet', bootstyle='warning')
            btn_dsheet.pack(side='left', anchor='w')
            btn_dsheet.config(command=lambda: open_dsheet_url(data_dict['datasheet']))
            
            amt_fstring = f'Cantidad: {data_dict["cantidad"]}'
            lbl_cant = tb.Label(master=additional_frame, text=amt_fstring, font=("Arial", 12, "bold"), padding=md_padd, foreground=color)
            lbl_cant.pack(side='left', anchor='center')
            try:
                lbl_date = tb.Label(master=additional_frame, text=data_dict['fechaInsercion'])
            except KeyError:
                print(f'Fecha insercion no actualizada.')
                datetimenow = datetime.now()
                self.act_date = datetimenow.strftime('%d/%m/%Y')
                lbl_date = tb.Label(master=additional_frame, text=self.act_date)
            lbl_date.pack(side='right', anchor='e')
            
            
        control_frame = tb.Frame(master=item_frame_lower, bootstyle='dark')
        control_frame.pack(side="bottom", fill='both', expand=True)
        EditBar(par=control_frame,stickto='e',isEmpty=isEmpty,objectdata=data_dict,popmanagerRef=self.popmanager,default_box_num=self.boxnum)
        #Separador para el siguiente objeto
        sepa = tb.Separator(par, orient="horizontal", bootstyle="dark")
        sepa.pack(side='top', fill='x', pady=4,expand=True)
        
    @classmethod
    def retrieve_box_num_contents(cls,boxnum:int) -> list:
        pass
    
    @classmethod
    def retrieve_all_items(cls):
        return cls.all_items
    
    
