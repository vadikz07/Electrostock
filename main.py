import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from interfaz.componentes.navbar import NavBarTop
from interfaz.componentes.toolbar import Toolbar

from logica.populateList import PopulateManager
from logica.getDataLogic import getData, modify_item

root = tb.Window(themename="superhero")
root.title("Electrostock")
wid = 1050
hei = 1000
root.geometry(f"{wid}x{hei}")
root.update_idletasks()
root.withdraw()
root.geometry(
    f"+{(root.winfo_screenwidth() - wid) // 2}+{(root.winfo_screenheight() - hei) // 2}"
)
root.deiconify()

# sizing variables
sml_padding = 10

# frame navbar
fr_navbar = tb.Frame(master=root, bootstyle="light")
fr_navbar.pack(padx=5, pady=5, side="top", anchor="nw", expand=False, fill="x")
# frame inferior, contiene toolbar izquierdo y info de los items
fr_lower = tb.Frame(master=root)
fr_lower.pack(fill="x", anchor="nw", expand=False)

fr_left_toolbar = tb.Frame(master=fr_lower, padding=sml_padding)
fr_left_toolbar.pack(side="left", anchor="nw", fill="y", expand=False)

sf_info_items = ScrolledFrame(master=fr_lower, autohide=True, height=hei - 120)
sf_info_items.pack(fill="both", expand=True, padx=10, pady=10, anchor="nw")


# frame statusbar
fr_statusbar = tb.Frame(master=root, relief="sunken", padding=sml_padding)
fr_statusbar.pack(fill="x", side="bottom", anchor="s")

# Widgets del navbar
NavBarTop(fr_navbar, sf_info_items)
Toolbar(fr_left_toolbar, root, sf_info_items)


# Insercion item desde itemslist al arrancar el programa
PopulateManager(sf_info_items, getData()).visualize_all()


status_lbl = tb.Label(
    master=fr_statusbar, text="ElectroStock - vadikz@gmail.com - 2023"
)
status_lbl.pack(anchor="e", expand=True, fill="x")


root.update()
root.mainloop()

modify_item('24330628-a835-4777-8661-c17e4cc26180',{
    "uuid": "24330628-a835-4777-8661-c17e4cc26180",
    "nombre": "Prueba mod",
    "modelo": "Probando",
    "fabricante": "",
    "cantidad": "11",
    "cantidadAviso": "10",
    "cantidadMaxima": "100",
    "datasheet": "",
    "notas": "Interruptores variados, incluye SMD, de palanca, y mecanicos de teclado.",
    "fechaInsercion": "25/12/2023",
    "localizacion": 1
  })

root.mainloop()
