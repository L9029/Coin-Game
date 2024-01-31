import pygame, random

class Food(pygame.sprite.Sprite):
    def __init__(self, images_dict, selected_key, screen_size, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen_size = screen_size
        self.images = images_dict[selected_key] #This select and image of the dict with the key
        self.mask = pygame.mask.from_surface(self.images) #This detected the collision in base with the image of the food
        self.rect = self.images.get_rect() #This delimited the position and the size of the image
        self.rect.left, self.rect.bottom = random.randint(20, screen_size[0] - 20), -10
        self.speed = random.randrange(5, 10) #This represent the vertical speed for the food
        self.score = 1 if selected_key == "gold" else 5 #This is the score associated with the food of the game like 1 for gold and 5 for others
    
    def update(self):
        #This update the position of the food in any frame
        self.rect.bottom += self.speed
        
        #This detects if the food get out of the bottom of the screen
        if self.rect.top > self.screen_size[1]:
            return True
        return False