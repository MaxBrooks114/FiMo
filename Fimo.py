from os import listdir
from os.path import isfile, join
import os

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













