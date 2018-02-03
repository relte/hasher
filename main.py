from tkinter import *
from tkinter.ttk import *
from path_resolver import *
from hash_generator import hash_file

def generate_hash() -> None:
    hash.set(hash_file(get_chosen_file_path(), selected_algorithm.get()))
    check_clipboard_match()

def check_clipboard_match() -> None:
    is_hash_the_same = hash.get() == root.clipboard_get()
    is_in_clipboard.set('The hash matches clipboard!' if is_hash_the_same else 'The hash does not match clipboard!')

root = Tk()
root.title('Hasher')
root.minsize(400, 100)
root.resizable(False, False)

ALGORITHMS = ['md5', 'sha256', 'sha512']
selected_algorithm = StringVar()
algorithms_option_menu = OptionMenu(root, selected_algorithm, ALGORITHMS[0], *ALGORITHMS)

hash = StringVar()
hash_entry = Entry(root, state='readonly', textvariable=hash, width=60).pack()

algorithms_option_menu.pack()

is_in_clipboard = StringVar()
is_in_clipboard_label = Label(root, textvariable=is_in_clipboard).pack()

Button(root, text='Generate checksum', command=generate_hash).pack()

generate_hash()
check_clipboard_match()

root.mainloop()
