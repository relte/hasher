import os, sys
if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import path_resolver
import hash_generator
import config
import views


class MasterController:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master)

        self.hash_entry = views.HashEntry(self.frame)
        self.algorithms_option_menu = views.AlgorithmsOptionMenu(self.frame)
        self.is_in_clipboard_label = views.IsInClipboardLabel(self.frame)
        self.generate_hash_button = views.GenerateHashButton(self.frame)

        self.frame.pack()
        self.hash_entry.pack()
        self.algorithms_option_menu.pack()
        self.is_in_clipboard_label.pack()
        self.generate_hash_button.pack()

        self.generate_hash_button.bind('<Button>', self.generate_hash)

        self.generate_hash(None)
        self.check_clipboard_match()

    def generate_hash(self, event):
        if config.is_dev_environment():
            file_path = path_resolver.get_test_file_path()
        else:
            file_path = path_resolver.get_selected_file_path()

        self.hash_entry.setValue(hash_generator.get_file_hash(file_path, self.algorithms_option_menu.getValue()))
        self.check_clipboard_match()

    def check_clipboard_match(self):
        try:
            is_matching = self.hash_entry.isValue(self.master.clipboard_get())
        except:
            is_matching = False

        if is_matching:
            self.is_in_clipboard_label.setSuccessful()
        else:
            self.is_in_clipboard_label.setUnsuccessful()


def main():
    if config.is_dev_environment():
        run(config.get_name() + ' [dev environment]')
    else:
        try:
            run(config.get_name())
        except:
            tk.messagebox.showerror(config.get_name(), 'Could not run the application')


def run(title):
    master = views.MasterWindow(title, path_resolver.get_icon_path())
    MasterController(master)
    master.mainloop()


if __name__ == '__main__':
    main()
