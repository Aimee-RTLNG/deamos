### importation des librairies 
from Tkinter import *
from math import *
import time
import pymedia
import tkMessageBox
import random


# fonction qui permet le d�placement du satellite gr�ce aux touches du clavier
def clavier(event):               
    global centresatellite
    global angledeg

    touche = event.keysym
    

    if touche == "Right":
            angledeg = angledeg + anglepas 
            centresatellite=[centreplanete[0]+rayonplanete*cos(angledeg*pi/180) ,centreplanete[1]+rayonplanete*sin(angledeg*pi/180) ]
    elif touche == "Left":
            angledeg = angledeg - anglepas 
            centresatellite=[centreplanete[0]+rayonplanete*cos(angledeg*pi/180) ,centreplanete[1]+rayonplanete*sin(angledeg*pi/180) ]
        # changement de coordonn�es pour le rond
        
    canvas.coords(satellite, centresatellite[0]-5, centresatellite[1]-5, centresatellite[0]+5, centresatellite[1]+5)
    

#fonction pour quitter le jeu gr�ce � un bouton Quitter
def callback():
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        player.stop()
        jeu.destroy()


#fonction qui lance un compte � rebours pour lancer le jeu et permette au joueur de comprendre les commandes 
def chargement():

    debut=0
    while debut==0:
        for x in range (0,3) :
            canvas.delete(ALL)
            canvas.create_image(300,300,image=fond)
            canvas.create_image(300.5, 300.5, image=giflist[0])
            canvas.create_image(300,100,image=Acomptage[x])
            canvas.create_oval(centreplanete[0]-rayonplanete,centreplanete[1]-rayonplanete,centreplanete[0]+rayonplanete,centreplanete[1]+rayonplanete,width=3.5,outline="black")
            canvas.create_oval(centresatellite[0]-rayonsatellite,centresatellite[1]-rayonsatellite,centresatellite[0]+rayonsatellite,centresatellite[1]+rayonsatellite,fill="white")
            canvas.create_image(300,200,image=controles)
            canvas.create_image(300,400,image=commandes)
            canvas.update()
            time.sleep(1.5)
        debut=debut+1


# fonction qui permet de lancer la musique du jeu
def musique():
    global player
    player=pymedia.Player()   
    player.start()     # jouer la musique
    player.startPlayback('resources/music/musique.mp3')


#cr�ation de la fen�tre de jeu et d�finie des param�tre (taille non modifiable) 
jeu = Tk()
jeu.maxsize(600,600)
jeu.minsize(600,600)
canvas = Canvas(jeu, width=600, height=600)
canvas.pack()


# angle entre le point (centre de la plan�te, x(centre plan�te)+rayon de la planete) et le vecteur (centre de la plan�te, centre satellite)
angledeg = 90
anglerad = ( angledeg * pi  ) / 180
anglepas = 5


# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)

# coordonn�es de la plan�te
centreplanete = (300, 300)
rayonplanete = 100

# coordonn�es et cr�ation du satellite
rayonsatellite = 10
centresatellite=[centreplanete[0]+rayonplanete*cos(angledeg) ,centreplanete[1]+rayonplanete*sin(angledeg) ]
satellite = canvas.create_oval(centresatellite[0]-rayonsatellite,centresatellite[1]-rayonsatellite,centresatellite[0]+rayonsatellite,centresatellite[1]+rayonsatellite,fill="white")

#cr�ation du bouton qui permet de quitter le jeu 
bouton1 = Button(jeu, text="Quitter",command=callback).place(x='500',y='10') ##bouton qui fermer la fermuture du jeu 


 # Diff�rentes images qui composent la fen�tre 

commandes = PhotoImage(file="resources/images/commandes.gif") ## image de l'explication des commandes 

controles = PhotoImage(file="resources/images/controles.gif") ## image du texte " Contr�les "
 
fond = PhotoImage(file="resources/images/fond.gif") ##image de fond

