# FiMo
A python module to organize your files on your computer 


This module is for people whose download folders are just laden with junk they don't even remeber downloading. It is completely OS agnostic (but only tested on a mac). It will probably save you around 30 seconds of time, but it was fun to make!

## What it does ## 
The program takes the loose files (not in a folder) of an extension of your choice and moves them all into another folder in that same directory titled with the extension you chose. Have a bunch of loose pdfs in your downloads folder? Now all of them are in a folder labeled 'pdf' in that same directory. 

## How to use ###
fork and download the code, run it from your command line or your ide. The first column will automatically populate with your home directory. Using the "choose directory" button will populate that first column with all of the subdirectories in te folder you chose. Now choosing a selection in the first column will populate both the middle and right columns. The middle column will fill with all of the folders and loose files in the subdirectory you chose. The right most column will fill the types of extensions of all the loose files. Selecting one of those extensions and hitting the 'create folder' button will begin the process. You will be prompted with a decision to 1) make the folder titled {extension} and it will 2)begin to populate that folder with all the {extension} files. Note that if the folder already exists only step 2 will occur.


