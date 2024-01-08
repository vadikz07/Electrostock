import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from logica.constants_data import *
from PIL import Image, ImageTk
import urllib.request
from urllib import error
from interfaz.componentes.editItemForm import EditItemForm


class SingleReport:
    xpadding = 10
    ypadding = 5
    def __init__(self,par, tup_data, popmanagerRef) -> None:
        self.tup_data = tup_data
        self.main_container = tb.Frame(master=par)
        self.main_container.pack(side='top', expand=True, fill='x')
        self.name_lbl = tb.Label(master=self.main_container, text=self.tup_data[1])
        self.name_lbl.grid(row=0, column=0, padx=self.xpadding, pady=self.ypadding)
        self.img_lbl_trimmed = tb.Label(master=self.main_container, text=self.tup_data[2][-20:])
        self.img_lbl_trimmed.grid(row=0, column=1, padx=self.xpadding, pady=self.ypadding)
        self.btn_edit = tb.Button(master=self.main_container, text='Editar', bootstyle='info', command=lambda:
            EditItemForm(
                par=par,
                uuid_to_modify=self.tup_data[0],
                popmanagerRef=popmanagerRef, #TODO: Agregar referencia a popmanager
            ))
        self.btn_edit.grid(row=0, column=2, padx=self.xpadding, pady=self.ypadding)
        

class ImgCheckerGUI:
    #Estructura del tuple , 0-uuid, 1-nombre, 2-imagen
    
    def __init__(self, par, arr_of_items=[],popmanagerRef=None) -> None:
        self.items_name_img = []
        self.root = par
        self.imgs_problems = []
        self.arr_of_items = arr_of_items
        self.popmanagerRef = popmanagerRef
        self.generate_tuple_arr()
        # TODO: Crear interfaz para mostrar las imagenes con problemas.
        self.generate_gui()

    def generate_gui(self):
        common_options = {"fill": "x", "expand": True, "anchor": "center", "pady": 4}
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title("Comprobador de imagenes")
        self.newWindow.geometry("+%d+%d" % ((self.root.winfo_screenwidth() - self.newWindow.winfo_reqwidth()) / 2, (self.root.winfo_screenheight() - self.newWindow.winfo_reqheight() - 600) / 2))
        mainFrame = tb.Frame(master=self.newWindow, padding=5)
        mainFrame.pack(fill="both", expand=True, padx=10, pady=10)

        self.results_lblFrame = tb.LabelFrame(master=mainFrame, text="Resultados")
        self.results_lblFrame.pack(**common_options)
        
        for tup_item in self.get_imgs_problems():
            # print(tup_item)
            self.generate_single_gui_report(tup_item)
        

    def generate_single_gui_report(self, tup_data):
        SingleReport(par=self.results_lblFrame, tup_data=tup_data, popmanagerRef=self.popmanagerRef)
    
    def generate_tuple_arr(self):
        for item in self.arr_of_items:
            if (
                item["imagen"] != ""
            ):  # si tiene contenido, agregar nombre y url al items_name_img
                self.items_name_img.append((item['uuid'],item["nombre"], item["imagen"]))

    def get_imgs_problems(self) -> list:
        
        for tup in self.items_name_img:
            try:
                with urllib.request.urlopen(tup[2]) as u:
                    u.read()
            except error.HTTPError:
                self.imgs_problems.append(tup)
        return self.imgs_problems

    def report_failures(self):
        for item in self.imgs_problems:
            print(item)
