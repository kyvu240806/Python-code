import pygame
import sys
import random
import os

pygame.init()
pygame.mixer.init()

# ================== SCREEN ==================
WIDTH, HEIGHT = 1100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# ================== SOUND ==================
jump_sound = pygame.mixer.Sound("sound/jump.mp3")
lose_sound = pygame.mixer.Sound("sound/lose.mp3")
pass_sound = pygame.mixer.Sound("sound/pass.mp3")

pygame.mixer.music.load("sound/bgm.mp3")
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)

# ================== SCORE FILE ==================
SCORE_FILE = "score.log"
best_score = 0
if os.path.exists(SCORE_FILE):
    try:
        with open(SCORE_FILE, "r") as f:
            best_score = int(f.read())
    except:
        best_score = 0

# ================== BACKGROUND ==================
background = pygame.image.load("img/mixibackground.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ================== BIRD ==================
bird_img = pygame.image.load("img/mixibird.png").convert_alpha()
bird_img = pygame.transform.smoothscale(bird_img, (80, 80))

bird_x = 150
gravity = 0.5
jump_strength = -10

# ================== POLE ==================
pole_img = pygame.image.load("img/mixipole.png").convert_alpha()
pole_img = pygame.transform.scale(pole_img, (150, 400))
pole_top_img = pygame.transform.flip(pole_img, False, True)

pole_gap = 200
pole_speed = 3

# ================== BUTTON ==================
def draw_button(text, x, y, w, h, color, text_color):
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=8)
    label = font.render(text, True, text_color)
    screen.blit(
        label,
        (x + (w - label.get_width()) // 2,
         y + (h - label.get_height()) // 2)
    )

# ================== RESET GAME ==================
def reset_game():
    global bird_y, bird_velocity, pole_x, pole_height, score, passed
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pole_x = WIDTH
    pole_height = random.randint(100, 360)
    score = 0
    passed = False

reset_game()

# ================== GAME LOOP ==================
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength
                jump_sound.play()

    # -------- BIRD PHYSICS --------
    bird_velocity += gravity
    bird_y += bird_velocity

    if bird_y <= 0:
        bird_y = 0
        bird_velocity = 0

    if bird_y + bird_img.get_height() >= HEIGHT:
        bird_y = HEIGHT - bird_img.get_height()
        bird_velocity = 0

    # -------- POLE MOVEMENT --------
    pole_x -= pole_speed
    if pole_x < -pole_img.get_width():
        pole_x = WIDTH
        pole_height = random.randint(100, 360)
        passed = False

    # -------- HITBOX --------
    bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
    bird_rect.inflate_ip(-15, -15)

    top_pole_rect = pole_top_img.get_rect(
        topleft=(pole_x, pole_height - pole_top_img.get_height())
    )
    top_pole_rect.inflate_ip(-5, -5)

    bottom_pole_rect = pole_img.get_rect(
        topleft=(pole_x, pole_height + pole_gap)
    )
    bottom_pole_rect.inflate_ip(-5, -5)

    # -------- SCORE --------
    if not passed and bird_x > pole_x + pole_img.get_width():
        score += 1
        passed = True
        pass_sound.play()

    # -------- DRAW --------
    screen.blit(background, (0, 0))
    screen.blit(pole_top_img, top_pole_rect.topleft)
    screen.blit(pole_img, bottom_pole_rect.topleft)
    screen.blit(bird_img, (bird_x, bird_y))

    screen.blit(font.render(f"Score: {score}", True, (0, 0, 200)), (20, 20))
    screen.blit(font.render(f"Best: {best_score}", True, (200, 0, 200)), (20, 60))

    # -------- COLLISION --------
    if bird_rect.colliderect(top_pole_rect) or bird_rect.colliderect(bottom_pole_rect):
        pygame.mixer.music.stop()
        lose_sound.play()

        if score > best_score:
            best_score = score
            with open(SCORE_FILE, "w") as f:
                f.write(str(best_score))

        game_over = True
        while game_over:
            screen.blit(background, (0, 0))

            screen.blit(
                font.render("GAME OVER", True, (255, 0, 0)),
                (WIDTH // 2 - 120, HEIGHT // 2 - 120)
            )

            play_x, play_y = WIDTH // 2 - 250, HEIGHT // 2 - 20
            end_x, end_y = WIDTH // 2 + 20, HEIGHT // 2 - 20

            draw_button("Play Again", play_x, play_y, 200, 60, (0, 180, 0), (255, 255, 255))
            draw_button("End Game", end_x, end_y, 200, 60, (180, 0, 0), (255, 255, 255))

            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if e.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if play_x < mx < play_x + 200 and play_y < my < play_y + 60:
                        reset_game()
                        pygame.mixer.music.play(-1)
                        game_over = False

                    if end_x < mx < end_x + 200 and end_y < my < end_y + 60:
                        pygame.quit()
                        sys.exit()

    pygame.display.update()
