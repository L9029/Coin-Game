import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, images, position=[375, 520], **kwargs):
        pygame.sprite.Sprite.__init__(self)
        
        #This are the position of the images for the hero in the list from the images path
        self.images_right = images[:5]
        self.images_left = images[5:]
        self.images = self.images_right.copy()
        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image) #This create the collision mask for the hero
        self.rect = self.image.get_rect() #Create the rectangular for the hero
        
        #This will refer to the coordinates of the initialization of our hero that is initially located
        self.rect.left, self.rect.top = position
        
        self.direction = "right"
        self.speed = 8
        self.switch_frame_count = 0
        self.switch_frame_frep = 1
        self.frame_index = 0
        
    
    def move(self, screen_size, direction):
        assert direction in ["left", "right"]
        
        if direction != self.direction:
            self.images = self.images_left.copy() if direction == "left" else self.images_right.copy()
            self.image = self.images[0]
            self.direction = direction
            self.switch_frame_count = 0
        
        self.switch_frame_count += 1
        
        if self.switch_frame_count % self.switch_frame_frep == 0:
            self.switch_frame_count = 0
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.image = self.images[self.frame_index]
        
        if direction == "left":
            self.rect.left = max(self.rect.left - self.speed, 0)
        else:
            self.rect.left = min(self.rect.left + self.speed, screen_size[0])
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
