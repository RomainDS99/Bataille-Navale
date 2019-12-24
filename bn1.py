from upemtk import *
from random import randint
from time import sleep, time

taille_case = 25
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
				if 0 <= y - i < hauteur_plateau and 0 <= x < largeur_plateau:
					plateau[y-i][x]=1
				else:
					return False

			elif direction == 1:
				if x + taille > largeur_plateau:
					return False
				elif (0 <= y < hauteur_plateau) and (0 <= x + i < largeur_plateau):
					plateau[y][x+i]=1
				else:
					return False

			elif direction == 2:
				if y + taille > hauteur_plateau:
					return False
				elif (0 <= y + i < hauteur_plateau) and (0 <= x < largeur_plateau):
					plateau[y+i][x]=1
				else:
					return False

			elif direction == 3:
				if 0 <= y < hauteur_plateau and 0 <= x - i < largeur_plateau:
					plateau[y][x-i]=1
				else:
					return False

		return True

def demande(taille):
	x = int(input("abscisse de la tete du bateau: "))
	y = int(input("ordonnée de la tete du bateau: "))
	direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	return x, y, taille, direction

def sortie_bateau(taille, plateau):
	placement = False
	while not placement:
		x, y, taille, direction = demande(taille)
		if placer_bateau(x, y, taille, direction, plateau) == False:
			if direction == 0:
				for i in range(y-taille, y+1):
					plateau[i][x]=0
			if direction == 1:
				for i in range(x, len(plateau)):
					plateau[y][i]=0
			if direction == 2:
				for i in range(y, len(plateau)):
					plateau[i][x]=0
			if direction == 3:
				for i in range(x-taille, x+1):
					plateau[y][i]=0

		elif placer_bateau(x, y, taille, direction, plateau) == True:
			placement = placer_bateau(x, y, taille, direction, plateau)

			
def dessine_bateau(plateau, x, y, j, j_bis):
	texte(x, y, "Grille de bateaux de " + j, couleur='red', ancrage='nw', police='Helvetica', taille=30)
	texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de votre bateau de 6 cases [1]")
	sortie_bateau(6, plateau)
	efface(texte1)
	dessine_grille(25, 25, plateau)

	for i in range(2):
		nb = 2 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 5 cases [" + str(nb) + ']')
		sortie_bateau(5, plateau)
		efface(texte1)
		dessine_grille(25, 25, plateau)	
	efface(texte1)

	for i in range(3):
		nb = 3 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 4 cases [" + str(nb) + ']')
		sortie_bateau(4, plateau)
		efface(texte1)
		dessine_grille(25, 25, plateau)
	efface(texte1)

	for i in range(4):
		nb = 4 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 3 cases [" + str(nb) + ']')
		sortie_bateau(3, plateau)
		efface(texte1)
		dessine_grille(25, 25, plateau)		
	efface(texte1)

	for i in range(5):
		nb = 5 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 2 cases [" + str(nb) + ']')
		sortie_bateau(2, plateau)
		efface(texte1)
		dessine_grille(25, 25, plateau)
	efface(texte1)

	for i in range(6):
		nb = 6 - i
		texte1 = texte(x, y + 35, "Veuillez rentrez les coordonnées et la direction de vos bateaux de 1 case [" + str(nb) + ']')
		sortie_bateau(1, plateau)
		efface(texte1)
		dessine_grille(25, 25, plateau)
	efface(texte1)

	efface(dessine_grille(25, 25, plateau1)) #efface pas la grille de j1 ni texte fin ca efface rien en fait 
	texte(750, 500, "C'est au tour de " + j_bis + " de placer ses bateaux !", couleur='red', ancrage='center', police='Helvetica', taille=50)


def tir(x, y, plateau):
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
			carre(i, j, "white", "darkblue")
			if plateau[j][i] == 1:
				carre(i, j, "white", "red")

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
		x_tir = int(input("abscisse du tir: "))
		y_tir = int(input("ordonnée du tir: "))
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


def couler(plateau):
	for x in range(len(plateau)):
		for y in range(len(plateau)):
			if plateau[x][y] != 1 and plateau[x][y] != 3 and plateau[x][y] != 4 and plateau[x][y] != 0:
				plateau[x][y] = 5

if __name__ == "__main__":

	# initialisation du jeu 
	score = 0
	menu = True
	jouer = False
	joueur_1 = False
	joueur_2 = False

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
	while jouer:
		efface_tout()
		plateau1 = init(20)
		dessine_grille(25, 25, plateau1)
		dessine_bateau(plateau1, 25, 530, 'j1', 'j2')
		
		
		plateau2 = init(20)
		dessine_grille(900, 25, plateau2)
		dessine_bateau(plateau2, 900, 530, 'j2', 'j1')



		affiche_plateau(plateau1)

		dessine_grille(25, 25, plateau1)

		touch(plateau1)

		affiche_plateau(plateau1)
		


		attend_fermeture()