gameover= PhotoImage(file="resources/images/gameover.gif") ## image de Game Over

satellite = PhotoImage(file="resources/images/satellite.gif") ## image du satellite

            
# images qui composent l'animation de la plan�te 
planeteanimation = ["resources/images/frames/frame01.gif","resources/images/frames/frame01.gif",
             "resources/images/frames/frame02.gif","resources/images/frames/frame02.gif",
             "resources/images/frames/frame03.gif","resources/images/frames/frame03.gif",
             "resources/images/frames/frame04.gif","resources/images/frames/frame04.gif",
             "resources/images/frames/frame05.gif","resources/images/frames/frame05.gif",
             "resources/images/frames/frame06.gif","resources/images/frames/frame06.gif",
             "resources/images/frames/frame07.gif","resources/images/frames/frame07.gif",
             "resources/images/frames/frame08.gif","resources/images/frames/frame08.gif",
             "resources/images/frames/frame09.gif","resources/images/frames/frame09.gif",
             "resources/images/frames/frame10.gif","resources/images/frames/frame10.gif",
             "resources/images/frames/frame11.gif","resources/images/frames/frame11.gif",
             "resources/images/frames/frame12.gif","resources/images/frames/frame12.gif",
             "resources/images/frames/frame13.gif","resources/images/frames/frame13.gif",
             "resources/images/frames/frame14.gif","resources/images/frames/frame14.gif",
             "resources/images/frames/frame15.gif","resources/images/frames/frame15.gif",
             "resources/images/frames/frame16.gif","resources/images/frames/frame16.gif",
             "resources/images/frames/frame17.gif","resources/images/frames/frame17.gif",
             "resources/images/frames/frame18.gif","resources/images/frames/frame18.gif",
             "resources/images/frames/frame19.gif","resources/images/frames/frame19.gif",
             "resources/images/frames/frame20.gif","resources/images/frames/frame20.gif",
             "resources/images/frames/frame21.gif","resources/images/frames/frame21.gif",
             "resources/images/frames/frame22.gif","resources/images/frames/frame22.gif",
             "resources/images/frames/frame23.gif","resources/images/frames/frame23.gif",
             "resources/images/frames/frame24.gif","resources/images/frames/frame24.gif",
             "resources/images/frames/frame25.gif","resources/images/frames/frame25.gif",
             "resources/images/frames/frame26.gif","resources/images/frames/frame26.gif",
             "resources/images/frames/frame27.gif","resources/images/frames/frame27.gif",
             "resources/images/frames/frame28.gif","resources/images/frames/frame28.gif",
             "resources/images/frames/frame29.gif","resources/images/frames/frame29.gif",
             "resources/images/frames/frame30.gif","resources/images/frames/frame30.gif",
             "resources/images/frames/frame31.gif","resources/images/frames/frame31.gif"]

giflist = [] # cr�ation d'une liste d'images pour l'animation de la plan�te 
for imagefile in planeteanimation:
    image = PhotoImage(file=imagefile)
    giflist.append(image)

threetwoone = ["resources/images/countdown/3.gif","resources/images/countdown/2.gif","resources/images/countdown/1.gif"]    # Diff�rentes images qui composent l'animation du compte � rebours


Acomptage = [] # cr�ation d'une liste d'images pour l'animation de le compte � rebours 
for imagefile in threetwoone:
    image = PhotoImage(file=imagefile)
    Acomptage.append(image)   


asteroideanimation = ["resources/images/asteroids/asteroids1.gif","resources/images/asteroids/asteroids2.gif","resources/images/asteroids/asteroids3.gif",
                      "resources/images/asteroids/asteroids4.gif","resources/images/asteroids/asteroids5.gif","resources/images/asteroids/asteroids7.gif",
                      "resources/images/asteroids/asteroids8.gif","resources/images/asteroids/asteroids9.gif"] # Diff�rentes images qui composent l'animation de la m�t�orite


