import ttkbootstrap as tb
from ttkbootstrap.constants import *
from interfaz.componentes.navbar import NavBarTop
from interfaz.componentes.item import ItemShow
from interfaz.componentes.spacer import Spacer
from interfaz.componentes.toolbar import Toolbar
from data.itemlists import items

root = tb.Window(themename='superhero')
root.title('Electrostock')
root.geometry('900x700')

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

fr_info_items = tb.Frame(master=fr_lower, padding=sml_padding, bootstyle='secondary')
fr_info_items.pack(fill='x', expand=True, side='left', anchor='nw')

#frame statusbar
fr_statusbar = tb.Frame(master=root, relief='sunken',padding=sml_padding)
fr_statusbar.pack(fill='x', side='bottom', anchor='s')

# Widgets del navbar
NavBarTop(fr_navbar)

Toolbar(fr_left_toolbar)


#Insercion item desde itemslist
ItemShow(fr_info_items, items[0])
ItemShow(fr_info_items, items[1])
ItemShow(fr_info_items, items[2])
status_lbl = tb.Label(master=fr_statusbar, text='this is a test for the status bar')
status_lbl.pack(anchor='e')


root.mainloop()














root.mainloop()
