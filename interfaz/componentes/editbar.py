import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class EditBar:
    def __init__(self, par, stickto , isEmpty=False) -> None:
        self.isEmpty = isEmpty
        common_settings = {'side':'left', 'fill':'x', 'expand':True}
        
        btn_edit = tb.Button(master=par, text='Editar')
        btn_edit.pack(**common_settings)
        
        btn_notes = tb.Button(master=par, text='Leer notas')
        btn_notes.pack(**common_settings)
        
        btn_del = tb.Button(master=par, text='Borrar', bootstyle='danger')
        btn_del.pack()
        
        if self.isEmpty:
            btn_notes.config(state='disabled')        
            btn_edit.config(state='disabled')
            btn_del.config(state='disabled')