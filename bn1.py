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
	bateau = []
	if direction == 0:
		for i in range(y-taille + 1, y+1):
			plateau[i][x] = 1
			bateau.append((x, i))
	elif direction == 1:
		for i in range(x, x + taille):
			plateau[y][i] = 1
			bateau.append((i, y))
	elif direction == 2:
		for i in range(y, y + taille):
			plateau[i][x] = 1
			bateau.append((x, i))
	elif direction == 3:
		for i in range(x-taille + 1, x+1):
			plateau[y][i] = 1
			bateau.append((i, y))
	return bateau


def demande(taille):
	# x = int(input("abscisse de la tete du bateau: "))
	x = my_input("abscisse de la tete du bateau: ", "int")
	# y = int(input("ordonnée de la tete du bateau: "))
	y = my_input("ordonnée de la tete du bateau: ", "int")
	# direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	direction = my_input("      orientation du bateau \nvers Nord, Est, Sud, Ouest: \n            [0, 1, 2, 3] ", "int")
	return x, y, taille, direction


def sortie_bateau(taille, plateau, liste_bateau):
	placement = False
	while not placement:
		x, y, taille, direction = demande(taille)
		if control_placement(x, y, taille, direction, plateau):
			bateau = placer_bateau(x, y, taille, direction, plateau)
			placement = True
			for elem in bateau:
				liste_bateau[taille - 1].append(elem)


def control_placement(x, y, taille, direction, plateau):
	if direction == 0:
		if y + 1 >= taille:
			for i in range(y-taille + 1, y+1):
				if plateau[i][x] != 0:
					return False
			return True 
		return False
	if direction == 1:
		if x + taille <= len(plateau[0]):
			for i in range(x, x + taille):
				if plateau[y][i] != 0:
					return False
			return True
		return False
	if direction == 2:
		if y + taille <= len(plateau):
			for i in range(y, y + taille):
				if plateau[i][x] != 0:
					return False
			return True 
		return False
	if direction == 3:
		if x + 1 >= taille:
			for i in range(x-taille + 1, x+1):
				if plateau[y][i] != 0:
					return False
			return True 
		return False

			
def dessine_bateau(plateau, x, y, j, placement_x, placement_y, liste_bateau, navires):
	texte(x, y, "Grille de bateaux de " + j, couleur='red', ancrage='nw', police='Helvetica', taille=30)
	for elem in navires:
		for i, taille in enumerate(elem):
			nb = len(elem) - i
			texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de votre bateau de {} cases [{}]".format(taille, nb))
			sortie_bateau(taille, plateau, liste_bateau)
			efface(texte1)
			dessine_grille(placement_x, placement_y, plateau)
		efface(texte1)

	
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
	return False


def carre(x, y, c1, c2):
	rectangle(x*taille_case+taille_case, y*taille_case+taille_case, x*taille_case+2*taille_case, y*taille_case+2*taille_case, c1, c2)


