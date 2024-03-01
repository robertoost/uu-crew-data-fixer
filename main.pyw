#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import tkinter as tk
from tkinter import filedialog
import sys
import os


# Code by @robertoost 
# Written for my friend Arjen Ritzerfeld

def main():
    """ Main program """

    # Hide the standard application window that is empty in our case.
    #
    root = tk.Tk()
    root.withdraw()

    # Icon for the application.
    # https://stackoverflow.com/questions/53587322/how-do-i-include-files-with-pyinstaller
    #
    icopath = os.path.join(sys._MEIPASS, "favicon.ico") if getattr(sys, 'frozen', False) else "favicon.ico"
    root.iconbitmap(icopath)

    # Prompt the user for a file to fix, prepare a new filename.
    #
    filename = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")], title="UU Crew Data fixer 9000")
    new_filename = filename.replace(".xls", "-fixed.xls").split("/")[-1]

    if filename == '':
        return

    df = pd.read_excel(filename)
    
    # Clean up the labels we want to keep at the start of each row.
    #
    new_start_labels = ["FormFiller", "Programme", "SpecifyProgramme"]
    start_labels = df.columns.values[5:8]
    df.rename(columns=dict(zip(start_labels, new_start_labels)), inplace=True)

    # List of labels that will be the same for each person.
    new_labels = ['Role', 'FirstName', 'LastName', 'Email', 'Phone', 'Diet', 'DietSpecify', 'Workstatus', 'ColleagueRole', 'SpecifyColleagueRole']

    # We start at "rol1"
    startindex = 8
    increment = len(new_labels) + 1

    # List with columns that we intend to remove.
    #
    drop_indices = [1,2,3,4]

    # Loop over the entire dataframe, incrementing by the number of cells per person.
    #
    for i in range(0, 9):
        index = startindex + (increment * i)

        # Rename the labels to a numbered format.
        #
        labels = df.columns.values[index:index+increment-1]
        new_labels_indexed = [f"{i}_{label}" for label in new_labels]
        renamer = dict(zip(labels, new_labels_indexed))
        df.rename(columns=renamer, inplace=True)

        # Flag the "add_another_person" columns for removal.
        #
        if i != 0:
            drop_indices.append(index - 1)

    # Drop all columns we've previously chosen to remove.
    #
    df.drop(df.columns[drop_indices], axis=1, inplace=True)

    # Code taken from:
    # https://stackoverflow.com/questions/56776539/how-to-i-convert-a-pandas-dataframe-row-into-multiple-rows
    # And altered for this file. level_1 changed to level_4 because we include 3 extra indices.
    #
    df.set_index(['_fd_id', "FormFiller", "Programme", "SpecifyProgramme"], inplace=True)
    df.columns = pd.MultiIndex.from_arrays(zip(*df.columns.str.split('_')))
    df = df.stack([0]).reset_index().drop('level_4', axis=1)
    df.to_excel(new_filename)
    
    return 0

if __name__ == "__main__":
    main()