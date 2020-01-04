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
	"""
	fonction qui verifie que le bateau a assez de place pour etre mis au coordonnées demandées 
	:param x: int 0 <= x <= 19
	:param y: int 0 <= y <= 19
	:param taille: int 1 <= taille <= 6
	:param direction: int 0 <= direction <= 3
	:param plateau: lst

	"""
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
	""" 
	fonction qui demande les coordonnées de l'emplacement souhaité du bateau 
	:param taille: int 1 <= taille <= 6

	"""
	# x = int(input("abscisse de la tete du bateau: "))
	x = my_input("abscisse de la\n tete du bateau: ", "int")
	# y = int(input("ordonnée de la tete du bateau: "))
	y = my_input("ordonnée de la\n tete du bateau: ", "int")
	# direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	direction = my_input("    orientation du bateau \n\t  vers\n   Nord, Est, Sud, Ouest: \n            [0, 1, 2, 3] ", "int")
	return x, y, taille, direction


def sortie_bateau(taille, plateau, liste_bateau):
	""" 
	fonction qui verifie si le bateau peut etre placé et redemande des coordonnées si non
	:param taille: int 1 <= taille <= 6
	:param plateau: lst
	:param liste_bateau: lst

	"""
	placement = False
	while not placement:
		x, y, taille, direction = demande(taille)
		if control_placement(x, y, taille, direction, plateau):
			bateau = placer_bateau(x, y, taille, direction, plateau)
			placement = True
			for elem in bateau:
				liste_bateau[taille - 1].append(elem)

deplacement = [(0, 0), (0, -1), (-1, -1), (1, -1), (0, 1), (1, 1), (-1, 1), (1, 0), (-1, 0)]
def control_placement(x, y, taille, direction, plateau):
	"""
	fonction qui controle qu'il n'y ait pas déjà de bateau placé aux coordonnées souhaitées
	:param x: int 0 <= x <= 19
	:param y: int 0 <= y <= 19
	:param taille: int 1 <= taille <= 6
	:param direction: int 0 <= direction <= 3
	:param plateau: lst

	"""
	if direction == 0:
		if y + 1 >= taille:
			for i in range(y-taille + 1, y+1):
				for direction_x, direction_y in deplacement:
					if 0 <= x + direction_x < 20 and 0 <= i + direction_y < 20:
						x += direction_x
						y = i + direction_y
					else:
						continue
					if plateau[y][x] != 0:
						return False
			return True 
		return False
	if direction == 1:
		if x + taille <= len(plateau[0]):
			for i in range(x, x + taille):
				for direction_x, direction_y in deplacement:
					if 0 <= i + direction_x < 20 and 0 <= y + direction_y < 20:
						x = i + direction_x
						y += direction_y
					else:
						continue
					if plateau[y][x] != 0:
						return False
			return True
		return False
	if direction == 2:
		if y + taille <= len(plateau):
			for i in range(y, y + taille):
				for direction_x, direction_y in deplacement:
					if 0 <= x + direction_x < 20 and 0 <= i + direction_y < 20:
						x += direction_x
						y = i + direction_y
					else:
						continue
					if plateau[y][x] != 0:
						return False
			return True 
		return False
	if direction == 3:
		if x + 1 >= taille:
			for i in range(x-taille + 1, x+1):
				for direction_x, direction_y in deplacement:
					if 0 <= i + direction_x < 20 and 0 <= y + direction_y < 20:
						x = i + direction_x
						y += direction_y
					else:
						continue
					if plateau[y][x] != 0:
						return False
			return True 
		return False

			
def dessine_bateau(plateau, x, y, j, placement_x, placement_y, liste_bateau, navires):
	"""
	fonction qui dessine les bateaux si les caracteristiques sont respectées, cad qu
	:param plateau: lst
	:param x: int
	:param y: int
	param j: str
	param placement_x: int
	:param placement_y: int
	:param liste_bateau: lst
	:param navires: lst

	"""
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
	"""
	fonction qui détermine ou le tir a été lancé, sur un bateau ou dans l'eau,
	:param x: int 0 <= x <= 19
	:param y: int 0 <= y <= 19
	:param plateau: lst

	"""
