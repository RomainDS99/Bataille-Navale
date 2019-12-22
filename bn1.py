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
				plateau[y-i][x]=1

		elif direction == 1:
				plateau[y][x+i]=1

		elif direction == 2:
				plateau[y+i][x]=1

		elif direction == 3:
				plateau[y][x-i]=1

	

def demande():
	x = saisie_controlee("abscisse de la tete du bateau: ")
	y = saisie_controlee("ordonnée de la tete du bateau: ")
	taille = int(input("taille du bateau en cases: "))
	while taille > 6:
		print("Mauvaise saisie.")
		taille = int(input("taille du bateau en cases: "))
	direction = int(input("orientation du bateau vers Nord, Est, Sud, Ouest: [0, 1, 2, 3] "))
	return x, y, taille, direction

def control_placement(x, y, taille, direction):
	if direction == 0:
		if y >= taille:
			return True 
		return False
	if direction == 1:
		if x + taille <= len(plateau1[0]):
			return True
		return False
	if direction == 2:
		if y + taille <= len(plateau1):
			return True 
		return False
	if direction == 3:
		if x >= taille:
			return True 
		return False

	
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

def saisie_controlee(msg):
	while True:
		x = input(msg)
		if x.isdigit() and 0 <= int(x) <= 20:
			return int(x)
		print("Mauvaise saisie.")


cree_fenetre(1500, 1000)
plateau1 = init(20)
dessine_grille(25, 25, plateau1)
#navires=[1, 1, 1, 1, 1, 1],[[2, 2], [2, 2], [2, 2], [2, 2]],[[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]] [[5, 5], [5, 5]], [6]

placement = False
while not placement:
	x, y, taille, direction = demande()
	if not control_placement(x, y, taille, direction):
		continue
	placer_bateau(x, y, taille, direction, plateau1)
	#si il n'y a plus de bateau à placer placement = True
	placement = True


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



