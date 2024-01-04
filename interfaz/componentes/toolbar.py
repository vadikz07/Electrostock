import ttkbootstrap as tb
from tkinter import StringVar, IntVar
from ttkbootstrap.constants import *
from interfaz.componentes.newItemForm import NewItemForm
from interfaz.componentes.thumbgen import ThumbGen
from logica.populateList import PopulateManager
from interfaz.componentes.gridDisplay import GridDisplay


class Toolbar:
    def __init__(self, par, popmanagerRef: PopulateManager, rootRef) -> None:
        self.rootRef = rootRef
        self.popmanager = popmanagerRef
        common_settings = {
            "side": "top",
            "fill": "x",
            "pady": 5,
            "padx": 5,
            "anchor": "n",
        }

        container = tb.Frame(master=par, bootstyle="dark")
        container.pack(side="top", fill="both", expand=True)

        btn_sortName = tb.Button(
            master=container,
            text="Org. Nombre",
            command=lambda: popmanagerRef.organize_by("name"),
        )
        btn_sortName.pack(**common_settings)

        btn_sortNum = tb.Button(
            master=container,
            text="Org. Numero",
            command=lambda: popmanagerRef.organize_by("num"),
        )
        btn_sortNum.pack(**common_settings)

        btn_findByNum_btn = tb.Button(
            master=container,
            text='Mostrar por cajon',
            command=lambda: popmanagerRef.visualize_by_num(int(spinbox_cajon_num.get()))
        )
        # btn_findByNum_btn.pack(**common_settings)
        
        spinbox_cajon_num = tb.Spinbox(
            master=container,
            from_=1,
            to=99,
        )
        spinbox_cajon_num.insert(0,"1")
        # spinbox_cajon_num.pack(**common_settings)

        btn_export = tb.Button(master=container, text="Exportar", state="disabled")
        # btn_export.pack(**common_settings)

        btn_genThumb = tb.Button(
            master=container,
            text="Generar etiqueta",
            bootstyle="info",
            command=lambda: ThumbGen(par),
        )
        btn_genThumb.pack(**common_settings)


        # boton para abrir nueva ventana con formulario de insercion
        btn_addNew = tb.Button(
            master=container,
            text="Añadir objeto",
            bootstyle="success",
            command=lambda: NewItemForm(par, popmanagerRef=popmanagerRef),
        )
        btn_addNew.pack(**common_settings)


        btn_exit = tb.Button(
            master=container,
            text="Salir",
            bootstyle="danger",
            command=self.rootRef.destroy,
        )
        # btn_exit.pack(side="bottom", fill="x", expand=True, anchor="s")

        # Metricas
        GridDisplay(par=container, popmanagerRef=self.popmanager)

        #TODO: Si el contenedor img_lblframe tiene mas de 1 hijo, destruirlo, mostrar solo el ultimo.
        #TODO: Llamar desde previewimg a una funcion aqui para postear imagenes, donde se encuentre la logica del todo anterior.
        self.img_lblframe = tb.LabelFrame(master=container, text="Imagen")
        self.img_lblframe.pack(**common_settings)