#touché
	if plateau[y][x] == 1:
		plateau[y][x] = 2
		print("Touché !")
		txt = texte(250, 700 * 5/6, "Touché !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)
		return True
#en vue 
	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y - 1][x] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y - 1][x - 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y - 1][x + 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y + 1][x] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y + 1][x + 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y + 1][x - 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y][x + 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

	elif 0 <= x < 20 and 0 <= y < 20 and plateau[y][x - 1] in {1, 2}:
		plateau[y][x] = 4
		print("En vue !")
		txt = texte(250, 700 * 5/6, "En vue !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)

#rien
	else:
		plateau[y][x] = 3
		print("Dommage !")
		txt = texte(250, 700 * 5/6, "Dommage !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
		attente(1)
		efface(txt)
	return False


def carre(x, y, c1, c2):
	"""
	fonction qui dessine un rectangle
	:param x: int
	:param y: int
	:param c1: str couleur contour
	:param c2: str couleur remplissage 

	"""
	rectangle(x*taille_case+taille_case, y*taille_case+taille_case, x*taille_case+2*taille_case, y*taille_case+2*taille_case, c1, c2)


def dessine_grille(x, y, plateau, tir=False):
	"""
	focntion qui dessine la grille qui prend en commpte l'état des bateaux et les tirs effectués
	:param x: int
	:param y: int
	:param plateau: lst

	"""
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
	"""
	fonction qui dessine les chiffres allant de 0 à 19
	:param x: int
	:param y: int

	"""
	for i in range(largeur_plateau):
		largeur, hauteur = taille_texte(texte)
		texte((x + 1) * taille_case + i * taille_case + taille_case // 2, y * taille_case + taille_case // 2, i, ancrage="center", police="Impact", taille=12)
		texte(x * taille_case + taille_case // 2, (y + 1) * taille_case + i * taille_case + taille_case // 2, i, ancrage="center", police="Impact", taille=12)


def touch(plateau, liste_bateau):
	"""
	fonction qui redemande des coordonnées au joueur si un tir a touché un bateau
	:param plateau: lst
	:param liste_bateau: lst

	"""
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
	"""
	fonction qui détermine si un bateau est coulé
	:param plateau: lst
	:param liste_bateau: lst

	""" 
	for taille_bateau in liste_bateau:
		for elem in taille_bateau:
			if plateau[elem[1]][elem[0]] != 2:		#touché
				break
		else:
			if taille_bateau:
				print("Coulé !")
				txt = texte(250, 700 * 5/6, "Coulé !", couleur='magenta', ancrage='nw', police='Helvetica', taille=50, tag='')
				attente(1)
				efface(txt)
				for elem in taille_bateau:
					plateau[elem[1]][elem[0]] = 5


def gagner(plateau, liste_bateau):
	"""
	fonction qui détermine si tous les bateaux sont coulés, donc si un joueur a gagné
	:param plateau: lst
	:param liste_bateau: lst
	
	"""
	for taille_bateau in liste_bateau:
		for elem in taille_bateau:
			if plateau[elem[1]][elem[0]] != 5:
				return False
	return True
				

def bateaux_aleatoire(plateau, liste_bateau, navires):
	"""
	fonction qui permet de placer les bateaux de facon aléatoire
	:param plateau: lst

	"""
	for liste_taille_bateau in navires:
		for taille in liste_taille_bateau:
			while True:
				x = randint(0, 19)
				y = randint(0, 19)
				direction = randint(0, 3)
				if control_placement(x, y, taille, direction, plateau):
					bateau = placer_bateau(x, y, taille, direction, plateau)
					for elem in bateau:
						liste_bateau[taille - 1].append(elem)
					break


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
            1300 * 4 / 5 + 60,
            700 //4 + 30,
            texte_,
            couleur="#ff0000",
            ancrage="center",
            tag="texte_input",
        )
        mise_a_jour()


def my_input(msg, type_retour, reponse_defaut=""):
    """affichage de l'input"""
    rectangle(1300 * 4 / 5 - 90, 700 // 4 - 150, 1300 * 4 / 5 + 215, 700 // 4 + 100,
        #1500 * 4 / 5 - 250,
        #1000 // 4 - 200 - 25,
        #1500 * 4 / 5 + 250,
        #1000 // 4 + 200  - 25,
        couleur="gray28",
        remplissage="gray",
        epaisseur=5,
        tag="cadre",
    )

    while True:
        texte(1300 * 4 / 5 + 60, 700 // 4 - 70,
            #1500 * 4 / 5,
            #1000 // 4 - 100 - 25,
            msg,
            couleur="white",
            ancrage="center",
	    taille=20,
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


def affichage(x, plateau, x2, plateau_2, prof):
	"""
	fonction qui affiche les grilles de bateaux et de tirs, des deux joueurs si mode prof activé
	:param x: int
	:param plateau: lst
	:param x2: int
	:param plateau_2: lst
	param prof: bool

	"""
	dessine_grille(x, 0, plateau_2, True)
	dessine_grille(x + 21, 0, plateau)
	if prof:
		dessine_grille(x2, 14, plateau_2)



if __name__ == "__main__":

	# initialisation du jeu 
	score = 0
	menu = True
	jouer = False
	joueur_1 = False
	joueur_2 = False
	mode_prof = False

	choix_mode = [("Mode classique", 1300/2, 700*1/3), 
		("Mode aléatoire", 1300/2, 700/2),
		("Mode prof", 1300/2, 700*2/3), 
		("Quitter", 1300/2, 700-25)] 

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

	plateau1 = init(20)
	plateau2 = init(20)
	

	cree_fenetre(1300, 700)

	while menu:
		rectangle(0, 0, 1500, 1000, couleur='darkblue', remplissage='darkblue')
		polygone((200, 150, 300, 230, 100, 230), epaisseur=3)
		ligne(200, 150, 200, 240, epaisseur=3)
		polygone((75, 240, 325, 240, 300, 270, 100, 270, 75, 240), epaisseur=3)

		for mode in choix_mode:
			texte(640, 50, 'Bataille Navale', ancrage = "center", couleur='red', police='Helvetica', taille=50)
			if mode[0] != "Mode prof":
				texte(mode[1], mode[2], mode[0], ancrage = "center", couleur='white', police='Helvetica', taille=30)
			elif not mode_prof:
				texte(mode[1], mode[2], mode[0], ancrage = "center", couleur='#ff0000', police='Helvetica', taille=30)
			else:
				texte(mode[1], mode[2], mode[0], ancrage = "center", couleur='#00ff00', police='Helvetica', taille=30)

		(x, y) = attend_clic_gauche()
		for i in range(len(choix_mode)):
			x1, y1 , x2, y2 = coordonnées_clic(*choix_mode[i])
			if x1 < x < x2 and y1 < y < y2:
				mode = choix_mode[i][0]
				if mode == "Mode prof":
					mode_prof = not mode_prof

				elif mode == "Mode classique":
					jouer = True 
					menu = False
					aleatoire = False
				elif mode == "Mode aléatoire":
					jouer = True 
					menu = False
					aleatoire = True
				else:
					exit()
		efface_tout()

	debut = time()

	if not aleatoire:
		nb_bateau = my_input("nombre de bateaux\n         (0 = tout)", "int")
		if nb_bateau == 0:
			debut = 0
			fin = 6
		else:
			debut = nb_bateau - 1
			fin = nb_bateau

		dessine_grille(0, 0, plateau1)

		dessine_bateau(plateau1, 25, 430, 'j1', 0, 0, liste_bateau_joueur1, navires[debut:fin])
		attend_clic_gauche()
		efface_tout()

		txt = texte(1300/2, 700/2, "C'est au tour de j2 de placer ses bateaux !", couleur='red', ancrage='center', police='Helvetica', taille=50)
		attente(3)
		efface(txt)
		
		dessine_grille(0, 0, plateau2)
		dessine_bateau(plateau2, 25, 430, 'j2', 0, 0, liste_bateau_joueur2, navires[debut:fin])
		attend_clic_gauche()
	else:
		bateaux_aleatoire(plateau1, liste_bateau_joueur1, navires)


	a_gagner = False
	gagnant = None
	while jouer and not a_gagner:
		efface_tout()
		# affiche_plateau(plateau1)

		# dessine_grille(0, 0, plateau1)
		# dessine_grille(25, 0, plateau2)
		# dessine_grille(0, 25, plateau2, True)
		# dessine_grille(25, 25, plateau1, True)

		#joueur 1
		tour_j1 = True
		while tour_j1 and not a_gagner:
			efface_tout()
			print("j1")

			affichage(0, plateau1, 42, plateau2, mode_prof)
			texte(25, 425, "Grille de tirs de J1")
			texte(440, 425, "Grille de bateaux de J1")
			tour_j1 = touch(plateau2, liste_bateau_joueur2)
			affichage(0, plateau1, 42, plateau2, mode_prof)
			attend_clic_gauche()

			a_gagner = gagner(plateau2, liste_bateau_joueur2)
			if a_gagner:
				gagnant = "Joueur 1"

		#joueur 2
		tour_j2 = True
		while tour_j2 and not a_gagner:
			efface_tout()
			print("j2")
			affichage(0, plateau2, 42, plateau1, mode_prof)
			texte(25, 425, "Grille de tirs de J2")
			texte(440, 425, "Grille de bateaux de J2")
			tour_j2 = touch(plateau1, liste_bateau_joueur1)
			affichage(0, plateau2, 42, plateau1, mode_prof)
			attend_clic_gauche()

			a_gagner = gagner(plateau1, liste_bateau_joueur1)
			if a_gagner:
				gagnant = "Joueur 2"



	efface_tout()
	texte(1300 // 2, 700 // 2, "Gagnant: {}".format(gagnant), ancrage = "center", couleur='red', police='Helvetica', taille=50)


		


	attend_fermeture()


