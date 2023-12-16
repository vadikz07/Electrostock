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
        
        self.main_container = tb.Frame(master=self.newWindow, padding=self.x_padd)
        self.main_container.pack()
        name_lblframe= tb.LabelFrame(master=self.main_container, text='Nombre')
        name_lblframe.grid(row=0, column=0, sticky='ew')
        name_ent_var = StringVar()
        name_ent = tb.Entry(master=name_lblframe, textvariable=name_ent_var)
        name_ent.pack(side='left', fill='x',expand=True, anchor='w')
        boxnum_lblframe = tb.LabelFrame(master=self.main_container, text='Cajon nº')
        boxnum_lblframe.grid(row=0, column=1, sticky='e')
        boxnum_ent = tb.Spinbox(master=boxnum_lblframe, from_=1, to=96)
        boxnum_ent.pack(side='right', expand=False, anchor='e')
        
        model_lblframe= tb.LabelFrame(master=self.main_container, text='Modelo')
        model_lblframe.grid(row=1, column=0, columnspan=2, sticky='ew')
        model_ent_var = StringVar()
        model_ent = tb.Entry(master=model_lblframe, textvariable=model_ent_var)
        model_ent.pack(side='left', fill='x',expand=True, anchor='w')
        
        #Cantidades en un frame propio
        cant_frame = tb.LabelFrame(master=self.main_container, text='Cantidad')
        cant_frame.grid(row=3, column=0, columnspan=2, sticky='ew')
        #Hijos de cant-frame
        cant_act_lblframe = tb.LabelFrame(master=cant_frame, text='Actual')        
        # cant_act_lblframe.grid(row=0, column=0)
        cant_act_lblframe.pack(side='left', padx=(0,5), anchor='w', fill='x', expand=True)
        
        ##Entry del lblframe especifico para actual
        cant_act_entry_var = IntVar()
        cant_act_entry = tb.Entry(master=cant_act_lblframe,width=self.width_entries_int, textvariable=cant_act_entry_var)
        cant_act_entry.pack(side='top', fill='x')
        # Segundo hijo de cant frame para maximo
        cant_max_lblframe = tb.LabelFrame(master=cant_frame, text='Maximo')
        # cant_max_lblframe.grid(row=0, column=1)
        cant_max_lblframe.pack(side='left', padx=(5,5), anchor='center', fill='x', expand=True)
        ##Entry para el maximo
        cant_max_entry_var = IntVar()
        cant_max_entry = tb.Entry(master=cant_max_lblframe,width=self.width_entries_int, textvariable=cant_max_entry_var)
        cant_max_entry.pack(side='top', fill='x')
        # Tercer hijo de cant frame para aviso
        cant_warn_lblframe = tb.LabelFrame(master=cant_frame, text='Avisar', bootstyle='warning')
        cant_warn_lblframe.pack(side='left', padx=(5,0), anchor='e', fill='x', expand=True)
        ##Entry para el aviso
        cant_warn_entry_var = IntVar()
        cant_warn_entry = tb.Entry(master=cant_warn_lblframe,width=self.width_entries_int, textvariable=cant_warn_entry_var)
        cant_warn_entry.pack(side='top', fill='x')
        #todo: continuar formulario con los datos de itemlist
        dsheet_lblframe = tb.LabelFrame(master=self.main_container, text='Datasheet')
        dsheet_lblframe.grid(row=4,column=0, columnspan=2, sticky='ew')
        dsheet_ent_var = StringVar()
        dsheet_ent = tb.Entry(master=dsheet_lblframe, textvariable=dsheet_ent_var)        
        dsheet_ent.pack(side='top', fill='x', expand=True)
        
        notes_lblframe = tb.LabelFrame(master=self.main_container, text='Notas')
        notes_lblframe.grid(row=5, column=0, columnspan=2, sticky='ew')
        notes_scroll = tb.Scrollbar(master=notes_lblframe, orient='vertical', bootstyle='success round')
        notes_text = tb.Text(master=notes_lblframe, height=4, yscrollcommand=notes_scroll.set)
        notes_text.pack(side='left',fill='x')
        notes_scroll.pack(side='right', fill='y')
        notes_scroll.config(command=notes_text.yview)
        
        #Fecha insercion
        date_lblframe = tb.LabelFrame(master=self.main_container, text='Fecha insercion')
        date_lblframe.grid(row=6, column=0, columnspan=2, sticky='ew')
        testdate = tb.DateEntry(date_lblframe, bootstyle='info')
        testdate.pack()
        
        control_lblframe = tb.LabelFrame(master=self.main_container, text='Acciones')
        control_lblframe.grid(row=10, column=0, columnspan=2, sticky='ew')
        clear_data_btn = tb.Button(master=control_lblframe, text='Limpiar campos', bootstyle='danger')
        clear_data_btn.pack(side='left', padx=(0,5),anchor='w',fill='x')
        
        add_dataDB_btn = tb.Button(master=control_lblframe, text='Agregar componente', bootstyle='success')
        add_dataDB_btn.pack(side='right', padx=(5,0), anchor='e', fill='x')
        
        
        