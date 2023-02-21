import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    """ Обработка событий """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            # Движение вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # Движение влево
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, bullets):
    """ Обновление экрана """
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    """ Обновление позиции пулек"""
    bullets.update()

    # удаление пулек за пределами экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # вывод длины контеннера с пульками и их мгновенное удаление
    # print(len(bullets))

