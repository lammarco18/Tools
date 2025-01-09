import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import tkinter as tk
from numpy import exp
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from tkinter.ttk import Combobox
import filecmp
import os.path

# ---- GUI ----

root = Tk()
root.title("Folder comparison")
root.geometry('600x500')
root.resizable(False, False)

def input():
    global dir1
    dir1 = filedialog.askdirectory()
    input_entry.delete(1, END)  # Remove current text in entry
    input_entry.insert(0, dir1)  # Insert the 'path'


def output():
    global dir2
    dir2 = filedialog.askdirectory()
    output_entry.delete(1, END)  # Remove current text in entry
    output_entry.insert(0, dir2)  # Insert the 'path'
    Compare.config(state="normal")


def difference(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]


def compare():
    my_listbox_in.delete(0, 'end')
    my_listbox_out.delete(0, 'end')
    dir1_files = []
    # dir1_path = []
    dir2_files = []
    # dir2_path = []
    for parent_path, _, filenames in os.walk(dir1):
        for f in filenames:
            # print(os.path.join(parent_path, f))
            dir1_files.append(f)
            # dir1_path.append(os.path.join(parent_path, f))
    for parent_path, _, filenames in os.walk(dir2):
        for f in filenames:
            # print(os.path.join(parent_path, f))
            dir2_files.append(f)
            # dir2_path.append(os.path.join(parent_path, f))
    diff_files = difference(dir1_files, dir2_files)
    # diff_path = difference(dir1_path, dir2_path)
    dir1_only = diff_files[0]
    # dir1_only_path = diff_path[0]
    dir2_only = diff_files[1]
    # dir2_only_path = diff_path[1]
    # print(dir1_only_path)
    # print(dir2_only_path)
    # dirs_cmp = filecmp.dircmp(dir1, dir2)
    # common_files = ', '.join(dirs_cmp.common)
    # print('Common files: '+ common_files)
    # dir1_only = ', '.join(dirs_cmp.left_only)
    # dir1_only = dirs_cmp.left_only
    for i in range(len(dir1_only)):
         my_listbox_in.insert(my_listbox_in.size() + 1, dir1_only[i])
    # dir2_only = ', '.join(dirs_cmp.right_only)
    # dir2_only = dirs_cmp.right_only
    for i in range(len(dir2_only)):
         my_listbox_out.insert(my_listbox_out.size() + 1, dir2_only[i])

top_frame = Frame(root)
bottom_frame = Frame(root)
space_frame = Frame(root)
line = Frame(root, height=1, width=400, bg="grey80", relief='groove')

input_path = Label(top_frame, text="Input Folder:")
input_entry = Entry(top_frame, text="", width=80)
browse1 = Button(top_frame, text="Browse", command=input)

output_path = Label(bottom_frame, text="Output Folder:")
output_entry = Entry(bottom_frame, text="", width=80)
browse2 = Button(bottom_frame, text="Browse", command=output)

Compare = Button(bottom_frame, command=compare, text='Compare Folders')

top_frame.pack(side=TOP)
line.pack(pady=10)
bottom_frame.pack(side=TOP)
space_frame.pack(side=BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

# Create the panes and frames
vertical_pane = ttk.PanedWindow(root, orient=VERTICAL)
vertical_pane.pack(side=BOTTOM)
horizontal_pane = ttk.PanedWindow(vertical_pane, orient=HORIZONTAL)
vertical_pane.add(horizontal_pane)
input_frame = ttk.Labelframe(horizontal_pane, text="Only in Input Folder")
input_frame.columnconfigure(1, weight=1)
output_frame = ttk.Labelframe(horizontal_pane, text="Only in Output Folder")
output_frame.columnconfigure(1, weight=1)
horizontal_pane.add(input_frame, weight=1)
horizontal_pane.add(output_frame, weight=1)

my_listbox_in = Listbox(input_frame, width=40)
my_listbox_in.pack(pady=5)

my_listbox_out = Listbox(output_frame, width=40)
my_listbox_out.pack(pady=5)

Compare.pack(pady=20, fill=X)
Compare.config(state="disabled")

space = Label(space_frame, text="M. Lamberti")
space.pack(pady=0)

root.mainloop()