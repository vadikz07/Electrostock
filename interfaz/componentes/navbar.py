from tkinter import StringVar
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from logica.showEmptyContainers import show_empty_containers
from logica.populateList import PopulateManager

class NavBarTop:
    def __init__(self, par, sframe_ref) -> None:
        common_left = {'side':'left', 'padx':4}
        common_right = {'side':'right', 'anchor':'e'}
        
        navbar_frame = tb.Frame(master=par, bootstyle='dark')
        navbar_frame.pack(anchor='ne', fill='both', expand=True)

        btn_showEmpty = tb.Button(master=navbar_frame, text='Mostrar vacios', command=lambda: show_empty_containers(sframe_ref))
        btn_showEmpty.pack(**common_left)
        
        btn_showAll = tb.Button(master=navbar_frame, text='Mostrar todos', bootstyle='info', command=lambda: PopulateManager(sframe_ref).visualize_all())
        btn_showAll.pack(**common_left)
        
        
        
        btn_refreshList = tb.Button(master=navbar_frame, text='Vaciar lista', command=lambda: PopulateManager(sframe_ref).clear_children())
        # btn_refreshList.pack(**common_left)
        
        btn_showFew = tb.Button(master=navbar_frame, text='Mostrar avisos', bootstyle='warning', command=lambda: PopulateManager(sframe_ref).visualize_low_qty())
        btn_showFew.pack(**common_left)
        
        btn_commitSearch = tb.Button(master=navbar_frame, text='Buscar', command=lambda: PopulateManager(sframe_ref).search_item(ent_searchBar.get(), int(precision_slider.get())))
        btn_commitSearch.pack(**common_right)
        
        
        value_searchBar = StringVar()
        ent_searchBar = tb.Entry(master=navbar_frame, textvariable=value_searchBar)
        ent_searchBar.pack(**common_right)
        
        #Resolucion de busqueda
        def slider(e):
            precision_lbl.config(text=f'{int(precision_slider.get())}')
            
        precision_slider = tb.Scale(master=navbar_frame, orient='horizontal', length=135, from_=35, to=100, value=70, command=slider)
        precision_slider.pack(**common_right, padx=10)
        
        precision_lbl = tb.Label(master=navbar_frame, text='Precision')
        precision_lbl.pack(**common_right, padx=5)

    
