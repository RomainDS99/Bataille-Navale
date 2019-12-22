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


def coule(plateau):
	for x in range(len(plateau)):
		for y in range(len(plateau)):
			if plateau[x][y] != 1 and plateau[x][y] != 3 and plateau[x][y] != 4 and plateau[x][y] != 0:
				plateau[x][y] = 5


cree_fenetre(1500, 1000)
plateau1 = init(20)
dessine_grille(25, 25, plateau1)
#navires=[1, 1, 1, 1, 1, 1],[[2, 2], [2, 2], [2, 2], [2, 2]],[[3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]] [5, 5], [6]

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
	affiche_plateau(plateau1)

affiche_plateau(plateau1)


attend_fermeture()

Bondoufle

