from tkinter import *
from tkinter import ttk

def calculate_percentage():
    try:
        totalCapacity = float(entry1.get())
        totalUsed = float(entry2.get())
        
        percentageUsed = (totalUsed / totalCapacity) * 100
        
        labelResult.config(text=f"Le disk est utilisé à {percentageUsed:.2f}%")
    except ValueError:
        labelResult.config(text="Veuillez entrer des valeurs valides.")

root = Tk()

labelTitle1 = ttk.Label(root, text='Total Capacity (GB)')
entry1 = ttk.Entry(root)
labelTitle2 = ttk.Label(root, text='Total Used (GB)')
entry2 = ttk.Entry(root)
submitButton = ttk.Button(root, text="Calculer", command=calculate_percentage)
exitButton = ttk.Button(root, text='Exit', command=root.destroy)
labelResult = ttk.Label(root, text='')

labelTitle1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
labelTitle2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
submitButton.grid(row=2, column=1)
exitButton.grid(row=3, column=1)
labelResult.grid(row=4, column=0, columnspan=2)

root.mainloop()
