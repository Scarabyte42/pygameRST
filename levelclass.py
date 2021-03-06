import pygame
import rgbColours
import enemyclass

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.hitmarker_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.hitmarker_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # screen.fill(rgbColours.BLUE)
        background = pygame.image.load('images/Test-Background.png')
        screen.blit(background, (self.world_shift, 0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.hitmarker_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for marker in self.hitmarker_list:
            marker.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x