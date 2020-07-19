from tkinter import *

fenetrePrincipal = Tk()

listeFichier = Listbox(fenetrePrincipal)

listeFichier.insert(END, "Fichier")
listeFichier.insert(END, "Ouvrir un fichier")

listeFichier.pack()

fenetrePrincipal.mainloop()