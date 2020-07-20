#Ressources
from tkinter import filedialog
import tkinter
import webbrowser
import cv2
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


# Fenetres et parametres
lecteurVideo = tkinter.Tk()
lecteurVideo.geometry("1420x820")
lecteurVideo.minsize(700,400)
lecteurVideo.title("Lecteur Vidéo VLB2")

#Fonction Fichier
def ouvrirFichier():

    #Liste des types de fichiers supportés
    typesDeFichier = [
        ('Fichiers Vidéos', '*.mp4 *.avi'),
        ('Fichiers Audio', '*.mp3 *.wav')
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

        #Lance le son
        if formatVideo == "mp3":
            fichierAudio = AudioSegment.from_mp3(fichierPath)
        elif formatVideo == "wav":
            fichierAudio = AudioSegment.from_wav(fichierPath)
        play(fichierAudio)
                    
def camera():
    fluxVideo = cv2.VideoCapture(0)
    while True:

        ret, frame = fluxVideo.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        fluxVideo.read()
        cv2.destroyAllWindows()

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
menuFichier.add_command(label="Utiliser une caméra", command=camera)
menuFichier.add_cascade(label="Fichiers récents")
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=lecteurVideo.quit)

#MENU LECTURE
menuLecture = tkinter.Menu(mainMenu, tearoff=0)
menuLecture.add_command(label="Lire")
menuLecture.add_command(label="Pause")
menuLecture.add_command(label="Plein Ecran")

#MENU SON
menuSon = tkinter.Menu(mainMenu, tearoff=0)
menuSon.add_command(label="Augmenter volume")
menuSon.add_command(label="Diminuer Volume")
menuSon.add_command(label="Couper le son")

#Menu AIDE
menuAide = tkinter.Menu(mainMenu, tearoff=0)
menuAide.add_command(label="Support", command=support)
menuAide.add_command(label="A propos", command=apropos)

#Ajout des differents menus
mainMenu.add_cascade(label="Fichier",menu=menuFichier)
mainMenu.add_cascade(label="Lecture",menu=menuLecture)
mainMenu.add_cascade(label="Son",menu=menuSon)
mainMenu.add_cascade(label="A propos",menu=menuAide)

#Création du cadre ou sera lu la vidéo
cadreVideo = tkinter.Frame(lecteurVideo, bg="black", width=1280, height=720)


#Barre pour controler la vidéo

#Boucle de la fenetre
cadreVideo.pack()
lecteurVideo.config(menu=mainMenu)
lecteurVideo.mainloop()