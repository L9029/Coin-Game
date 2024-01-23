import pygame, random

class Food(pygame.sprite.Sprite):
    def __init__(self, images_dict, selected_key, screen_size, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen_size = screen_size
        self.images = images_dict[selected_key]
        self.mask = pygame.mask.from_surface(self.images)
        self.rect = self.images.get_rect()
        self.rect.left, self.rect.bottom = random.randint(20, screen_size[0] - 20), -10
        self.speed = random.randrange(5, 10)
        self.score = 1 if selected_key == "gold" else 5
    
    def update(self):
        self.rect.bottom += self.speed
        
        if self.rect.top > self.screen_size[1]:
            return True
        return False