import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.popupNotes import NotePopup
from logica.constants_data import *
from logica.getDataLogic import *


class EditBar:
    def __init__(self, par, stickto, isEmpty=False, objectdata=None, popmanagerRef=None) -> None:
        self.isEmpty = isEmpty
        self.objectdata = objectdata
        common_settings = {"side": "left", "fill": "x", "expand": True}

        #TODO: Añadir funcionalidad para editar campos (abrir nueva ventana)
        btn_edit = tb.Button(master=par, text="Editar")
        btn_edit.pack(**common_settings)
        btn_notes = tb.Button(
            master=par,
            text="Leer notas",
            command=lambda: NotePopup(par, self.objectdata),
        )
        btn_notes.pack(**common_settings)
        # si la longitud de las notas es menor a MAX_LEN_NOTES (45), desactivar boton
        if len(self.objectdata["notas"]) > MAX_LEN_NOTES:
            btn_notes.config(state="enabled")
        else:
            btn_notes.config(state="disabled")

        btn_del = tb.Button(master=par, text="Borrar", bootstyle="danger", command=lambda: delete_item(self.objectdata['uuid'],par=par))
        btn_del.pack()

        if self.isEmpty:
            btn_notes.config(state="disabled")
            btn_edit.config(state="disabled")
            btn_del.config(state="disabled")
