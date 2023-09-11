import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def get_number_rows(ai_settings, ship_height, alien_height):
    # calculate how many aliens can be draw in the screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    # calculate how many aliens can be draw in one row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # set an alien and add it into the current row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """set a fleet of aliens"""
    # set an alien and calculate how many aliens can be draw in one row
    # the space between aliens equal to the width of an alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # set a group of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
        
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to press the key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

        
def fire_bullet(ai_settings, screen, ship, bullets):
    """if the rest bullets in screen are lower than allowed , then shoot one bullet"""
    # set a bullet, and add it into group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
     """respond to release the key"""
     if event.key == pygame.K_RIGHT:
        ship.moving_right = False
     elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """respond to keyborad and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)    
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update the location of bullets, and delete disappeared bullets"""
    # update the location of bullets
    bullets.update()
    
    #delete disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """respond to the collisions of bullets and aliens"""
    # check whether bullets shot the aliens, if so, delete both of them
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
    # delete the rest bullets and set a new group of aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

            
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the image on screen and shift to new screen"""
    # redraw the screen in everyloops
    screen.fill(ai_settings.bg_color)

    # redraw all of bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()    

    ship.blitme()
    aliens.draw(screen)

    # make the screen mode to be seen
    pygame.display.flip()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to the ship hit by the ship"""
    if stats.ships_left > 0:
        # minus one from ship_left
        stats.ships_left -= 1

        # clear the group of alien and bullet
        aliens.empty()
        bullets.empty()

        # set a new group of alien, and put ship in the middle position at the bottom of screent
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check whether any aliens move to the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # dispose the case like ship hit by aliens
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    """measures respond to aliens move to the edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """move all the aliens down and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1    


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """check if aliens move to the edges and update all aliens location"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # check whether any aliens move to the bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
    # check the collisions of aliens and the ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
