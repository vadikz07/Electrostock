from tkinter import *
import ttkbootstrap as tb
from logica.InsertionManager import InsertionManager
from logica.getDataLogic import *


class NewItemForm:
    x_padd =5
    width_entries_txt = 20
    width_entries_int = 4
    def __init__(self, par) -> None:
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title("Formulario de insercion")
        
        self.main_container = tb.Frame(master=self.newWindow, padding=self.x_padd)
        self.main_container.pack()
        
        self.name_lblframe= tb.LabelFrame(master=self.main_container, text='Nombre')
        self.name_lblframe.grid(row=0, column=0, sticky='ew')
        self.name_ent_var = StringVar()
        self.name_ent = tb.Entry(master=self.name_lblframe, textvariable=self.name_ent_var)
        self.name_ent.pack(side='left', fill='x',expand=True, anchor='w')

        self.boxnum_lblframe = tb.LabelFrame(master=self.main_container, text='Cajon nº')
        self.boxnum_lblframe.grid(row=0, column=1, sticky='e')
        self.boxnum_ent = tb.Spinbox(master=self.boxnum_lblframe, from_=1, to=96)
        self.boxnum_ent.pack(side='right', expand=False, anchor='e')
        
        self.model_lblframe= tb.LabelFrame(master=self.main_container, text='Modelo')
        self.model_lblframe.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.model_ent_var = StringVar()
        self.model_ent = tb.Entry(master=self.model_lblframe, textvariable=self.model_ent_var)
        self.model_ent.pack(side='left', fill='x',expand=True, anchor='w')
        
        #Cantidades en un frame propio
        self.cant_frame = tb.LabelFrame(master=self.main_container, text='Cantidad')
        self.cant_frame.grid(row=3, column=0, columnspan=2, sticky='ew')
        #Hijos de cant-frame
        self.cant_act_lblframe = tb.LabelFrame(master=self.cant_frame, text='Actual')        
        # self.cant_act_lblframe.grid(row=0, column=0)
        self.cant_act_lblframe.pack(side='left', padx=(0,5), anchor='w', fill='x', expand=True)
        
        ##Entry del lblframe especifico para actual
        self.cant_act_entry_var = IntVar()
        self.cant_act_entry = tb.Entry(master=self.cant_act_lblframe,width=self.width_entries_int, textvariable=self.cant_act_entry_var)
        self.cant_act_entry.pack(side='top', fill='x')
        # Segundo hijo de cant frame para maximo
        self.cant_max_lblframe = tb.LabelFrame(master=self.cant_frame, text='Maximo')
        # self.cant_max_lblframe.grid(row=0, column=1)
        self.cant_max_lblframe.pack(side='left', padx=(5,5), anchor='center', fill='x', expand=True)
        ##Entry para el maximo
        self.cant_max_entry_var = IntVar()
        self.cant_max_entry = tb.Entry(master=self.cant_max_lblframe,width=self.width_entries_int, textvariable=self.cant_max_entry_var)
        self.cant_max_entry.pack(side='top', fill='x')
        # Tercer hijo de cant frame para aviso
        self.cant_warn_lblframe = tb.LabelFrame(master=self.cant_frame, text='Avisar', bootstyle='warning')
        self.cant_warn_lblframe.pack(side='left', padx=(5,0), anchor='e', fill='x', expand=True)
        ##Entry para el aviso
        self.cant_warn_entry_var = IntVar()
        self.cant_warn_entry = tb.Entry(master=self.cant_warn_lblframe,width=self.width_entries_int, textvariable=self.cant_warn_entry_var)
        self.cant_warn_entry.pack(side='top', fill='x')
        #todo: continuar formulario con los datos de itemlist
        self.dsheet_lblframe = tb.LabelFrame(master=self.main_container, text='Datasheet')
        self.dsheet_lblframe.grid(row=4,column=0, columnspan=2, sticky='ew')
        self.dsheet_ent_var = StringVar()
        self.dsheet_ent = tb.Entry(master=self.dsheet_lblframe, textvariable=self.dsheet_ent_var)        
        self.dsheet_ent.pack(side='top', fill='x', expand=True)
        
        self.notes_lblframe = tb.LabelFrame(master=self.main_container, text='Notas')
        self.notes_lblframe.grid(row=5, column=0, columnspan=2, sticky='ew')
        self.notes_scroll = tb.Scrollbar(master=self.notes_lblframe, orient='vertical', bootstyle='success round')
        self.notes_text = tb.Text(master=self.notes_lblframe, height=4, yscrollcommand=self.notes_scroll.set)
        self.notes_text.pack(side='left',fill='x')
        self.notes_scroll.pack(side='right', fill='y')
        self.notes_scroll.config(command=self.notes_text.yview)
        
        #Fecha insercion
        self.date_lblframe = tb.LabelFrame(master=self.main_container, text='Fecha insercion')
        self.date_lblframe.grid(row=6, column=0, columnspan=2, sticky='ew')
        self.testdate = tb.DateEntry(self.date_lblframe, bootstyle='info', firstweekday=0)
        self.testdate.pack()
        
        self.control_lblframe = tb.LabelFrame(master=self.main_container, text='Acciones')
        self.control_lblframe.grid(row=10, column=0, columnspan=2, sticky='ew')
        self.clear_data_btn = tb.Button(master=self.control_lblframe, text='Limpiar campos', bootstyle='danger')
        self.clear_data_btn.pack(side='left', padx=(0,5),anchor='w',fill='x')
        
        self.add_dataDB_btn = tb.Button(master=self.control_lblframe, text='Agregar componente', bootstyle='success', command=self.collect_data)
        self.add_dataDB_btn.pack(side='right', padx=(5,0), anchor='e', fill='x')
        
        self.cli_btn = tb.Button(master=self.control_lblframe, text='CLI', bootstyle='info', command=lambda: InsertionManager().wizard_cli())
        self.cli_btn.pack(side='right', padx=(5,0), anchor='e', fill='x')
    
    def collect_data(self) -> dict:
        data_dict = {}
        data_dict['nombre'] = self.name_ent_var.get()
        data_dict['modelo'] = self.model_ent_var.get()
        data_dict['fabricante'] = ''
        data_dict['cantidad'] = self.cant_act_entry_var.get()
        data_dict['cantidadAviso'] = self.cant_warn_entry_var.get()
        data_dict['cantidadMaxima'] = self.cant_max_entry_var.get()
        data_dict['datasheet'] = self.dsheet_ent_var.get()
        data_dict['notas'] = self.notes_text.get("1.0", "end-1c")
        data_dict['fechaInsercion'] = self.testdate.entry.get()
        data_dict['localizacion'] = self.boxnum_ent.get()
        saveData(data_dict)
        #TODO: Añadir validacion de las entradas , ej, Nombre no este vacio y sea mayor a 3 caracteres, etc...
    

        
        