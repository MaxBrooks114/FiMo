from os import listdir
from os.path import isfile, isdir, join
import os
import tkinter

# global dict of files, key is  file types, values will be array or tuple of
# files themselves.

#create gui to list directories then based on directory list all extensions
# in that directory

#
path = "/Users/maxbrooks"



#create folders based on extension

#populate folders with the files of that extension



files = {}




os.chdir(path)

file_types = []

#use a list comp to get a list of files in the downloads folder
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
  file_type = file.split(".")[-1]
  if file_type not in file_types:
      file_types.append(file_type)

print(file_types)

print(os.listdir(path))


m_window = tkinter.Tk()
m_window.title('FiMo Folder Cleanup Tool')
m_window.geometry('1024x768')
m_window.columnconfigure(0, weight=2)
m_window.columnconfigure(1, weight=2)
m_window.columnconfigure(2, weight=2)
m_window.columnconfigure(3, weight=1)
m_window.rowconfigure(0, weight=1)
m_window.rowconfigure(1, weight=5)
m_window.rowconfigure(2, weight=5)
m_window.rowconfigure(3, weight=1)

# ===labels===
tkinter.Label(m_window, text="Directories").grid(row=0, column=0)
tkinter.Label(m_window, text="Folders").grid(row=0, column=1)
tkinter.Label(m_window, text="Extensions").grid(row=0, column=2)

# === Directories listbox ===
directories_list = tkinter.Listbox(m_window)
directories_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
directories_list.config(border=2, relief='sunken')
for d in os.listdir(path):
    if isdir(join(path, d)) and not d.startswith('.'):
        directories_list.insert('end', d)


    # === Folders listbox ===
folders_list = tkinter.Listbox(m_window)
folders_list.grid(row=1, column=1, sticky='nsew', rowspan=2, padx=(30, 0))
folders_list.config(border=2, relief='sunken')

# === Extensions listbox ===
extensions_list = tkinter.Listbox(m_window)
extensions_list.grid(row=1, column=2, sticky='nsew', rowspan=2, padx=(30, 0))
extensions_list.config(border=2, relief='sunken')

m_window.mainloop()











