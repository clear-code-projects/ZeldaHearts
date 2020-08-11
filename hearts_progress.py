import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('link.png').convert_alpha()
		self.rect = self.image.get_rect(center = (400,400))
		self.health = 5
		self.max_health = 20

	def get_damage(self):
		if self.health > 0:
			self.health -= 1

	def get_health(self):
		if self.health < self.max_health:
			self.health += 1

	def full_hearts(self):
		for heart in range(self.health):
			screen.blit(full_heart,(heart * 50 + 10,45))

	def empty_hearts(self):
		for heart in range(self.max_health):
			if heart < self.health:
				screen.blit(full_heart,(heart * 50 + 10,5))
			else:
				screen.blit(empty_heart,(heart * 50 + 10,5))

	def half_hearts(self):
		half_hearts_total = self.health / 2
		half_heart_exists = half_hearts_total - int(half_hearts_total) != 0

		for heart in range(int(self.max_health / 2)):
			if int(half_hearts_total) > heart:
				screen.blit(full_heart,(heart * 50 + 10,85))
			elif half_heart_exists and int(half_hearts_total) == heart:
				screen.blit(half_heart,(heart * 50 + 10,85))
			else:
				screen.blit(empty_heart,(heart * 50 + 10,85))

	def update(self):
		self.full_hearts()
		self.empty_hearts()
		self.half_hearts()

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
link = pygame.sprite.GroupSingle(Player())

full_heart = pygame.image.load('full_heart.png').convert_alpha()
half_heart = pygame.image.load('half_heart.png').convert_alpha()
empty_heart = pygame.image.load('empty_heart.png').convert_alpha()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				link.sprite.get_health()
			if event.key == pygame.K_DOWN:
				link.sprite.get_damage()

	screen.fill((30,30,30))
	link.draw(screen)
	link.update()
	pygame.display.update()
	clock.tick(60)