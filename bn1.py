from upemtk import *
from random import randint
from time import sleep, time

taille_case = 20
largeur_plateau = 20 
hauteur_plateau = 20

def init(taille):
	plateau=[]
	for i in range(taille):
		plateau.append([0]*taille)
	return plateau

def affiche_plateau(plateau):
	for ligne in plateau:
		print(ligne)

def placer_bateau(x, y, taille, direction, plateau):
	plateau[y][x]=1
	if taille == 1:
		if 0 <= x < largeur_plateau and 0 <= y < hauteur_plateau:
			return True
	else:
		for i in range(taille):
			if direction == 0:
				if y + 1 >= taille: #+1 car la matrice commence à 0
					plateau[y-i][x]=1
				else:
					return False

			elif direction == 1:
				if x + taille <= len(plateau1[0]):
					plateau[y][x+i]=1
				else:
					return False

			elif direction == 2:
				if y + taille <= len(plateau1):
					plateau[y+i][x]=1
				else:
					return False

			elif direction == 3:
				if x + 1 >= taille:
					plateau[y][x-i]=1
				else:
					return False

		return True

def demande(taille):
	# x = int(input("abscisse de la tete du bateau: "))
	x = my_input("abscisse de la tete du bateau: ", "int")
	# y = int(input("ordonnée de la tete du bateau: "))
	y = my_input("ordonnée de la tete du bateau: ", "int")
	# direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	direction = my_input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] ", "int")
	return x, y, taille, direction

def sortie_bateau(taille, plateau, liste_bateau):
	placement = False
	while not placement:
		x, y, taille, direction = demande(taille)
		if placer_bateau(x, y, taille, direction, plateau) == False:
			if direction == 0:
				for i in range(y-taille + 1, y+1):
					plateau[i][x]=0
			elif direction == 1:
				for i in range(x, len(plateau[0])):
					plateau[y][i]=0
			elif direction == 2:
				for i in range(y, len(plateau)):
					plateau[i][x]=0
			elif direction == 3:
				for i in range(x-taille + 1, x+1):
					plateau[y][i]=0

		elif placer_bateau(x, y, taille, direction, plateau) == True: # faut faire en sorte que si il y a deja un bateau 
			#que le truc redemande des coordoonnees
			placement = placer_bateau(x, y, taille, direction, plateau)

			bateau = []
			if direction == 0:
				for i in range(y-taille + 1, y+1):
					bateau.append((x, i))
			elif direction == 1:
				for i in range(x, x + taille):
					bateau.append((i, y))
			elif direction == 2:
				for i in range(y, y + taille):
					bateau.append((x, i))
			elif direction == 3:
				for i in range(x-taille + 1, x+1):
					bateau.append((i, y))
			liste_bateau[taille - 1].append(bateau)

			
