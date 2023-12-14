import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Spacer:
    def __init__(self, par) -> None:
        self.label = tb.Label(master=par,text='--------------------------', bootstyle='light')
        self.label.pack(fill='x', expand=True)
