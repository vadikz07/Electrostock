from tkinter import StringVar
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class NavBarTop:
    def __init__(self, par) -> None:
        common_left = {'side':'left', 'padx':4}
        common_right = {'side':'right', 'anchor':'e'}
        
        navbar_frame = tb.Frame(master=par, bootstyle='dark')
        navbar_frame.pack(anchor='ne', fill='both', expand=True)

        btn_showEmpty = tb.Button(master=navbar_frame, text='Mostrar vacios')
        btn_showEmpty.pack(**common_left)
        
        btn_refreshList = tb.Button(master=navbar_frame, text='Reiniciar lista')
        btn_refreshList.pack(**common_left)
        
        btn_showFew = tb.Button(master=navbar_frame, text='Mostrar obj con poca cantidad', bootstyle='warning')
        btn_showFew.pack(**common_left)
        
        btn_commitSearch = tb.Button(master=navbar_frame, text='Buscar')
        btn_commitSearch.pack(**common_right)
        
        value_searchBar = StringVar()
        ent_searchBar = tb.Entry(master=navbar_frame, textvariable=value_searchBar)
        ent_searchBar.pack(**common_right)
        

    
