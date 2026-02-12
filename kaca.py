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

canvas = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("kaca")
kvadrat = pygame.Rect(30, 30, 50, 50)

barva1 = (39, 150, 11)
barva2 = (50, 199, 12)
velikost = 50

exit = False
while not exit:
	canvas.fill((0, 0, 0))

	for x in range(0, 1000, velikost):
		for y in range (0, 1000, velikost):
			if(x//velikost + y//velikost)%2 == 0 :
				pygame.draw.rect(canvas, barva1, (x, y, velikost, velikost))
			else:
				pygame.draw.rect(canvas, barva2, (x, y, velikost, velikost))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True

	pygame.draw.rect(canvas, (200, 0, 0), kvadrat)

	pygame.display.update()