#Ressources
from tkinter import filedialog
import tkinter
import webbrowser
import cv2


# Fenetres et parametres
lecteurVideo = tkinter.Tk()
lecteurVideo.geometry("1420x820")
lecteurVideo.title("Lecteur Vidéo VLB2")

#Fonction Fichier
def ouvrirFichier():

    #Liste des types de fichiers supportés
    typesDeFichier = [
        ('Fichiers Vidéos', '*.mp4 *.avi'),
        ('Fichiers Audio', '*.mp3')
    ]
    #Demande à l utilisateur de choisir le fichier
    fichierPath = filedialog.askopenfilename(filetypes=typesDeFichier)
    print(fichierPath)
    
    #Verifie qu il n a pas annulé
    if fichierPath != "":

        #Essaye de trouver le format de la video
        separateur = fichierPath.split(".")
        formatVideo = separateur[-1]
        print(formatVideo)
        

#Fonctions -> Fenetre A propos
def apropos():
    fenetreApropos = tkinter.Toplevel(lecteurVideo)
    fenetreApropos.title("A Propos")
    fenetreApropos.geometry("250x250")
    auteur = tkinter.Label(fenetreApropos, text="Auteur: Gatien Oudoire")
    auteur.pack()
def support():
    webbrowser.open_new(r"https://gatien-oudoire.com")

#Decalaration de barre de menu
mainMenu = tkinter.Menu(lecteurVideo)

#Menu FICHIER
menuFichier = tkinter.Menu(mainMenu, tearoff=0)
menuFichier.add_command(label="Ouvrir un fichier", command=ouvrirFichier)
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=lecteurVideo.quit)

#Menu AIDE
menuAide = tkinter.Menu(mainMenu, tearoff=0)
menuAide.add_command(label="Support", command=support)
menuAide.add_command(label="A propos", command=apropos)

#Ajout des differents menus
mainMenu.add_cascade(label="Fichier",menu=menuFichier)
mainMenu.add_cascade(label="A propos",menu=menuAide)

cadre = tkinter.Frame(lecteurVideo, bg="black", width=1280, height=720)

barreControle = tkinter.Frame(lecteurVideo, bg="grey")

#Boucle de la fenetre
cadre.pack()
barreControle.propagate(False)
barreControle.pack()
lecteurVideo.config(menu=mainMenu)
lecteurVideo.mainloop()