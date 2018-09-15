import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from alien import A_1
from alien import A_2
from game_state import GameState
from time import sleep
from button import Button
from scoreboard import Scoreboard


def keyd(event, screen, ship, a_s, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_front = True
    elif event.key == pygame.K_DOWN:
        ship.moving_back = True
    elif event.key == pygame.K_q:
        print("Quit Game!")
        print("Thank you for playing")
        exit()

    if event.key == pygame.K_SPACE:
        if len(bullets) < a_s.bullets_count:
            new_bullet = Bullet(a_s, screen, ship)
            bullets.add(new_bullet)


def keyu(event, screen, ship, a_s, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_front = False
    elif event.key == pygame.K_DOWN:
        ship.moving_back = False


def Exit():
    sys.exit()


# 关卡1 -> 矩阵
def create_aliens1(a_s, screen, aliens, ship):
    image = pygame.image.load('images/1.bmp')
    alien = Alien(a_s, screen, image)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.height
    a_V_X = a_s.screen_width - 2 * alien_width
    n_A_X = a_V_X / (2 * alien_width)
    a_s_y = a_s.screen_height - 3 * alien_height - ship_height
    n_A_Y = a_s_y / (2 * alien_height)
    for a_n_y in range(int(n_A_Y)):
        for a_n in range(int(n_A_X)):
            alien = Alien(a_s, screen, image)
            alien.x = alien_width + 2 * alien_width * a_n
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * a_n_y
            aliens.add(alien)


# 关卡2 -> 三角
def create_aliens2(a_s, screen, aliens, ship):
    alien = A_1(a_s, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.height
    a_V_X = a_s.screen_width - 2 * alien_width
    n_A_X = a_V_X / (2 * alien_width)
    a_s_y = a_s.screen_height - 3 * alien_height - ship_height
    n_A_Y = a_s_y / (2 * alien_height)
    for a_n_y in range(int(n_A_Y)):
        for a_n in range(int(n_A_X)):
            alien = A_1(a_s, screen)
            alien.x = alien_width + 2 * alien_width * a_n
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * a_n_y
            aliens.add(alien)
        n_A_X = n_A_X - n_A_X / 4


# 关卡3 -> 箭头
def create_aliens3(a_s, screen, aliens, ship):
    alien = A_2(a_s, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.height
    a_V_X = a_s.screen_width - 2 * alien_width
    n_A_X = a_V_X / (2 * alien_width)
    a_s_y = a_s.screen_height - 3 * alien_height - ship_height
    n_A_Y = a_s_y / (2 * alien_height)
    for a_n_y in range(int(n_A_Y * 1/3)):
        for a_n in range(int(n_A_X * 1/4), int(n_A_X * 3/4), 1):
            alien = A_2(a_s, screen)
            alien.x = alien_width + 2 * alien_width * a_n
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * a_n_y
            aliens.add(alien)

    ll = 1/100
    rr = 99/100
    for a_n_y in range(int(n_A_Y * 1/3), int(n_A_Y), 1):
        for a_n in range(int(n_A_X * ll), int(n_A_X * rr), 1):
            alien = A_2(a_s, screen)
            alien.x = alien_width + 2 * alien_width * a_n
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * a_n_y
            aliens.add(alien)
        ll = ll + 0.1
        rr = rr - 0.1


def check_f_e(a_s, aliens):
    flag = False
    for alien in aliens:
        if alien.check_edges() == True:
            for alien in aliens.sprites():
                alien.rect.y += a_s.alien_drop
            a_s.f_d *= -1
            flag = True

        if flag:
            break


def check_b_a_c(a_s, screen, ship, aliens, bullets, flag, state, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for c in collisions.values():
            state.score += a_s.a_score * len(c)
            sb.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        a_s.all_init()
        print(str(flag))
        if flag == 1:
            a_s.a_d_up()
            a_s.a_d_up()
            create_aliens2(a_s, screen, aliens, ship)
        elif flag == 2:
            a_s.b_c_up()
            create_aliens3(a_s, screen, aliens, ship)
        else:
            create_aliens1(a_s, screen, aliens, ship)
        flag = flag + 1
    if flag == 4:
        flag = 1
    return flag


def ship_hit(screen, ship, a_s, bullets, aliens, state):
    state.ships_left -= 1
    bullets.empty()
    a_s.ship_init()
    ship.center_ship()


def check_aliens_bottom(screen, ship, a_s, bullets, aliens, state):
    screen_rect = screen.get_rect()
    flag = False
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            flag = True
            break
    return flag


def a_update(event, screen, ship, a_s, bullets, aliens, state, play_button, flag, sb):
    r_flag = flag

    if state.game_active:
        ship.update()
        bullets.update()
        ship.blitme()

        for bullet in bullets.sprites():
            bullet.draw_bullet()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        r_flag = check_b_a_c(a_s, screen, ship, aliens, bullets, flag, state, sb)
        check_f_e(a_s, aliens)
        aliens.update()
        aliens.draw(screen)
        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(screen, ship, a_s, bullets, aliens, state)
            if state.ships_left == 0:
                print("Ship hit!!!!!")
                print("GAME OVER!!!!")
                sleep(0.5)
                state.game_active = False
                pygame.mouse.set_visible(True)

        elif check_aliens_bottom(screen, ship, a_s, bullets, aliens, state):
            print("Aliens hit You Home!!!!!")
            print("GAME OVER!!!!")
            sleep(0.5)
            state.game_active = False
            pygame.mouse.set_visible(True)
        sb.show()
    else:
        play_button.draw()

    return r_flag


def run_game():
    pygame.init()
    a_s = Settings()
    screen = pygame.display.set_mode((a_s.screen_width, a_s.screen_height))
    pygame.display.set_caption("JB-1428大乱斗")
    ship = Ship(a_s, screen)
    aliens = Group()
    flag = 1
    create_aliens1(a_s, screen, aliens, ship)
    bullets = Group()
    state = GameState(a_s)
    play_button = Button(a_s, screen, "Play")
    sb = Scoreboard(a_s, screen, state)
    posx = 0
    posy = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit()
            elif event.type == pygame.KEYDOWN:
                keyd(event, screen, ship, a_s, bullets)
            elif event.type == pygame.KEYUP:
                keyu(event, screen, ship, a_s, bullets)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                posx = x
                posy = y
                if play_button.rect.collidepoint(x, y):
                    state.game_active = True

        screen.fill(a_s.bg_color)
        if not state.game_active and play_button.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            state.reset_state()
            play_button.draw()
            aliens.empty()
            bullets.empty()
            create_aliens1(a_s, screen, aliens, ship)
            ship.center_ship()

        flag = a_update(event, screen, ship, a_s, bullets, aliens, state, play_button, flag, sb)
        pygame.display.flip()


run_game()