def dessine_grille(x, y, plateau, tir=False):
	dessine_lettre(x, y)
	for i in range(len(plateau)):
		for j in range(len(plateau[i])):
			carre(i + x, j + y, "white", "darkblue")
			if plateau[j][i] == 1 and not tir:
				carre(i + x, j + y, "white", "red")
			elif plateau[j][i] == 2:
				carre(i + x, j + y, "white", "cyan")
			elif plateau[j][i] == 3:
				point((i + x) *taille_case + taille_case + taille_case // 2, (j + y)*taille_case +taille_case + taille_case // 2, couleur='black', epaisseur=5)
			elif plateau[j][i] == 4:
				point((i + x)*taille_case + taille_case + taille_case // 2, (j + y)*taille_case +taille_case + taille_case // 2, couleur='red', epaisseur=5)
			elif plateau[j][i] == 5:
				carre(i + x, j + y, "white", "#ff0080")


def dessine_lettre(x, y):
	for i in range(largeur_plateau):
		largeur, hauteur = taille_texte(texte)
		texte((x + 1) * taille_case + i * taille_case + taille_case // 2, y * taille_case + taille_case // 2, i, ancrage="center", police="Impact", taille=12)
		texte(x * taille_case + taille_case // 2, (y + 1) * taille_case + i * taille_case + taille_case // 2, i, ancrage="center", police="Impact", taille=12)


def touch(plateau, liste_bateau):
	while True:
		# x_tir = int(input("abscisse du tir: "))
		x_tir = my_input("abscisse du tir: ", "int")
		# y_tir = int(input("ordonnée du tir: "))
		y_tir = my_input("ordonnée du tir: ", "int")
		if plateau[y_tir][x_tir] in {0, 1}:
			break

	toucher = tir(x_tir, y_tir, plateau)
	couler(plateau, liste_bateau)
	# affiche_plateau(plateau)
	return toucher


def coordonnées_clic(texte, x, y):
	""" 
	Cette fonction renvoie les coordonnées de la zone de texte
	(les points supérieur gauche et inférieur droit) dans lequel il y a 
	le texte.
	
	"""
	largeur, hauteur = taille_texte(texte)
	return (x - (largeur / 2), y - (hauteur / 2), x + (largeur / 2), y + (hauteur / 2))


def couler(plateau, liste_bateau): #faut faire cette putain de fonction jsp comment faire 
	for taille_bateau in liste_bateau:
		for elem in taille_bateau:
			if plateau[elem[1]][elem[0]] != 2:		#touché
				break
		else:
			if taille_bateau:
				print("Coulé !")
				for elem in taille_bateau:
					plateau[elem[1]][elem[0]] = 5


def gagner(plateau, liste_bateau):
	for taille_bateau in liste_bateau:
		for elem in taille_bateau:
			if plateau[elem[1]][elem[0]] != 5:
				return False
	return True
				

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
            1500 * 4 / 5,
            1000 // 4 - 25,
            texte_,
            couleur="white",
            ancrage="center",
            tag="texte_input",
        )
        mise_a_jour()


def my_input(msg, type_retour, reponse_defaut=""):
    """affichage de l'input"""
    rectangle(
        1500 * 4 / 5 - 250,
        1000 // 4 - 200 - 25,
        1500 * 4 / 5 + 250,
        1000 // 4 + 200  - 25,
        couleur="gray28",
        remplissage="gray",
        epaisseur=5,
        tag="cadre",
    )

    while True:
        texte(
            1500 * 4 / 5,
            1000 // 4 - 100 - 25,
            msg,
            couleur="white",
            ancrage="center",
            tag="msg",
        )
        _var = _input(msg, reponse_defaut)
        if type_retour == "int":
            if _var.isdigit():
                if int(_var) < 20:
                    efface("msg")
                    efface("texte_input")
                    efface("cadre")
                    return int(_var)
        else:
            efface("msg")
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

	choix_mode = [("Mode classique", 640, 200),  
		("Mode aléatoire", 640, 300),
		("Mode prof", 640, 400),
		("Quitter", 640, 500)]

	liste_bateau_joueur1 = [[] for i in range(6)]
	liste_bateau_joueur2 = [[] for i in range(6)]
	# liste_bateau = []
	# for i in range(6):
	# 	liste_bateau.append([])

	navires = []
	for x in range(6, 0, -1):
		navires.append([])
		for y in range(7-x):
			navires[-1].append(x)


	cree_fenetre(1500, 1000)

	rectangle(0, 0, 1500, 1000, couleur='darkblue', remplissage='darkblue')
	polygone((200, 150, 300, 230, 100, 230), epaisseur=3)
	ligne(200, 150, 200, 240, epaisseur=3)
	polygone((75, 240, 325, 240, 300, 270, 100, 270, 75, 240), epaisseur=3)
	for i in range(len(choix_mode)):
		texte(640, 50, 'Bataille Navale', ancrage = "center", couleur='red', police='Helvetica', taille=50)
		texte(choix_mode[i][1], choix_mode[i][2], choix_mode[i][0], ancrage = "center", couleur='white', police='Helvetica', taille=30)

	while menu:
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
	efface_tout()

	debut = time()
	plateau1 = init(20)
	plateau2 = init(20)


	dessine_grille(0, 0, plateau1)
	dessine_grille(25, 0, plateau2)

	dessine_bateau(plateau1, 25, 530, 'j1', 0, 0, liste_bateau_joueur1, navires[:1])
	texte(750, 500, "C'est au tour de j2 de placer ses bateaux !", couleur='red', ancrage='center', police='Helvetica', taille=50)

	dessine_bateau(plateau2, 900, 530, 'j2', 25, 0, liste_bateau_joueur2, navires[:1])
	print(liste_bateau_joueur1)
	print(liste_bateau_joueur2)


	a_gagner = False
	gagnant = None
	while jouer and not a_gagner:
		efface_tout()
		# affiche_plateau(plateau1)

		dessine_grille(0, 0, plateau1)
		dessine_grille(25, 0, plateau2)
		dessine_grille(0, 25, plateau2, True)
		dessine_grille(25, 25, plateau1, True)

		#joueur 1
		tour_j1 = True
		while tour_j1 and not a_gagner:
			print("j1")
			tour_j1 = touch(plateau2, liste_bateau_joueur2)
			dessine_grille(0, 25, plateau2, True)
			dessine_grille(25, 0, plateau2)

			a_gagner = gagner(plateau2, liste_bateau_joueur2)
			if a_gagner:
				gagnant = "Joueur 1"

		#joueur 2
		tour_j2 = True
		while tour_j2 and not a_gagner:
			print("j2")
			tour_j2 = touch(plateau1, liste_bateau_joueur1)
			dessine_grille(25, 25, plateau1, True)
			dessine_grille(0, 0, plateau1)

			a_gagner = gagner(plateau1, liste_bateau_joueur1)
			if a_gagner:
				gagnant = "Joueur 2"



	efface_tout()
	texte(1500 // 2, 1000 // 2, "Gagnant: {}".format(gagnant), ancrage = "center", couleur='red', police='Helvetica', taille=50)


		


	attend_fermeture()


