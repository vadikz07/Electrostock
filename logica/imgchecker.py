import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from logica.constants_data import *
from PIL import Image, ImageTk
import urllib.request
from urllib import error
import io


class ImgCheckerGUI:
    items_name_img = []
    imgs_problems = []

    def __init__(self, par, arr_of_items=[]) -> None:
        self.root = par
        self.arr_of_items = arr_of_items
        self.generate_tuple_arr()
        #TODO: Crear interfaz para mostrar las imagenes con problemas.
        
    def generate_tuple_arr(self):
        for item in self.arr_of_items:
            if (
                item["imagen"] != ""
            ):  # si tiene contenido, agregar nombre y url al items_name_img
                self.items_name_img.append((item["nombre"], item["imagen"]))
        self.check_all_imgs()

    def check_all_imgs(self):
        for tup in self.items_name_img:
            try:
                with urllib.request.urlopen(tup[1]) as u:
                    u.read()
            except error.HTTPError:
                self.imgs_problems.append(tup)
        self.report_failures()
        
    def report_failures(self):
        for item in self.imgs_problems:
            print(item)
