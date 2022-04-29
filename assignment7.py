# AnhTu Vothang (---------) 

import pygame

window = pygame.display.set_mode()

#Load image and create corrrect size window
image = pygame.image.load("puppy.jpg").convert()
(height, width) = image.get_size()
window = pygame.display.set_mode((height, width))

#Blit loaded image onto window
window.blit(image, (0, 0))

print(height)
print(width)

exit_flag = False
while not exit_flag:
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit_flag = True
	
		#not sure how to implement the following into code: (button1, button2, button3) = pygame.mouse.get_pressed()
		#when you click the mouse, a 10 pixel by 10 pixel square of the inverted colour appears
		#not sure how to allow the user to select all the pixels they want to invert
		if e.type == pygame.MOUSEBUTTONDOWN:
			(x, y) = pygame.mouse.get_pos()
			
			for i in range(x,x+100):
				for j in range(y,y+100):
					(r, g, b, __) = image.get_at((i, j))
					print(x)
					
					#inverted colour calculation:
					rr = 255-r
					gg = 255-g
					bb = 255-b
				
					#tried impleting "set_at" but I couldn't figure out how
					#pygame.draw.rect(window, (rr, gg, bb), (i,j,1, 1))
					window.set_at((i, j), (rr,gg,bb))

	pygame.display.update()
