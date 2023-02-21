import pygame, sys
from bullet import Bullet
from ino import Ino
import time

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

def update(bg_color, screen, stats, sc, gun, inos, bullets):
    """ Обновление экрана """
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    """ Обновление позиции пулек"""
    bullets.update()

    # удаление пулек за пределами экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    """ метод groupcollide - сравниваниет прямоугольник rect каждой пули
     с атрибутом rect каждого пришельца
     если один попадает на другой(между ними есть коллизия)
     в итоге образуется словарь, в котором ключ это пуля а значение 
     это пришелец """
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    
    if collisions:
        # проверка на прибавление очков равноценно как если бы
        # уничтожалось несколько обьектов за один выстрел
        # for inos in collisions.values():
        #     stats.score += 10 * len(inos)
        stats.score += 10
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()

    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


    
    # вывод длины контеннера с пульками и их мгновенное удаление
    # print(len(bullets))


def gun_kill(stats, screen, sc, gun, inos, bullets):
    """ Столкновение пушки и прищельцев """
    if stats.guns_left > 0:
        # создаем новую армию, пули
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    """ Обновление позиции пришельцев """
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    """ Проверка, добрались ли пришельцы до края экрана """
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos):
    """ Создание армии пришельцев """
    ino = Ino(screen)
    ino_width = ino.rect.width
    
    # расчет пришельцев в одном ряду
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    # преобразование в целое т.к в ряду не может быть дробного

    # расчет рядов
    ino_height = ino.rect.height
    number_ino_y = int((600 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        # заполнение рядов пришельцами
        for ino_number in range(number_ino_x):
            # заполнение ряда пришельцами
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            # добавление в группу
            inos.add(ino)


def check_high_score(stats, sc):
    """ Проверка новых рекордов """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as file:
            file.write(str(stats.high_score))