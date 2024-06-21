import tkinter as tk
from tkinter import *
from tkinter.ttk import *

import pandas as pd

# Assuming the `pals` module provides access to your Character objects:
# import pals  # Adapt import if necessary

# Function to update the listbox based on pandas DataFrame
def update_listbox(dataframe):
    listbox.delete(0, tk.END)  # Clear existing items to avoid duplicates
    for pal_name in dataframe['pal_name']:
        listbox.insert(tk.END, pal_name)

# Function to get selected pal names from the listbox
def get_selected_pals():
    selected_indices = listbox.curselection()
    if not selected_indices:
        return []  # Handle case where no items are selected
    return [listbox.get(index) for index in selected_indices]

# Function to calculate summary statistics for selected pals (replace "stat_column" if needed)
def calculate_summary_stats(dataframe, selected_pals):
    if not selected_pals:
        return "No pals selected!"

    # Filter DataFrame based on selected pal names
    filtered_df = dataframe[dataframe['pal_name'].isin(selected_pals)]

    # Filter numeric columns for summary
    numeric_cols = filtered_df.select_dtypes(include=['number'])

    # Calculate summary statistics for numeric columns
    summary_stats = numeric_cols.sum(axis=0)

    # Construct a formatted string for the pal numbers and summary
    summary_text = ""
    for stat_name, stat_value in summary_stats.items():
        summary_text += f"{stat_name}: {stat_value}\n"

    # Add selected pal numbers and names with commas
    pal_numbers = ", ".join(str(x) for x in filtered_df['pal_number'].tolist())
    pal_names = ", ".join(filtered_df['pal_name'].tolist())  # Assuming 'pal_name' is a string column
    summary_text += f"\nSelected Pal Numbers: {pal_numbers}\nSelected Pals: {pal_names}"

    return summary_text.rstrip()  # Remove trailing newline


# Data retrieval and initialization
df = pd.read_csv('pals.csv')

# Window and label
root = tk.Tk()
root.title('Palworld Pal Picker')
root.geometry("500x750")
label = Label(root,
              text="Choose Pals (1-20) Below:",
              font="Helvetica, 18")
label.pack()


# Listbox with scrollbar and initial data
yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, selectmode="multiple",
                  yscrollcommand=yscrollbar.set)
update_listbox(df)  # Populate the listbox using the DataFrame
listbox.pack(padx=10, pady=10, expand=YES, fill="both")

yscrollbar.config(command=listbox.yview)

# Button to display summary statistics and pal numbers
get_summary_button = Button(root, text="Get Selected Pals' Summary Stats",
                             command=lambda: summary_label.config(text=calculate_summary_stats(df, get_selected_pals())))
get_summary_button.pack()

# Label to display the summary statistics (initially blank)
summary_label = Label(root, wraplength=200, text="")
summary_label.pack()

root.mainloop()