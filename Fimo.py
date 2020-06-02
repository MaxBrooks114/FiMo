from os import listdir
from os.path import isfile, join
import os
import tkinter



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


# global dict of files, key is  file types, values will be array or tuple of
# files themselves.

#create gui to list directories then based on directory list all extensions
# in that directory

#
path = "/Users/maxbrooks/downloads"



#create folders based on extension

#populate folders with the files of that extension



files = {}




os.chdir(path)

file_types = []

files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
  file_type = file.split(".")[-1]
  if file_type not in file_types:
      file_types.append(file_type)

print(file_types)



print(os.listdir(path))













