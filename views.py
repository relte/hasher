import tkinter as tk
import tkinter.ttk as ttk


class MasterWindow(tk.Tk):

    def __init__(self, title, icon_path):
        super().__init__()

        self.title(title)
        self.maxsize(400, 100)
        self.minsize(400, 100)
        self.resizable(False, False)
        self.iconbitmap(icon_path)
        self.center()

    def center(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class AlgorithmsOptionMenu(ttk.OptionMenu):

    def __init__(self, frame):
        algorithms = ['md5', 'sha256', 'sha512']
        self.selected_algorithm = tk.StringVar()
        super().__init__(frame, self.selected_algorithm, algorithms[0], *algorithms)

    def getValue(self):
        return self.selected_algorithm.get()


class HashEntry(ttk.Entry):

    def __init__(self, frame):
        self.hash = tk.StringVar()
        super().__init__(frame, state='readonly', textvariable=self.hash, width=60)

    def getValue(self):
        return self.hash.get()

    def setValue(self, value):
        self.hash.set(value)

    def isValue(self, value):
        return self.getValue() == value


class IsInClipboardLabel(ttk.Label):

    def __init__(self, frame):
        self.is_in_clipboard = tk.StringVar()
        super().__init__(frame, textvariable=self.is_in_clipboard)

    def setSuccessful(self):
        self.is_in_clipboard.set('The hash matches clipboard!')

    def setUnsuccessful(self):
        self.is_in_clipboard.set('The hash does not match clipboard!')


class GenerateHashButton(ttk.Button):

    def __init__(self, frame):
        super().__init__(frame, text='Generate checksum')
