from tkinter import *
import ttkbootstrap as tb
from logica.cli_wizard import Wololo
from logica.getDataLogic import *
from logica.getDataLogic import validateData
from uuid import uuid4
from interfaz.componentes.previewImg import PreviewWindow
from interfaz.componentes.previewImgstandalone import PreviewWindowSA

class NewItemForm:
    x_padd = 5
    width_entries_txt = 20
    width_entries_int = 4

    def __init__(self, par, popmanagerRef, default_box_num=1) -> None:
        self.popmanager = popmanagerRef
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title("Formulario de insercion")
        self.newWindow.geometry("+%d+%d" % ((self.root.winfo_screenwidth() - 800) / 2, (self.root.winfo_screenheight() - 800) / 2))
        self.list_entry_widgets = []
        self.main_container = tb.Frame(master=self.newWindow, padding=self.x_padd)
        self.main_container.pack()

        self.boxnum_lblframe = tb.LabelFrame(
            master=self.main_container, text="Cajon nº"
        )
        self.boxnum_lblframe.grid(row=0, column=0, sticky="w")
        self.boxnum_ent = tb.Spinbox(master=self.boxnum_lblframe, from_=1, to=96)
        self.boxnum_ent.insert(0,default_box_num)
        self.boxnum_ent.pack(side="left", expand=False, anchor="w")
        self.list_entry_widgets.append(self.boxnum_ent)

        self.name_lblframe = tb.LabelFrame(master=self.main_container, text="Nombre")
        self.name_lblframe.grid(row=0, column=1, sticky="ew")
        self.name_ent_var = StringVar()
        self.name_ent = tb.Entry(
            master=self.name_lblframe, textvariable=self.name_ent_var
        )
        self.name_ent.pack(side="right", fill="x", expand=True, anchor="w")
        self.list_entry_widgets.append(self.name_ent_var)



        self.model_lblframe = tb.LabelFrame(master=self.main_container, text="Modelo")
        self.model_lblframe.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.model_ent_var = StringVar()
        self.model_ent = tb.Entry(
            master=self.model_lblframe, textvariable=self.model_ent_var
        )
        self.model_ent.pack(side="left", fill="x", expand=True, anchor="w")
        self.list_entry_widgets.append(self.model_ent_var)

        self.maker_lblframe = tb.LabelFrame(master=self.main_container, text="Fabricante")
        self.maker_lblframe.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.maker_ent_var = StringVar()
        self.maker_ent = tb.Entry(
            master=self.maker_lblframe, textvariable=self.maker_ent_var
        )
        self.maker_ent.pack(side="left", fill="x", expand=True, anchor="w")
        self.list_entry_widgets.append(self.maker_ent_var)

        self.img_lblframe = tb.LabelFrame(master=self.main_container, text="URL Imagen")
        self.img_lblframe.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.img_ent_var = StringVar()
        self.img_ent = tb.Entry(
            master=self.img_lblframe, textvariable=self.img_ent_var
        )
        self.img_ent.pack(side="left", fill="x", expand=True, anchor="w")
        self.test_img_btn = tb.Button(master=self.img_lblframe, text='Probar imagen', command=lambda:(
                PreviewWindowSA(par=par,popmanagerRef=popmanagerRef,urlTest=self.img_ent_var.get()).show_image()
            ),bootstyle='info')
        self.test_img_btn.pack(side="left", expand=False, anchor="e")
        self.list_entry_widgets.append(self.img_ent_var)


        # Cantidades en un frame propio
        self.cant_frame = tb.LabelFrame(master=self.main_container, text="Cantidad")
        self.cant_frame.grid(row=4, column=0, columnspan=2, sticky="ew")
        # Hijos de cant-frame
        self.cant_act_lblframe = tb.LabelFrame(master=self.cant_frame, text="Actual")
        # self.cant_act_lblframe.grid(row=0, column=0)
        self.cant_act_lblframe.pack(
            side="left", padx=(0, 5), anchor="w", fill="x", expand=True
        )

        ##Entry del lblframe especifico para actual
        self.cant_act_entry_var = tb.Spinbox(master=self.cant_act_lblframe, from_=1, to=200)
        self.cant_act_entry_var.pack(side="top", fill="x")
        self.list_entry_widgets.append(self.cant_act_entry_var)
        
        # Segundo hijo de cant frame para maximo
        # self.cant_max_lblframe = tb.LabelFrame(master=self.cant_frame, text="Maximo")
        # self.cant_max_lblframe.grid(row=0, column=1)
        # self.cant_max_lblframe.pack(
        #     side="left", padx=(5, 5), anchor="center", fill="x", expand=True
        # )
        ##Entry para el maximo
        # self.cant_max_entry_var = tb.Spinbox(master=self.cant_max_lblframe, from_=1, to=200)
        # self.cant_max_entry_var.pack(side="top", fill="x")
        # self.list_entry_widgets.append(self.cant_max_entry_var)

        # Tercer hijo de cant frame para aviso
        self.cant_warn_lblframe = tb.LabelFrame(
            master=self.cant_frame, text="Avisar", bootstyle="warning"
        )
        # self.cant_warn_lblframe.pack(
        #     side="left", padx=(5, 0), anchor="e", fill="x", expand=True
        # )
        ##Entry para el aviso
        self.cant_warn_entry_var = tb.Spinbox(master=self.cant_warn_lblframe, from_=1, to=200)
        self.cant_warn_entry_var.insert(0,"1")
        # self.cant_warn_entry_var.pack(side="top", fill="x")
        self.list_entry_widgets.append(self.cant_warn_entry_var)

        # todo: continuar formulario con los datos de itemlist
        self.dsheet_lblframe = tb.LabelFrame(
            master=self.main_container, text="Datasheet"
        )
        self.dsheet_lblframe.grid(row=5, column=0, columnspan=2, sticky="ew")
        self.dsheet_ent_var = StringVar()
        self.dsheet_ent = tb.Entry(
            master=self.dsheet_lblframe, textvariable=self.dsheet_ent_var
        )
        self.dsheet_ent.pack(side="top", fill="x", expand=True)
        self.list_entry_widgets.append(self.dsheet_ent_var)

        self.notes_lblframe = tb.LabelFrame(master=self.main_container, text="Notas")
        self.notes_lblframe.grid(row=6, column=0, columnspan=2, sticky="ew")
        self.notes_scroll = tb.Scrollbar(
            master=self.notes_lblframe, orient="vertical", bootstyle="success round"
        )
        self.notes_text = tb.Text(
            master=self.notes_lblframe, height=4, yscrollcommand=self.notes_scroll.set
        )
        self.notes_text.pack(side="left", fill="x")
        self.notes_scroll.pack(side="right", fill="y")
        self.notes_scroll.config(command=self.notes_text.yview)

        # Fecha insercion
        self.date_lblframe = tb.LabelFrame(
            master=self.main_container, text="Fecha insercion"
        )
        self.date_lblframe.grid(row=7, column=0, columnspan=2, sticky="ew")
        self.testdate = tb.DateEntry(
            self.date_lblframe, bootstyle="info", firstweekday=0
        )
        self.testdate.pack()

        self.control_lblframe = tb.LabelFrame(
            master=self.main_container, text="Acciones"
        )
        self.control_lblframe.grid(row=10, column=0, columnspan=2, sticky="ew")
        self.clear_data_btn = tb.Button(
            master=self.control_lblframe, text="Limpiar campos", bootstyle="danger"
        )
        self.clear_data_btn.pack(side="left", padx=(0, 5), anchor="w", fill="x")

        self.add_dataDB_btn = tb.Button(
            master=self.control_lblframe,
            text="Agregar componente",
            bootstyle="success",
            command=self.collect_data,
        )
        self.add_dataDB_btn.pack(side="right", padx=(5, 0), anchor="e", fill="x")

        self.cli_btn = tb.Button(
            master=self.control_lblframe,
            text="CLI",
            bootstyle="info",
            command=lambda: Wololo().main_wizard()
        )
        self.cli_btn.pack(side="right", padx=(5, 0), anchor="e", fill="x")

        self.fr_statusbar = tb.Frame(
            master=self.main_container, relief="sunken", padding=(10, 10)
        )
        self.fr_statusbar.grid(row=100, column=0, columnspan=3, sticky="ew")

        self.status_lbl_var = StringVar()
        self.status_lbl_var.set("-")
        self.status_lbl = tb.Label(
            master=self.fr_statusbar, textvariable=self.status_lbl_var
        )
        self.status_lbl.pack(anchor="center", fill="x", expand=True)
        

    def collect_data(self) -> dict:
        print(f"Ejecutando collect data")
        data_dict = {}
        data_dict["uuid"] = str(uuid4())
        data_dict["nombre"] = self.name_ent_var.get()
        data_dict["modelo"] = self.model_ent_var.get()
        data_dict["imagen"] = self.img_ent_var.get()
        data_dict["fabricante"] = self.maker_ent_var.get()
        data_dict["cantidad"] = self.cant_act_entry_var.get()
        # data_dict["cantidadAviso"] = self.cant_warn_entry_var.get()
        # data_dict["cantidadMaxima"] = self.cant_max_entry_var.get()
        data_dict["datasheet"] = self.dsheet_ent_var.get()
        data_dict["notas"] = self.notes_text.get("1.0", "end-1c")
        data_dict["fechaInsercion"] = self.testdate.entry.get()
        try:
            data_dict["localizacion"] = int(self.boxnum_ent.get())
        except ValueError:
            data_dict["localizacion"] = ""

        if validateData(
            data_dict
        ):  
            self.result_save = saveData(data_dict, popmanagerRef=self.popmanager)
            self.status_lbl_var.set("Datos insertados correctamente")
            if self.result_save:
                self.clear_ent_fields()
        else:  # fallo en validacion
            self.status_lbl_var.set("Error al validar datos")

    def clear_ent_fields(self):
        for ent in self.list_entry_widgets:
            try:
                ent.set("")
            except Exception as e:
                print(f"Problema al borrar campos: {e}")
        self.notes_text.delete("1.0", "end")
