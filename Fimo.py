from os import listdir
from os.path import isfile, isdir, join
import os
import tkinter

# global dict of files, key is file types, values will be array or tuple of
# files themselves.

# create gui to list directories then based on directory list all extensions
# in that directory

#
my_path = "/Users/maxbrooks"


class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL,
                                           command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1,
             **kwargs):

        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
                     columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, stick='nse',
                            rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):
    def __init__(self, window, path, **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_value = None
        self.link_field = None
        self.path = path
        self.bind('<<ListboxSelect>>', self.on_select)

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field=None):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):

        self.link_value = link_value

        if link_value and self.link_field == "files":
            self.clear()
            for d in os.listdir("{}/{}".format(my_path, link_value)):
                self.insert('end', d)

        elif link_value and self.link_field == "extensions":
            self.clear()
            file_types = []
            files = [f for f in listdir("{}/{}".format(my_path, link_value)) if
                     isfile(join("{}/{}".format(my_path, link_value), f))]

            for file in files:
                file_type = file.split(".")[-1]
                if file_type not in file_types:
                    file_types.append(file_type)
                    self.insert('end', file_type)
        else:
            for d in os.listdir(my_path):
                if isdir(join(my_path, d)) and not d.startswith('.'):
                    self.insert('end', d)

    def on_select(self):
        if self.linked_box:
            print("self is event.widget")
            index = self.curselection()[0]
            value = self.get(index),
            chosen_path = value[0]

            self.linked_box.requery(chosen_path)


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
directories_list = DataListBox(m_window, my_path)
directories_list.grid(row=1, column=0, sticky='nsew', rowspan=1, padx=(30, 0))
directories_list.config(border=2, relief='sunken')
directories_list.requery()


# === File List listbox ===
folders_list = DataListBox(m_window, my_path)
folders_list.grid(row=1, column=1, sticky='nsew', rowspan=1, padx=(30, 0))
folders_list.config(border=2, relief='sunken')
directories_list.link(folders_list, "files")

# === Extensions listbox ===
extensions_list = DataListBox(m_window, my_path)
extensions_list.grid(row=1, column=2, sticky='nsew', rowspan=1, padx=(30, 0))
extensions_list.config(border=2, relief='sunken')
directories_list.link(extensions_list, "extensions")

m_window.mainloop()