rotation = [] # cr�ation d'une liste d'images pour l'animation de la m�t�orite 
for imagefile in asteroideanimation:
    image = PhotoImage(file=imagefile)
    rotation.append(image)


# d�finition des coordon�es de la trajectoire et des param�tres de la m�t�orite 
point0 = 300,300
meteotraj=rayonplanete * 3.6  # rayon du cercle ou la m�t�orite se situe au d�part 
rayonmeteo= 5 ### rayon de la m�t�orite
vitesse = 0.05


#### JEU 

chargement() # lance un compte � rebours et d�finit debut � 0 

x=0  # param�tre qui permet de lancer l'animation de la m�t�orite au d�but
debut = 1 #param�tre qui permet de lancer le jeu 
f=0 # param�tre qui permet de d�finir le nombre de mort [min : 0, max : 1]
mouv = random.randint(0,360) # permet de d�finir un endroit de d�part pour la trajectoire de la m�t�orite
musique() #lance la fonction musique
score = 0 
while debut==1 : 
    for gif in giflist :  #permet de donner une impression de mouvement � la plan�te gr�ce aux diff�rentes images qui composent l'animation
        if x > 7:    
            x = 0    ## faire tourner la m�t�orite � nouveau
        canvas.delete(ALL) ## actualise la fen�tre 
        imagedefond = canvas.create_image(300,300,image=fond)  #d�finie l'image de fond
        animationdelaplanete = canvas.create_image(300.5, 300.5, image=gif)  #d�finie l'image de la plan�te
        contourdelaplanete = canvas.create_oval(centreplanete[0]-rayonplanete,centreplanete[1]-rayonplanete,centreplanete[0]+rayonplanete,centreplanete[1]+rayonplanete,width=3.5,outline="black") #d�fini le contour de la plan�te 
        satel = canvas.create_image(centresatellite[0],centresatellite[1],image= satellite ) # d�fini le satellite 
        centremeteo = [centreplanete[0]+meteotraj*cos(mouv) ,centreplanete[1]+meteotraj*sin(mouv)] #d�fini le centre de la m�t�orite 
        meteorite = canvas.create_image(centremeteo[0],centremeteo[1],image=rotation[x]) #d�fini la m�t�orite 
        x=x+1   # actualise l'image de la m�t�orite  
        meteotraj=meteotraj*0.993  #permet de r�duire le rayon de la trajectoire circulaire de la m�t�orite, et de donc la faire se rapprocher du centre progressivement
        mouv = mouv - vitesse  #permet d'ajuster la vitesse de la m�t�orite 
 
        if (centremeteo[0] > (centresatellite[0]-rayonsatellite) ) and ( centremeteo[0] < (centresatellite[0]+rayonsatellite) ) and (centremeteo[1] > (centresatellite[1]-rayonsatellite)) and (centremeteo[1] < (centresatellite[1]+rayonsatellite)) :
            #faire disparaitre meteo, apparaitre une nouvelle avec nouvel endroit de d�part et rayon d'origine
            mouv = random.randint(0,360)  
            meteotraj=rayonplanete * 3.6  
            score = score + 1  # incr�mente le score de 1 
            
        if (meteotraj < rayonplanete) :
            f=f+1 #augmente le compteur de morts
            canvas.delete(ALL)  # r�initialise la fen�tre
            canvas.create_image(300,300,image=gameover)  #affiche l'image Game Over 
            canvas.update()  # actualise la fen�tre 
            time.sleep(3) 
            player.stop()  # coupe la musique 
            jeu.destroy()  # ferme la fen�tre de jeu 

        if f==0:  #tant que le joueur n'est pas mort
            canvas.update()  #le jeu continue 
        time.sleep(0.02) # d�lai entre l'animation de la plan�te (actualisation de la fen�tre )


#### FIN JEU
        
jeu.mainloop() 
