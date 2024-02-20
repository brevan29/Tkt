texte=""
def occurences(texte):
    nblettres={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0, "z":0} 
    #au-dessus la foçon la plus évidente de définir la liste - nblettres car c'est le nombre de chaque lettre
    for lettre in texte.lower(): #On veut regarder chaque lettre en minuscule (c'est la même chose au fond que ce soit en maj ou en min)
        if lettre!=" ":#On ne veut pas les espaces
            nblettres[lettre]+=1 #On modifie la valeur de la clé (qui est notre lettre) et on lui ajoute 1 comme si c'était une variable classique
    return nblettres

def distincts(texte):
    dictionnaire=occurences(texte) #On veut le nombre de letres où c'est pas 0
    nbdistincts=0 #Au départ on a logiquement aucune lettre car on en a pas eu une seule
    for valeurs in dictionnaire.values(): #On regarde chaque valeur prise par le clés du dictionnaire
        if valeurs!=0: # Si il y a eu une occurence de la lettre dans la phrase, on le compte
            nbdistincts+=1 # Sinon non.

"""Façons plus rapides de définir la liste des lettres dans la fonction:"""
#Version 1:
nblettres={}
for lettre in "abcdefghijklmnopqrstuvwxyz": #Ici on regarde toutes les lettres et
    nblettres[lettre]=0 #On les initialise une par une

#Version 2:
nblettres={}
for lettre in texte.lower(): #Elle est plus technique celle-là 
        if lettre!=" ":
            try: #Try et except te permettent de contourner une erreur si tu la fait en sachant d'ou vient le problème
                nblettres[lettre]+=1 #Si ton caractère est défini tu lui ajoutes 1
            except KeyError: #Si la lettre n'est pas définie, le code te renvoie une erreur et except nous permet de la contourner (d'en faire un cas particulier)
                nblettres[lettre]=1 # On initialise la lettre ici, Cette méthode a l'avantage de prendre en compte les accents que j'ai pas intégré avant

# La version 2 est utile car la fonction occurence se résumerait à len(nblettres)
                







