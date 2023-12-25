import ttkbootstrap as tb

class NotePopup:
    common_options_btm = {'side':'top','expand':True,'anchor':'center','padx':20, 'pady':20}
    def __init__(self, par, objectdata) -> None:
        self.objectdata = objectdata
        self.root = par
        self.newWindow = tb.Toplevel(self.root)
        self.newWindow.title('Lector de notas')
        
        self.main_container = tb.Frame(master=self.newWindow)
        self.main_container.pack()
        
        self.name_labelFrame = tb.LabelFrame(master=self.main_container, text='Nombre')
        self.name_labelFrame.pack(**self.common_options_btm, fill='x')
        
        self.name_lbl = tb.Label(master=self.name_labelFrame, text=objectdata['nombre'], font=("Arial", 20, "bold"), anchor='center')
        self.name_lbl.pack(**self.common_options_btm, fill='x')
        
        self.data_container = tb.LabelFrame(master=self.main_container, text='Notas')
        self.data_container.pack(**self.common_options_btm)
        
        self.note_text = tb.Text(master=self.data_container, height=5)
        self.note_text.insert(tb.END, self.objectdata['notas'])
        self.note_text.pack(**self.common_options_btm)
        self.note_text.config(state='disabled')
        
        self.control_frame = tb.LabelFrame(master=self.main_container, text='Acciones')
        self.control_frame.pack(**self.common_options_btm)        
        
        # self.update_btn = tb.Button(master=self.control_frame, text='Actualizar notas', bootstyle='warning', command=lambda: self.update_note() )
        # self.update_btn.pack(**self.common_options_btm, fill='x')
        
        self.close_btn = tb.Button(master=self.control_frame, text='Cerrar', bootstyle='danger', command=lambda: self.newWindow.destroy())
        self.close_btn.pack(**self.common_options_btm, fill='x')
        
    def update_note(self):
        print(f'Actualizando contenido de nota.')