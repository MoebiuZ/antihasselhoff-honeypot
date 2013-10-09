import pygame
import os

width = 1920
height = 1080

quit = False
lockscreen = False
done = False

pygame.init()

winpath = os.environ["windir"]

flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
screen = pygame.display.set_mode((width, height), flags)


backg = pygame.image.load(os.path.join('', 'full.bmp'))
unicorn = pygame.image.load(os.path.join('', 'unicornio.bmp'))


file = 'trololo.ogg'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)


screen.blit(backg, (0, 0))
pygame.display.flip()


pygame.mouse.set_visible(True)

mousex, mousey = pygame.mouse.get_pos()


while not quit:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:

			m = pygame.key.get_mods()

			if event.key == pygame.K_PERIOD and m & pygame.KMOD_SHIFT:
				quit = True
				exit()
			elif event.key != pygame.K_LSHIFT:
				if done == False:
					quit = True
					done = True
					
					screen.blit(unicorn, (0,0))					
					pygame.display.flip()
					pygame.mixer.music.play()
					
		elif event.type == pygame.MOUSEMOTION:
			mousex2, mousey2 = pygame.mouse.get_pos() 
			if done == False and (mousex2 != mousex or mousey2 != mousey):
				quit = True
				done = True
				
				screen.blit(unicorn, (0,0))
				pygame.display.flip()
				pygame.mixer.music.play()
				

while not lockscreen:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_RCTRL) or (event.key == pygame.K_RALT) or (event.key == pygame.K_LCTRL) or (event.key == pygame.K_LALT):
				lockscreen = True

	
os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')
