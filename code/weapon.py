import pygame 

class Weapon(pygame.sprite.Sprite):
	def _init_(self,player,groups):
		super()._init_(groups)
		direction = player.status.split('_')[0]

		# graphic
		full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
		self.image = pygame.image.load(full_path).convert_alpha()
		
        