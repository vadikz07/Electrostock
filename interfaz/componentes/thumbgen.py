from tkinter import *
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class ThumbGen():
    common_options = {'fill':'x', 'expand':True, 'anchor':'center', 'pady':4}
    maxlengthstr = 20
    def __init__(self, par) -> None:
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title('Generador de etiquetas')
        
        mainFrame = tb.Frame(master=self.newWindow, padding=5)
        mainFrame.pack(fill='both', expand=True, padx=10, pady=10)
        
        cajon_num_lbl_frame = tb.LabelFrame(master=mainFrame, text='Cajon num')
        cajon_num_lbl_frame.pack(side='top', **self.common_options)
        
        cajon_num_var = IntVar()
        cajon_num_ent = tb.Entry(master=cajon_num_lbl_frame, textvariable=cajon_num_var, width=5)
        cajon_num_ent.pack(side='top', **self.common_options)
        
        cajon_nombre_lbl_frame = tb.LabelFrame(master=mainFrame, text='Nombre')
        cajon_nombre_lbl_frame.pack(side='top', **self.common_options)
        
        cajon_nombre_var = StringVar()
        cajon_nombre_ent = tb.Entry(master=cajon_nombre_lbl_frame, textvariable=cajon_nombre_var)
        cajon_nombre_ent.pack(side='top', **self.common_options)
        
        imagen_lbl_frame = tb.LabelFrame(master=mainFrame, text='Imagen')
        imagen_lbl_frame.pack(side='top', **self.common_options)
        
        imagen_filename_var = StringVar()
        imagen_filename_var.set("Sin imagen")
        imagen_filename_lbl = tb.Label(master=imagen_lbl_frame, textvariable=imagen_filename_var)
        imagen_filename_lbl.pack(side='top', **self.common_options)
        imagen_select_btn = tb.Button(master=imagen_lbl_frame, text='Selecciona una imagen', command=lambda: self.pick_file(imagen_filename_var))        
        imagen_select_btn.pack(side='top', **self.common_options)
        
    
    def trim_string(self, string, maxlen = maxlengthstr):
        return string if len(string) <= maxlen else f'...{string[-maxlen:]}'
        
    def pick_file(self, varToChange):
        filepicker = filedialog.askopenfilename(initialdir='./', title='Selecciona una imagen', filetypes=(('png files','*.png'),('all files', '*.*')))
        varToChange.set(self.trim_string(filepicker))
        