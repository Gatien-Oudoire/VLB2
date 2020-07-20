#Ressources
from tkinter import filedialog
import tkinter
import webbrowser
import vlc


# Fenetres et parametres
app = tkinter.Tk()
app.geometry("1366x768")
app.title("Lecteur Vidéo VLB2")

#Fonction Fichier
def ouvrirFichier():

    #Demande à l utilisateur de choisir le fichier
    fichierPath = filedialog.askopenfilename()
    print(fichierPath)
    
    #Verifie qu il n a pas annulé
    if fichierPath != "":

        #Essaye de trouver le format de la video
        separateur = fichierPath.split(".")
        formatVideo = separateur[-1]
        print(formatVideo)

#Fonctions -> Fenetre A propos
def apropos():
    fenetreApropos = tkinter.Toplevel(app)
    fenetreApropos.title("A Propos")
    fenetreApropos.geometry("250x250")
    auteur = tkinter.Label(fenetreApropos, text="Auteur: Gatien Oudoire")
    auteur.pack()
def support():
    webbrowser.open_new(r"https://gatien-oudoire.com")

#Decalaration de barre de menu
mainMenu = tkinter.Menu(app)

#Menu FICHIER
menuFichier = tkinter.Menu(mainMenu, tearoff=0)
menuFichier.add_command(label="Ouvrir un fichier", command=ouvrirFichier)
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=app.quit)

#Menu AIDE
menuAide = tkinter.Menu(mainMenu, tearoff=0)
menuAide.add_command(label="Support", command=support)
menuAide.add_command(label="A propos", command=apropos)

#Ajout des differents menus
mainMenu.add_cascade(label="Fichier",menu=menuFichier)
mainMenu.add_cascade(label="A propos",menu=menuAide)

#Boucle de la fenetre
app.config(menu=mainMenu)
app.mainloop()