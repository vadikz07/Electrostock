import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.newItemForm import NewItemForm
from interfaz.componentes.thumbgen import ThumbGen
from logica.populateList import PopulateManager

class Toolbar:
    def __init__(self, par, infoframe=None) -> None:
        common_settings = {'side':'top', 'fill':'x', 'pady':5, 'padx':5, 'anchor':'n'}
        
        container = tb.Frame(master=par, bootstyle='dark')
        container.pack(side='top', fill='both', expand=True)
        
        btn_sortName = tb.Button(master=container, text='Org. Nombre', command=lambda: PopulateManager(infoframe).organize_by('name'))
        btn_sortName.pack(**common_settings)
        
        btn_sortNum = tb.Button(master=container, text='Org. Numero', command=lambda: PopulateManager(infoframe).organize_by('num'))
        btn_sortNum.pack(**common_settings)
        
        btn_export = tb.Button(master=container, text='Exportar')
        btn_export.pack(**common_settings)
        
        btn_genThumb = tb.Button(master=container, text='Generar etiqueta', bootstyle='info', command=lambda: ThumbGen(par))
        btn_genThumb.pack(**common_settings)
        #DEBUG
        # ThumbGen(par)
        
        #boton para abrir nueva ventana con formulario de insercion
        btn_addNew = tb.Button(master=container, text='Añadir objeto', bootstyle='success', command=lambda: NewItemForm(par))
        btn_addNew.pack(**common_settings)

        btn_exit = tb.Button(master=container, text='Salir', bootstyle='danger')        
        btn_exit.pack(side='bottom', fill='x', expand=True, anchor='s')
        
        #Metricas 