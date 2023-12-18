from tkinter import *
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from logica.DrawThumb import DrawThumb

class ThumbGen():
    common_options = {'fill':'x', 'expand':True, 'anchor':'center', 'pady':4}
    maxlengthstr = 20
    def __init__(self, par) -> None:
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title('Generador de etiquetas')
        
        mainFrame = tb.Frame(master=self.newWindow, padding=5)
        mainFrame.pack(fill='both', expand=True, padx=10, pady=10)
        
        cajon_num_lbl_frame = tb.LabelFrame(master=mainFrame, text='Cajon num (1-99)')
        cajon_num_lbl_frame.pack(side='top', **self.common_options)
        
        self.cajon_num_var = IntVar()
        cajon_num_ent = tb.Entry(master=cajon_num_lbl_frame, textvariable=self.cajon_num_var, width=5)
        cajon_num_ent.pack(side='top', **self.common_options)
        
        cajon_nombre_lbl_frame = tb.LabelFrame(master=mainFrame, text='Nombre (Max 15 car.)')
        cajon_nombre_lbl_frame.pack(side='top', **self.common_options)
        
        self.cajon_nombre_var = StringVar()
        cajon_nombre_ent = tb.Entry(master=cajon_nombre_lbl_frame, textvariable=self.cajon_nombre_var)
        cajon_nombre_ent.pack(side='top', **self.common_options)
        
        cajon_modelo_lbl_frame = tb.LabelFrame(master=mainFrame, text='Modelo (Max 20 car.)')
        cajon_modelo_lbl_frame.pack(side='top', **self.common_options)
        
        self.cajon_modelo_var = StringVar()
        cajon_modelo_ent = tb.Entry(master=cajon_modelo_lbl_frame, textvariable=self.cajon_modelo_var)
        cajon_modelo_ent.pack(side='top', **self.common_options)
        
        imagen_lbl_frame = tb.LabelFrame(master=mainFrame, text='Imagen (PNG/JPG)')
        imagen_lbl_frame.pack(side='top', **self.common_options)
        
        self.imagen_filename_var = StringVar()
        self.imagen_filename_var.set("Sin imagen")
        imagen_filename_lbl = tb.Label(master=imagen_lbl_frame, textvariable=self.imagen_filename_var)
        imagen_filename_lbl.pack(side='top', **self.common_options)
        imagen_select_btn = tb.Button(master=imagen_lbl_frame, text='Selecciona una imagen', command=lambda: self.pick_file(imagen_filename_var))        
        imagen_select_btn.pack(side='top', **self.common_options)
        
        control_lbl_frame = tb.LabelFrame(master=mainFrame, text='Acciones')
        control_lbl_frame.pack(side='top', **self.common_options)
        
        generateImg_btn = tb.Button(master=control_lbl_frame, text='Generar etiqueta', bootstyle='info', command=lambda: self.genImage())
        generateImg_btn.pack(side='top', **self.common_options)
        
    
    def trim_string(self, string, maxlen = maxlengthstr):
        return string if len(string) <= maxlen else f'...{string[-maxlen:]}'
        
    def pick_file(self, varToChange):
        filepicker = filedialog.askopenfilename(initialdir='./', title='Selecciona una imagen', filetypes=(('png files','*.png'),('all files', '*.*')))
        varToChange.set(self.trim_string(filepicker))
        
    def is_all_input_valid(self):
        num_ok = type(self.cajon_num_var.get()) == int and 1 <= self.cajon_num_var.get() <= 99
        name_ok = 3 <= len(self.cajon_nombre_var.get()) <= 15
        model_ok = 3 <= len(self.cajon_modelo_var.get()) <= 20
        if num_ok and name_ok and model_ok:
            return True
        else:
            return False
    
    def genImage(self):
        if not self.is_all_input_valid():
            print('Error en inputs, no cumplen los requisitos.')
            return
        else:
            print('Generando imagen')