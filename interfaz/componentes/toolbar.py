import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.newItemForm import NewItemForm

class Toolbar:
    def __init__(self, par) -> None:
        common_settings = {'side':'top', 'fill':'x', 'pady':5, 'padx':5}
        
        container = tb.Frame(master=par, bootstyle='dark')
        container.pack(side='top', fill='both', expand=True)
        
        btn_newItem = tb.Button(master=container, text='Añadir nuevo')
        btn_newItem.pack(**common_settings, anchor='n')
        
        btn_sortName = tb.Button(master=container, text='Org. alfab.')
        btn_sortName.pack(**common_settings, anchor='n')
        
        btn_sortNum = tb.Button(master=container, text='Org. Numero')
        btn_sortNum.pack(**common_settings, anchor='n')
        
        btn_export = tb.Button(master=container, text='Exportar')
        btn_export.pack(**common_settings, anchor='n')
        
        btn_addNew = tb.Button(master=container, text='Añadir objeto', bootstyle='success', command=lambda: NewItemForm(par))
        btn_addNew.pack(**common_settings, anchor='n')
        #todo: abrir nueva ventana para formulario de entrada
        #DEBUG:
        NewItemForm(par)
        
        
        btn_exit = tb.Button(master=container, text='Salir', bootstyle='danger')        
        btn_exit.pack(side='bottom', fill='x', expand=True, anchor='s')
        