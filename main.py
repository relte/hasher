from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from path_resolver import *
from hash_generator import hash_file
import config
import path_resolver


class Application:

    def __init__(self, master):
        self.master = master
        if config.is_dev_environment():
            master.title('Hasher [dev environment]')
        else:
            master.title('Hasher')

        master.maxsize(400, 100)
        master.minsize(400, 100)
        master.resizable(False, False)
        master.iconbitmap(get_icon_path())
        self.center_window(master)
        self.frame = Frame(master)

        algorithms = ['md5', 'sha256', 'sha512']
        self.selected_algorithm = StringVar()
        self.algorithms_option_menu = OptionMenu(self.frame, self.selected_algorithm, algorithms[0], *algorithms)

        self.hash = StringVar()
        self.hash_entry = Entry(self.frame, state='readonly', textvariable=self.hash, width=60)

        self.is_in_clipboard = StringVar()
        self.is_in_clipboard_label = Label(self.frame, textvariable=self.is_in_clipboard)

        self.generate_hash_button = Button(self.frame, text='Generate checksum', command=self.generate_hash)

        self.frame.pack()
        self.hash_entry.pack()
        self.algorithms_option_menu.pack()
        self.is_in_clipboard_label.pack()
        self.generate_hash_button.pack()

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def generate_hash(self) -> None:
        file_path = path_resolver.get_selected_file_path() if not config.is_dev_environment() else path_resolver.get_test_file_path()

        self.hash.set(hash_file(file_path, self.selected_algorithm.get()))
        self.check_clipboard_match()

    def check_clipboard_match(self) -> None:
        is_hash_the_same = self.hash.get() == self.master.clipboard_get()
        self.is_in_clipboard.set('The hash matches clipboard!' if is_hash_the_same else 'The hash does not match clipboard!')


def main():
    root = Tk()

    try:
        app = Application(root)
        app.generate_hash()
        app.check_clipboard_match()
        root.mainloop()
    except:
        messagebox.showerror('Hasher', 'Could not run the application')

if __name__ == '__main__':
    main()
