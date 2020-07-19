#Ressources
import tkinter

# Fenetre et parametres
app = tkinter.Tk()
app.geometry("1366x768")
app.title("Lecteur Vidéo VLB2")

#Decalaration de barre de menu
mainMenu = tkinter.Menu(app)

#Menu FICHIER
menuFichier = tkinter.Menu(mainMenu)
menuFichier.add_command(label="Ouvrir un fichier")
menuFichier.add_command(label="Quitter", command=app.quit)

#Menu AIDE
menuAide = tkinter.Menu(mainMenu)
menuAide.add_command(label="A propos")

#Ajout des differents menus
mainMenu.add_cascade(label="Fichier",menu=menuFichier)
mainMenu.add_cascade(label="Fichier",menu=menuAide)

#Boucle de la fenetre
app.config(menu=mainMenu)
app.mainloop()


