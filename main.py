from tkinter import *
from tkinter.ttk import *
from path_resolver import *
from hash_generator import hash_file

def generate_checksum() -> None:
    hash.set(hash_file(get_chosen_file_path(), selected_algorithm.get()))

root = Tk()
root.title('Hasher')
root.minsize(400, 100)
root.resizable(False, False)

ALGORITHMS = ['md5', 'sha256', 'sha512']
selected_algorithm = StringVar()
algorithms_option_menu = OptionMenu(root, selected_algorithm, ALGORITHMS[0], *ALGORITHMS)

hash = StringVar()
hash_label = Label(root, textvariable=hash).pack()
algorithms_option_menu.pack()

Button(root, text='Generate checksum', command=generate_checksum).pack()

root.mainloop()
