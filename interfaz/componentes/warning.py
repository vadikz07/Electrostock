import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

class WarningWindow:
    def __init__(self, par, msg="Default message", title='') -> None:
        self.messagebox = Messagebox.show_question(message=msg, title=title, buttons=['No:secondary', 'Yes:danger'])
                
    def return_response(self):
        return True if self.messagebox == 'Yes' else False