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

clock = pygame.time.Clock()

exit = False
while not exit:
	clock.tick(5)

	canvas.fill((0, 0, 0))

	for a in range(0, 1000, velikost):
		for b in range (0, 1000, velikost):
			if(a//velikost + b//velikost)%2 == 0 :
				pygame.draw.rect(canvas, barva1, (a, b, velikost, velikost))
			else:
				pygame.draw.rect(canvas, barva2, (a, b, velikost, velikost))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True

	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a and smer != "right":
				smer = "left"
			elif event.key == pygame.K_d and smer != "left":
				smer = "right"
			elif event.key == pygame.K_w and smer != "down":
				smer = "up"
			elif event.key == pygame.K_s and smer != "up":
				smer = "down"

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


	pygame.draw.rect(canvas, (200, 0, 0), kvadrat)

	pygame.display.update()