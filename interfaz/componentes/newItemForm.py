from tkinter import *
import ttkbootstrap as tb

class NewItemForm:
    x_padd =5
    width_entries_txt = 20
    width_entries_int = 4
    def __init__(self, par) -> None:
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title("Formulario de insercion")
        self.newWindow.geometry('300x300')
        
        self.main_container = tb.Frame(master=self.newWindow, padding=self.x_padd)
        self.main_container.pack()
        name_lbl = tb.Label(master=self.main_container, text='Nombre:')
        name_lbl.grid(row=0, column=0)
        name_ent_var = StringVar()
        name_ent = tb.Entry(master=self.main_container, textvariable=name_ent_var, width=self.width_entries_txt)
        name_ent.grid(row=0, column=1)
        
        model_lbl = tb.Label(master=self.main_container, text='Modelo:')
        model_lbl.grid(row=2, column=0)
        model_ent_var = StringVar()
        model_ent = tb.Entry(master=self.main_container, textvariable=model_ent_var, width=self.width_entries_txt)
        model_ent.grid(row=2, column=1)
        
        #Cantidades en un frame propio
        cant_frame = tb.LabelFrame(master=self.main_container, text='Cantidad')
        cant_frame.grid(row=3, column=0, columnspan=2, sticky='ew')
        #Hijos de cant-frame
        cant_act_lblframe = tb.LabelFrame(master=cant_frame, text='Actual')        
        # cant_act_lblframe.grid(row=0, column=0)
        cant_act_lblframe.pack(side='left', padx=(0,5), anchor='w', fill='x', expand=True)
        
        ##Entry del lblframe especifico para actual
        cant_act_entry_var = IntVar()
        cant_act_entry = tb.Entry(master=cant_act_lblframe, width=self.width_entries_int, textvariable=cant_act_entry_var)
        cant_act_entry.grid(row=0, column=0)
        # Segundo hijo de cant frame para maximo
        cant_max_lblframe = tb.LabelFrame(master=cant_frame, text='Maximo')
        # cant_max_lblframe.grid(row=0, column=1)
        cant_max_lblframe.pack(side='left', padx=(5,5), anchor='center', fill='x', expand=True)
        ##Entry para el maximo
        cant_max_entry_var = IntVar()
        cant_max_entry = tb.Entry(master=cant_max_lblframe, width=self.width_entries_int, textvariable=cant_max_entry_var)
        cant_max_entry.grid(row=0,column=0)
        # Tercer hijo de cant frame para aviso
        cant_warn_lblframe = tb.LabelFrame(master=cant_frame, text='Avisar', bootstyle='warning')
        cant_warn_lblframe.pack(side='left', padx=(5,0), anchor='e', fill='x', expand=True)
        ##Entry para el aviso
        cant_warn_entry_var = IntVar()
        cant_warn_entry = tb.Entry(master=cant_warn_lblframe, width=self.width_entries_int, textvariable=cant_warn_entry_var)
        cant_warn_entry.grid(row=0,column=0)
         