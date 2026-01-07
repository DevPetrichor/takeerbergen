from tkinter import *
import tkinter as tk

master = Tk()
master.title("Druk Berekenen")
master.iconbitmap("flavicon_druk.ico")
master.minsize(520, 250)  
master.maxsize(521, 251)

Label(master, text="Van wat wil je de druk berekenen: ").grid(row=0)
voorwerp = Entry(master)
voorwerp.grid(row=0,column=1)
Label(master, text="Lengte van voorwerp (m): ").grid(row=3)
Label(master, text="Breedte van voorwerp (m): ").grid(row=4)
Label(master, text="Hoogte van voorwerp (m): ").grid(row=5)
Label(master, text="Gewicht van voorwerp (kg): ").grid(row=6)
Label(master, text="Hoeveel druk wil je (bar): ").grid(row=7)
Label(master, text="Oppervlakte van de ondergrond waar de bananen op liggen (m²): ").grid(row=8)
lengte = Entry(master)
breedte = Entry(master)
hoogte = Entry(master)
gewicht = Entry(master)
bar = Entry(master)
ondergrond = Entry(master)
lengte.grid(row=3,column=1)
breedte.grid(row=4,column=1)
hoogte.grid(row=5,column=1)
gewicht.grid(row=6,column=1)
bar.grid(row=7,column=1)
ondergrond.grid(row=8,column=1)

def calculate():
    pa = float(bar.get()) * 10**5
    F = float(gewicht.get()) * 9.81
    A = float(breedte.get()) * float(hoogte.get()) * float(lengte.get())
    druk_banaan = F / A
    n = round((pa * float(ondergrond.get())) / F)
    oppervlakte = float(ondergrond.get()) / A

    Uitkomst_1 = f"Je zult {n} {voorwerp.get()}(en) nodig hebben voor een druk van {bar.get()} bar."
    Uitkomst_2 = f"Je kunt {int(oppervlakte)} {voorwerp.get()} op de opgegeven ondergrond plaatsen."

    uitkomst1.config(text=Uitkomst_1)
    uitkomst2.config(text=Uitkomst_2)

Button(master, text="Bereken", command=calculate).grid(row=9, column=0)
uitkomst1 = Label(master, text="")
uitkomst1.grid(row=10, column=0)
uitkomst2 = Label(master, text="")
uitkomst2.grid(row=11, column=0)

mainloop()