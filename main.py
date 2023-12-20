import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from interfaz.componentes.navbar import NavBarTop
from interfaz.componentes.item import ItemShow
from interfaz.componentes.toolbar import Toolbar

from logica.populateList import PopulateManager

from data.itemlists import items

root = tb.Window(themename='superhero')
root.title('Electrostock')
wid = 950
hei = 1000
root.geometry(f'{wid}x{hei}')

#sizing variables
sml_padding = 10;

#frame navbar
fr_navbar = tb.Frame(master=root, bootstyle='light')
fr_navbar.pack(padx=5, pady=5,side='top', anchor='nw',expand=False, fill='x')
#frame inferior, contiene toolbar izquierdo y info de los items
fr_lower = tb.Frame(master=root)
fr_lower.pack(fill='x', anchor='nw',expand=False)

fr_left_toolbar = tb.Frame(master=fr_lower, padding=sml_padding)
fr_left_toolbar.pack(side='left', anchor='nw', fill='y', expand=False)

sf_info_items = ScrolledFrame(master=fr_lower,autohide=True, height=hei-120)
sf_info_items.pack(fill='both',expand=True, padx=10, pady=10, anchor='nw')


#frame statusbar
fr_statusbar = tb.Frame(master=root, relief='sunken',padding=sml_padding)
fr_statusbar.pack(fill='x', side='bottom', anchor='s')

# Widgets del navbar
NavBarTop(fr_navbar, sf_info_items)
Toolbar(fr_left_toolbar)


#Insercion item desde itemslist al arrancar el programa
PopulateManager(sf_info_items)



status_lbl = tb.Label(master=fr_statusbar, text='this is a test for the status bar')
status_lbl.pack(anchor='e')

root.update()
root.mainloop()














root.mainloop()
