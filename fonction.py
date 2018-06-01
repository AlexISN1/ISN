import time

def displayIntro():
	    print("Vous venez de récuperer une banane")
	    print("Vous préférez ne pas la manger, elle pourra probablement vous être utile ")
	    print("Vous avancez dans la jungle")
	    print("Et la un groupe de singe vous bloque")
	    print()

def choosePath():
	    path = ""
	    while path != "droite" and path != "gauche": 
	        path = input("Quel chemin allez vous choisir (Droite ou Gauche): ")
	    return path

def checkPath(chosenPath):
	    print("Vous avancez dans une jungle sauvage")
	    time.sleep(0.5)
	    print("Vous croisez des amis singes a qui vous passez la banane que vous venez de trouver ")
	    time.sleep(0.5)
	    print("Mais ils restent néanmoins suspect à votre égard...")
	    print()
	    time.sleep(0.5)
	    if chosenPath == 'droite':
	        print("C'est normal ! Ils veulent vous aider à avancer !")
	        print("Ils vous laissent pénétrer dans la deuxième partie de la jungle")
	        print ("Vous arrivez devant une riviere") 
	        print ("Deux chemins s'offrent à vous")
	    else:
	        print("Ils sont méfiants dû à la personne derriere vous")
	        print("C'est Alexandre !")
	        print("Attention à vos omoplates !!!")
	        
def chooseriviere():
	    riviere = ""
	    while riviere != "bouee" and riviere != "bois": 
	        riviere = input("Allez vous prendre la bouée ou le bout de bois ? (bouée ou bois): ")
	        return riviere

def checkriviere(riviere) :
	        if riviere == 'bouee':
	            print("Vous passez sans soucis")
	            print("")
	            print ("") 
	            print ("")
	        else:
	            print("Vous coulez")
	            print("")
	            print("")

def choosearme():
	    arme = ""
	    while arme != "epee" and arme != "couteau" and arme != "banane" : 
	        arme = input("Allez vous prendre l'épée, le couteau ou la banane ? (epee,couteau ou banane): ")
	        return arme

def checkarme(arme) :
	        if arme == 'banane':
	            print(" Bien joué c'est exactement ce qu il fallait !")
	            print("")
	            print ("") 
	            print ("")
	        else:
	            print("beaucoup trop tranchant !!")
	            print("")

def chooseboss():
	    boss = ""
	    while boss != "haut" and boss != "bas" : 
	        boss = input(" Un singe blanc et tres costaud apparait ! Attaquez les ! Allez vous porter un coup vers le bas ou le haut ? (haut ou bas): ")
	        return boss

def checkboss(boss) :
	        if boss == 'bas':
	            print(" Vous visez une partie assez sensible de l'anatomie de ce singe...")
	            print("mais les dégâts sont présents !")
	            print ("") 
	            print ("")
	        else:
	            print("Il vous contre très facilement")
	            print("vous tombez")

def choosefin():
	    fin = ""
	    while fin != "coeur" and fin != "tete" : 
	        fin = input("Portez lui le coup final ! Achevez le ! (coeur ou tete): ")
	        return fin

def checkfin(fin) :
	        if fin == 'tete':
	            print(" Vous lui lancez la banane dessus !")
	            print("il tombe dans les vappes")
	            print ("Bravo ! vous avez passé cette terrifante jungle...") 
	            print ("")
	        else:
	            print("Le coeur de ce singe est dur comme l'acier !")
	            print("")

