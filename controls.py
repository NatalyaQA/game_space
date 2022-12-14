import pygame
import sys
from bullet import Bullet
from ino import Ino
import time
from gun import Gun


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():  # отслеживать действия
        if event.type == pygame.QUIT:  # если нажал на крестик - выход
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:   # вправо
                gun.mright = True    # изначально движение на 1 - gun.rect.centerx += 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))  # проверка значений количества пуль на экране
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        if (stats.score % 500 == 0) and (stats.score // 200 != 0):
            ino.boost *= 1.1

        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    """столкновение пушки и  армиии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        print("END")
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    """обновляет позицию инопришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    """проверка, добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()  # получить экран
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((680 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
