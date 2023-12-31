import ttkbootstrap as tb
from tkinter import *
from logica.populateList import PopulateManager
from logica.getDataLogic import get_list_status_containers


class Cell:
    def __init__(self, par, num: int = 0, isEmpty=bool, row=0, col=0) -> None:
        self.root = par
        self.num = num
        self.lbl = tb.Label(master=self.root, background="yellow", text=self.num)
        if isEmpty:
            self.lbl.config(background="gray")
        else:
            self.lbl.config(background="green")
        self.lbl.grid(row=row, column=col, sticky='ew', padx=1, pady=1)


class GridDisplay:
    def __init__(self, par, popmanagerRef: PopulateManager) -> None:
        self.columns = 10
        self.rows = 10
        self.root = par
        self.cells_frame = tb.LabelFrame(master=self.root, text="Contenidos")
        self.cells_frame.pack(pady=20)
        occupied, empty = get_list_status_containers()
        # print(occupied)
        # print(empty)
        self.lbls_placed = 1
        while self.lbls_placed <= 98:
            for row in range(self.rows):
                for col in range(self.columns):
                    if self.lbls_placed in occupied:
                        Cell(par=self.cells_frame, num=self.lbls_placed, isEmpty=False, row=row, col=col)
                    else:
                        Cell(par=self.cells_frame, num=self.lbls_placed, isEmpty=True, row=row, col=col)
                    self.lbls_placed += 1
                    if self.lbls_placed >=99:
                        break

