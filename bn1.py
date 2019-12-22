from upemtk import *
from random import randint

taille_case = 25
largeur_plateau = 21 
hauteur_plateau = 21

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
	for i in range(taille):
		if direction == 0:
			if 0 <= y - i < hauteur_plateau and 0 <= x < largeur_plateau:
				plateau[y-i][x]=1
			else:
				return False

		elif direction == 1:
			if 0 <= y < hauteur_plateau and 0 <= x + i < largeur_plateau:
				plateau[y][x+i]=1
			else:
				return False

		elif direction == 2:
			if 0 <= y + i < hauteur_plateau and 0 <= x < largeur_plateau:
				plateau[y+i][x]=1
			else:
				return False

		elif direction == 3:
			if 0 <= y < hauteur_plateau and 0 <= x - i < largeur_plateau:
				plateau[y][x-i]=1
			else:
				return False

	return True

def demande():
	x = int(input("abscisse de la tete du bateau:"))
	y = int(input("ordonnée de la tete du bateau: "))
	taille = int(input("taille du bateau en cases: "))
	direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	return x, y, taille, direction

	
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



def coordonnées_clic(texte, x, y):
	""" 
	Cette fonction renvoie les coordonnées de la zone de texte
	(les points supérieur gauche et inférieur droit) dans lequel il y a 
	le texte.
	
	"""
	largeur, hauteur = taille_texte(texte)
	return (x - (largeur / 2), y - (hauteur / 2), x + (largeur / 2), y + (hauteur / 2))


def couler(plateau, taille, direction):
	for x in range(len(plateau)):
		for y in range(len(plateau)):
			if plateau[y][x] = 2:
				while plateau[y][x] != 1 and plateau[y][x] != 3  and plateau[y][x] != 4 and plateau[y][x] != 0:
					
				
			if plateau[x][y] != 1 and plateau[x][y] != 3 and plateau[x][y] != 4 and plateau[x][y] != 0:
				plateau[x][y] = 5

				
# initialisation du jeu
if __name__ == "__main__": 
	score = 0
	menu = True
	jouer = False
	navires=[[1, 1, 1, 1, 1, 1]],[[2, 2], [2, 2], [2, 2], [2, 2]],[[3, 3, 3], [3, 3, 3], [3, 3, 3]], 
	[[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]], [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5]] [[6], [6], [6], [6], [6], [6]]
	choix_mode = [("Mode classique ", 640, 200),  
		("Mode aléatoire", 640, 300),
		("Mode prof", 640, 400),
		("Quitter", 640, 500)]


	cree_fenetre(1500, 1000)
	while menu:
		rectangle(0, 0, 1500, 1000, couleur='darkblue', remplissage='darkblue')
		polygone((200, 150, 300, 230, 100, 230), epaisseur=3)
		ligne(200, 150, 200, 240, epaisseur=3)
		ligne(75, 240, 325, 240, epaisseur=3)
		ligne(75, 240, 100, 270, epaisseur=3)
		ligne(325, 240, 300, 270, epaisseur=3)
		ligne(100, 270, 300, 270, epaisseur=3)

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


	while jouer:
		efface_tout()
		plateau1 = init(20)
		dessine_grille(25, 25, plateau1)

		placement = False
		while not placement:
			x, y, taille, direction = demande()
			if placer_bateau(x, y, taille, direction, plateau1) == False:
				for i in range(len(plateau1)):
					for j in range(len(plateau1[i])):
						plateau1[j][i]=0 #ca marche que pour nord et ouest, pour sud et est ca met out of range 

			elif placer_bateau(x, y, taille, direction, plateau1) == True:
				placement = placer_bateau(x, y, taille, direction, plateau1)

		affiche_plateau(plateau1)
		dessine_grille(25, 25, plateau1)
		toucher = True
		while toucher:
			x_tir = int(input("abscisse du tir: "))
			y_tir = int(input("ordonnée du tir: "))
			toucher = tir(x_tir, y_tir, plateau1)
			hit(x_tir, y_tir, plateau1)
			affiche_plateau(plateau1)

		affiche_plateau(plateau1)
		


		attend_fermeture()