def dessine_bateau(plateau, x, y, j, j_bis, placement_x, placement_y, liste_bateau):
	texte(x, y, "Grille de bateaux de " + j, couleur='red', ancrage='nw', police='Helvetica', taille=30)
	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de votre bateau de 6 cases [1]")
	sortie_bateau(6, plateau, liste_bateau)
	efface(texte1)
	dessine_grille(placement_x, placement_y, plateau)

	for i in range(2):
		nb = 2 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 5 cases [" + str(nb) + ']')
		sortie_bateau(5, plateau, liste_bateau)
		efface(texte1)
		dessine_grille(placement_x, placement_y, plateau)	
	efface(texte1)

	# for i in range(3):
	# 	nb = 3 - i
	# 	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 4 cases [" + str(nb) + ']')
	# 	sortie_bateau(4, plateau, liste_bateau)
	# 	efface(texte1)
	# 	dessine_grille(placement_x, placement_y, plateau)
	# efface(texte1)

	# for i in range(4):
	# 	nb = 4 - i
	# 	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 3 cases [" + str(nb) + ']')
	# 	sortie_bateau(3, plateau, liste_bateau)
	# 	efface(texte1)
	# 	dessine_grille(placement_x, placement_y, plateau)		
	# efface(texte1)

	# for i in range(5):
	# 	nb = 5 - i
	# 	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 2 cases [" + str(nb) + ']')
	# 	sortie_bateau(2, plateau, liste_bateau)
	# 	efface(texte1)
	# 	dessine_grille(placement_x, placement_y, plateau)
	# efface(texte1)

	# for i in range(6):
	# 	nb = 6 - i
	# 	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 1 case [" + str(nb) + ']')
	# 	sortie_bateau(1, plateau, liste_bateau)
	# 	efface(texte1)
	# 	dessine_grille(placement_x, placement_y, plateau)
	efface(texte1)

	efface(dessine_grille(placement_x, placement_y, plateau)) #efface pas la grille de j1 ni texte fin ca efface rien en fait 
	texte(750, 500, "C'est au tour de " + j_bis + " de placer ses bateaux !", couleur='red', ancrage='center', police='Helvetica', taille=50)


def tir(x, y, plateau): #faut transformer cette merde pour que ca affiche dans la fenetre 
#touché
	if plateau[y][x] == 1:
		plateau[y][x] = 2
		print("Touché !")
		return True
#en vue 
	elif plateau[y - 1][x] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y - 1][x - 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y - 1][x + 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y + 1][x] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y + 1][x + 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y + 1][x - 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y][x + 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

	elif plateau[y][x - 1] == 1:
		plateau[y][x] = 4
		print("En vue !")

#rien
	else:
		plateau[y][x] = 3
		print("Dommage !")



def carre(x, y, c1, c2):
	rectangle(x*taille_case+taille_case, y*taille_case+taille_case, x*taille_case+2*taille_case, y*taille_case+2*taille_case, c1, c2)



def dessine_grille(x, y, plateau):
	for i in range(len(plateau)):
		for j in range(len(plateau[i])):
			carre(i + x, j + y, "white", "darkblue")
			if plateau[j][i] == 1:
				carre(i + x, j + y, "white", "red")

def hit(x, y, plateau):
	for i in range(len(plateau)):
		for j in range(len(plateau[i])):
			if plateau[j][i] == 2:
				carre(i, j, "white", "cyan")
			if plateau[j][i] == 3:
				point(i*taille_case+38, y*taille_case+38, couleur='black', epaisseur=5)
			if plateau[j][i] == 4:
				point(i*taille_case+38, y*taille_case+38, couleur='red', epaisseur=5)

def touch(plateau):
	toucher = True
	while toucher:
		# x_tir = int(input("abscisse du tir: "))
		x_tir = my_input("abscisse du tir: ", "int")
		# y_tir = int(input("ordonnée du tir: "))
		y_tir = my_input("ordonnée du tir: ", "int")
		toucher = tir(x_tir, y_tir, plateau)
		hit(x_tir, y_tir, plateau)
		affiche_plateau(plateau)


def coordonnées_clic(texte, x, y):
	""" 
	Cette fonction renvoie les coordonnées de la zone de texte
	(les points supérieur gauche et inférieur droit) dans lequel il y a 
	le texte.
	
	"""
	largeur, hauteur = taille_texte(texte)
	return (x - (largeur / 2), y - (hauteur / 2), x + (largeur / 2), y + (hauteur / 2))


def couler(plateau): #faut faire cette putain de fonction jsp comment faire 
	for x in range(len(plateau)):
		for y in range(len(plateau)):
			if plateau[x][y] != 1 and plateau[x][y] != 3 and plateau[x][y] != 4 and plateau[x][y] != 0:
				plateau[x][y] = 5

def bateaux_aleatoire():
	#faut faire ca aussi
	pass
	

def prof_de_merde():
	#faut faire une fonction pour afficher les 4 grilles en meme temps pour que les profs verifient ca marche
	pass


def _input(msg, reponse_defaut):
    """meme fonction que input mais cette fois si s'affiche à l'écran et non sur la console"""
    texte_ = reponse_defaut
    while True:
        ev = donne_ev()
        t_ev = type_ev(ev)
        if t_ev == "Quitte":			#ferme la fenetre et quitte le programme si on fait la croix
        	ferme_fenetre()		
        	exit()
        if t_ev == "Touche":
            x = touche(ev)

            if x == "Return":
                return texte_
            elif x == "BackSpace":
                texte_ = texte_[:-1]

            elif len(x) == 1 and len(texte_) <= 18:
                texte_ += x

        efface("texte_input")
        texte(
            1500 * 2/ 3,
            1000 // 3,
            texte_,
            couleur="white",
            ancrage="center",
            tag="texte_input",
        )
        mise_a_jour()


def my_input(msg, type_retour, reponse_defaut=""):
    """affichage de l'input"""
    rectangle(
        1500 * 2/3 - 280,
        1000 // 3 - 200,
        1500 * 2/3 + 280,
        1000 // 3 + 200,
        couleur="gray28",
        remplissage="gray",
        epaisseur=5,
        tag="cadre",
    )

    while True:
        texte(
            1500 * 2/3,
            1000 // 3 - 150,
            msg,
            couleur="white",
            ancrage="center",
            tag="msg",
        )
        _var = _input(msg, reponse_defaut)
        if type_retour == "int":
            if _var.isdigit():
                if int(_var) < 50:
                    efface("msg")
                    efface("msg_erreur")
                    efface("texte_input")
                    efface("cadre")
                    return int(_var)
        else:
            efface("msg")
            efface("msg_erreur")
            efface("texte_input")
            efface("cadre")
            return _var


if __name__ == "__main__":

	# initialisation du jeu 
	score = 0
	menu = True
	jouer = False
	joueur_1 = False
	joueur_2 = False

	liste_bateau_joueur1 = [[] for i in range(6)]
	liste_bateau_joueur2 = [[] for i in range(6)]
	# liste_bateau = []
	# for i in range(6):
	# 	liste_bateau.append([])



	choix_mode = [("Mode classique ", 640, 200),  
		("Mode aléatoire", 640, 300),
		("Mode prof", 640, 400),
		("Quitter", 640, 500)]


	cree_fenetre(1500, 1000)
	while menu:
		rectangle(0, 0, 1500, 1000, couleur='darkblue', remplissage='darkblue')
		polygone((200, 150, 300, 230, 100, 230), epaisseur=3)
		ligne(200, 150, 200, 240, epaisseur=3)
		polygone((75, 240, 325, 240, 300, 270, 100, 270, 75, 240), epaisseur=3)
		for i in range(len(choix_mode)):
			texte(640, 50, 'Bataille Navale', ancrage = "center", couleur='red', police='Helvetica', taille=50)
			texte(choix_mode[i][1], choix_mode[i][2], choix_mode[i][0], ancrage = "center", couleur='white', police='Helvetica', taille=30)

		(x, y) = attend_clic_gauche()
		for i in range(len(choix_mode)):
			x1, y1 , x2, y2 = coordonnées_clic(*choix_mode[i])
			if x1 < x < x2 and y1 < y < y2:
				mode = choix_mode[i][0]
				if mode != "Quitter":
					jouer = True 
					menu = False
				else:
					menu = False

	debut = time()
	plateau1 = init(20)
	plateau2 = init(20)
	while jouer:
		efface_tout()
		dessine_grille(0, 0, plateau1)
		dessine_bateau(plateau1, 25, 530, 'j1', 'j2', 0, 0, liste_bateau_joueur1)
		
		
		dessine_grille(25, 0, plateau2)
		dessine_bateau(plateau2, 900, 530, 'j2', 'j1', 25, 0, liste_bateau_joueur2)
		print(liste_bateau_joueur1)
		print(liste_bateau_joueur2)


		# affiche_plateau(plateau1)

		dessine_grille(0, 0, plateau1)

		touch(plateau1)

		affiche_plateau(plateau1)
		


		attend_fermeture()

