#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repozitorij, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave

#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov 

import pygame
import random

pygame.init()

game_over = False

canvas = pygame.display.set_mode((1000, 1000))
x = 50
y = 50
pygame.display.set_caption("kaca")
kvadrat = pygame.Rect(x, y, 50, 50)

barva1 = (39, 150, 11)
barva2 = (50, 199, 12)
velikost = 50

smer = "right"

dolzina_kaca = 1

barve = ((30, 17, 184), (240, 193, 53), (56, 14, 52), (232, 46, 214))

clock = pygame.time.Clock()

exit = False

sadje = []

stev_sadje = 0

while not exit:
	clock.tick(5)

	canvas.fill((0, 0, 0))

	obrat = False

	for a in range(0, 1000, velikost):
		for b in range (0, 1000, velikost):
			if(a//velikost + b//velikost)%2 == 0 :
				pygame.draw.rect(canvas, barva1, (a, b, velikost, velikost))
			else:
				pygame.draw.rect(canvas, barva2, (a, b, velikost, velikost))

	for a in range(3):
		if stev_sadje != 3:
			sadje_x = random.randint(0, 20)*50
			sadje_y = random.randint(0, 20)*50
			nou = True
			if sadje_x in sadje and sadje_y in sadje:
				sadje.append((sadje_x, sadje_y, random.choice(barve)))
			else:
				while nou:
					sadje_x = random.randint(0, 20)*50
					sadje_y = random.randint(0, 20)*50
					if sadje_x in sadje and sadje_y in sadje:
						sadje.append((sadje_x, sadje_y, random.choice(barve)))
						nou = False

			stev_sadje += 1

	for b in range(len(sadje)):
		pygame.draw.rect(canvas, sadje[b][2], (sadje[b][0], sadje[b][1], velikost, velikost))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True

	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a and smer != "right" and obrat != True:
				smer = "left"
				obrat = True
			elif event.key == pygame.K_d and smer != "left" and obrat != True:
				smer = "right"
				obrat = True
			elif event.key == pygame.K_w and smer != "down" and obrat != True:
				smer = "up"
				obrat = True
			elif event.key == pygame.K_s and smer != "up" and obrat != True:
				smer = "down"
				obrat = True

	if smer == "right":
		x += 50
	elif smer == "left":
		x -= 50
	elif smer == "up":
		y -= 50
	elif smer == "down":
		y += 50


	kvadrat = pygame.Rect(x, y, 50, 50)

	if not (x >= 0 and x<= 1000):
		game_over = True
	elif not (y >= 0 and y<= 1000):
		game_over = True

	while game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
				game_over = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					exit = False
					game_over = False
					x = 50
					y = 50
					smer = "right"
					obrat = False
					dolzina_kaca = 1
					sadje = []
					stev_sadje = 0


	pygame.draw.rect(canvas, (200, 0, 0), kvadrat)

	pygame.display.update()