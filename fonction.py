import time
from tkinter import * 

import pygame

from constantes import * 

def jouer():
    global menu
    global menu1
    global nbjeu

    def deplacement():
        global dx, dy, PosX2, PosY2, score, scorebis
        if scorebis==1 and canvas.coords(balle)[3]<=400:
            score+=scorebis 
            scorebis=0
        if canvas.coords(balle)[1]<0:
            dy=-1*dy
        if canvas.coords(balle)[2]>500:
            dx=-1*dx
        if canvas.coords(balle)[0]<0:
            dx=-1*dx
        if canvas.coords(balle)[3]>=PosY2 and canvas.coords(balle)[2]>=canvas.coords(raquette)[0] and canvas.coords(balle)[0]<=canvas.coords(raquette)[2] and canvas.coords(balle)[3]<=490:
            dy=-1*dy          
            scorebis=1
            TextGame.set("Score : "+ str(score))
            
        if canvas.coords(balle)[3] > 525 : 
            tk.destroy() #détruire le jeu lorsque la balle tombe


        if canvas.coords(balle)[3]<550:
            tk.after(10,deplacement)
        
        canvas.move(balle,dx,dy)
 
    def KeyBoard(event):
        global PosX2, menu
        Key = event.keysym
 
        if Key == 'Right':
            canvas.move(raquette,50,0)
        if Key == 'Left':
            canvas.move(raquette,-50,0)

    
    tk = Tk()
    tk.title("[Pong Game]")
    
    canvas = Canvas(tk,width = 500, height = 500 , bd=0, bg="green")
    canvas.pack(padx=10,pady=10)
    
        
    balle = canvas.create_oval(PosX,PosY,PosX+20,PosY+20,fill='white')
    raquette = canvas.create_rectangle(PosX2,PosY2,PosX2+100,PosY2+10,fill='white')
 
    TextGame = StringVar()
    LabelGame = Label(tk, textvariable = TextGame , bg ="white")
    TextGame.set("Score : "+ str(score))
    LabelGame.pack(padx = 15, pady = 5)
 
    canvas.focus_set()
 
    canvas.bind('<Key>',KeyBoard)
 
    deplacement()
    
    tk.mainloop()

