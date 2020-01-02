# -*- coding: cp1252 -*-

from Tkinter import *
from math import *
import time
import random
import pymedia
import tkMessageBox
import pygame

titre_fenetre = "Deamos"
image_icone = "resources/images/images.jpg" 
image_accueil = "resources/images/Collision.jpg"

def jeu():
    pygame.quit()
    global angledeg
    global anglepas
    global centresatellite
    global centreplanete
    global rayonplanete
    
    ############################

    # fonction qui permet le d�placement du satellite 
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
        
    ###########################


    #fonction pour quitter le jeu

    def callback():
        if tkMessageBox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
            player.stop()
            jeu.destroy()

    ############################
            
    #fonction qui lance un compte � rebours
            
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

    ############################

    def musique():
        global player
        player=pymedia.Player()   
        player.start()     # jouer la musique
        player.startPlayback('musique.mp3')


    jeu = Tk()

    jeu.maxsize(600,600)
    jeu.minsize(600,600)

    canvas = Canvas(jeu, width=600, height=600, bg="white")
    canvas.pack()


        # angle entre le point (centre de la plan�te, x(centre plan�te)+rayon de la planete) et le vecteur (centre de la plan�te, centre satellite)

    angledeg = 90
    anglerad = ( angledeg * pi  ) / 180
    anglepas = 5

        
        # coordonn�es initiales
    centreplanete = (300, 300)
    rayonplanete = 100

        # ajout du bond sur les touches du clavier
    canvas.focus_set()
    canvas.bind("<Key>", clavier)


        # cr�ation du satellite
    rayonsatellite = 10
    centresatellite=[centreplanete[0]+rayonplanete*cos(angledeg) ,centreplanete[1]+rayonplanete*sin(angledeg) ]
    satellite = canvas.create_oval(centresatellite[0]-rayonsatellite,centresatellite[1]-rayonsatellite,centresatellite[0]+rayonsatellite,centresatellite[1]+rayonsatellite,fill="white")


    bouton1 = Button(jeu, text="Quitter",command=callback).place(x='500',y='10') ##bouton qui fermer la fermuture du jeu 


     # Diff�rentes images 

    commandes = PhotoImage(file="commandes.gif")

    controles = PhotoImage(file="controles.gif")

    fond = PhotoImage(file="fond.gif")

    gameover= PhotoImage(file="gameover.gif")

    satellite = PhotoImage(file="satellite.gif")

                #  qui composent l'animation de la plan�te Deamos
     
    planeteanimation = ["frame01.gif","frame01.gif",
                 "frame02.gif","frame02.gif",
                 "frame03.gif","frame03.gif",
                 "frame04.gif","frame04.gif",
                 "frame05.gif","frame05.gif",
                 "frame06.gif","frame06.gif",
                 "frame07.gif","frame07.gif",
                 "frame08.gif","frame08.gif",
                 "frame09.gif","frame09.gif",
                 "frame10.gif","frame10.gif",
                 "frame11.gif","frame11.gif",
                 "frame12.gif","frame12.gif",
                 "frame13.gif","frame13.gif",
                 "frame14.gif","frame14.gif",
                 "frame15.gif","frame15.gif",
                 "frame16.gif","frame16.gif",
                 "frame17.gif","frame17.gif",
                 "frame18.gif","frame18.gif",
                 "frame19.gif","frame19.gif",
                 "frame20.gif","frame20.gif",
                 "frame21.gif","frame21.gif",
                 "frame22.gif","frame22.gif",
                 "frame23.gif","frame23.gif",
                 "frame24.gif","frame24.gif",
                 "frame25.gif","frame25.gif",
                 "frame26.gif","frame26.gif",
                 "frame27.gif","frame27.gif",
                 "frame28.gif","frame28.gif",
                 "frame29.gif","frame29.gif",
                 "frame30.gif","frame30.gif",
                 "frame31.gif","frame31.gif"]

        # cr�e une liste d'images pour l'animation de la m�t�orite
    giflist = []
    for imagefile in planeteanimation:
        image = PhotoImage(file=imagefile)
        giflist.append(image)

    threetwoone = ["3.gif","2.gif","1.gif"]    # Diff�rentes images qui composent l'animation du compte � rebours

        # cr�e une liste d'images pour le compte � rebours 
    Acomptage = []
    for imagefile in threetwoone:
        image = PhotoImage(file=imagefile)
        Acomptage.append(image)   


    asteroideanimation = ["asteroids1.gif","asteroids2.gif","asteroids3.gif",
                          "asteroids4.gif","asteroids5.gif","asteroids7.gif",
                          "asteroids8.gif","asteroids9.gif"] # Diff�rentes images qui composent l'animation de la m�t�orite


        # cr�e une liste d'images pour l'animation de la m�t�orite
    rotation = []
    for imagefile in asteroideanimation:
        image = PhotoImage(file=imagefile)
        rotation.append(image)



        #trajectoire

    point0 = 300,300

    meteotraj=rayonplanete * 3.6  # rayon du cercle ou la m�t�orite se situe au d�part 

    rayonmeteo= 5 ###rayon de la m�t�orite

    mort = 0
    coins=[[0,0],[600,600],[0,600],[600,0]]

    xmeteo=0
    ymeteo=0
    hasard = random.randint(0,3)
    centremeteorite=[coins[hasard][0],coins[hasard][1]]


    vitesse = 0.005

    x = 0  #nombres d'images pour la m�t�orite 

    #### JEU CONCRET 

    chargement() 

    debut = 1
    f=0
    mouv = random.randint(0,360)
    musique()
    score = 0 
    while debut==1 : #lance la musique
        for gif in giflist:
            if x > 7:
                x = 0    ## faire tourner la m�t�orite � nouveau
            canvas.delete(ALL)
            imagedefond = canvas.create_image(300,300,image=fond)
            animationdelaplanete = canvas.create_image(300.5, 300.5, image=gif)
            contourdelaplanete = canvas.create_oval(centreplanete[0]-rayonplanete,centreplanete[1]-rayonplanete,centreplanete[0]+rayonplanete,centreplanete[1]+rayonplanete,width=3.5,outline="black")
            satel = canvas.create_image(centresatellite[0],centresatellite[1],image= satellite )
            centremeteo = [centreplanete[0]+meteotraj*cos(mouv) ,centreplanete[1]+meteotraj*sin(mouv)]
            meteorite = canvas.create_image(centremeteo[0],centremeteo[1],image=rotation[x])
            x=x+1

            meteotraj=meteotraj*0.993 
            mouv = mouv - vitesse
     
            if (centremeteo[0] > (centresatellite[0]-rayonsatellite) ) and ( centremeteo[0] < (centresatellite[0]+rayonsatellite) ) and (centremeteo[1] > (centresatellite[1]-rayonsatellite)) and (centremeteo[1] < (centresatellite[1]+rayonsatellite)) :
                #faire disparaitre meteo, une nouvelle avec nouveau mouv et rayon d'origine
                mouv = random.randint(0,360)
                meteotraj=rayonplanete * 3.6
                score = score + 1
                
            if (meteotraj < rayonplanete) :
                f=f+1
                canvas.delete(ALL)
                canvas.create_image(300,300,image=gameover)
                canvas.update()
                time.sleep(4)
                player.stop()
                jeu.destroy()

            if f==0:
                canvas.update()
            time.sleep(0.02) 


    #### FIN JEU
            
    jeu.mainloop() 
