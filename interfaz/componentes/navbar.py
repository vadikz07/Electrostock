from tkinter import StringVar
import ttkbootstrap as tb
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.icons import Icon
from ttkbootstrap.constants import *
from logica.showEmptyContainers import show_empty_containers
from logica.populateList import PopulateManager
from logica.imgchecker import ImgCheckerGUI
from tkinter import BooleanVar, IntVar


class NavBarTop:
    def __init__(self, par, popmanagerRef: PopulateManager) -> None:
        common_left = {"side": "left", "padx": 4}
        common_right = {"side": "right", "anchor": "e"}

        navbar_frame = tb.Frame(master=par, bootstyle="dark")
        navbar_frame.pack(anchor="ne", fill="both", expand=True)

        btn_showEmpty = tb.Button(
            master=navbar_frame,
            text="Mostrar vacios",
            command=lambda: popmanagerRef.visualize_empty(),
        )
        # btn_showEmpty.pack(**common_left)

        btn_showAll = tb.Button(
            master=navbar_frame,
            text="Mostrar por fecha",
            bootstyle="info",
            command=lambda: popmanagerRef.visualize_all(),
        )
        btn_showAll.pack(**common_left)

        btn_showFew = tb.Button(
            master=navbar_frame,
            text="Mostrar avisos",
            bootstyle="warning",
            command=lambda: popmanagerRef.visualize_low_qty(),
        )
        btn_showFew.pack(**common_left)
        
        btn_check_img = tb.Button(
            master=navbar_frame,
            text='Comprobar imagenes',
            bootstyle='warning',
            command=lambda: ImgCheckerGUI(par=navbar_frame, arr_of_items=popmanagerRef.all_items)
        )
        btn_check_img.pack(**common_left)

        btn_clearSearchbar = tb.Button(
            master=navbar_frame,
            text="Borrar",
            bootstyle="danger",
            command=lambda: value_searchBar.set(""),
        )
        ttip_clearSearchBar = ToolTip(
            btn_clearSearchbar,
            text="Borrar texto de la busqueda",
            bootstyle=(DANGER, INVERSE),
        )
        btn_clearSearchbar.pack(**common_right)

        # btn_commitSearch = tb.Button(master=navbar_frame, text='Buscar', command=lambda: PopulateManager(sframe_ref).search_item(ent_searchBar.get(), int(precision_slider.get())))
        btn_commitSearch = tb.Button(
            master=navbar_frame,
            text="Buscar",
            command=lambda: popmanagerRef.search_item(
                ent_searchBar.get(),
                resolution=int(precision_slider.get()),
                search_all_fields=btn_search_all_bool_var.get(),
            ),
        )
        btn_commitSearch.pack(**common_right)

        btn_search_all_bool_var = IntVar()
        btn_search_all_bool_var.set(1)
        # TODO: Incluir tooltip al pasar el raton por encima del checkbutton

        btn_radio_search_all_fields = tb.Checkbutton(
            master=navbar_frame,
            text="",
            variable=btn_search_all_bool_var,
            onvalue=1,
            offvalue=0,
        )
        ttip_search_all = ToolTip(
            btn_radio_search_all_fields,
            text="Si esta activada, buscara en todos los campos disponibles (notas, fabricante, etc...)",
            bootstyle=(PRIMARY, INVERSE),
        )
        btn_radio_search_all_fields.pack(**common_right)

        value_searchBar = StringVar()
        ent_searchBar = tb.Entry(master=navbar_frame, textvariable=value_searchBar)
        ent_searchBar.pack(**common_right)

        # Resolucion de busqueda
        def slider(e):
            precision_lbl.config(text=f"Precision: {int(precision_slider.get())}")

        precision_slider = tb.Scale(
            master=navbar_frame,
            orient="horizontal",
            length=135,
            from_=35,
            to=100,
            value=60,
            command=slider,
        )
        precision_slider.pack(**common_right, padx=10)

        precision_lbl = tb.Label(
            master=navbar_frame, text=f"Precision: {int(precision_slider.get())}"
        )
        ttip_precision_lbl = ToolTip(
            precision_lbl,
            text="Cuanto menor sea el valor, menos estricta sera la busqueda.",
            bootstyle=(PRIMARY, INVERSE),
        )
        ttip_scale_lbl = ToolTip(
            precision_slider,
            text="Cuanto menor sea el valor, menos estricta sera la busqueda.",
            bootstyle=(PRIMARY, INVERSE),
        )
        precision_lbl.pack(**common_right, padx=5)
