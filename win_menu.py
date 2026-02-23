import pygame
import random
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ZOMBIE SURVIVAL")


BLACK, BLOOD_RED = (0, 0, 0), (255, 40, 0)
CRT_GREEN, CRT_GLOW = (20, 255, 20), (100, 255, 100)


font_big = pygame.font.SysFont("courier", 72, bold=True)
font_small = pygame.font.SysFont("courier", 36, bold=True)


def show_win_screen(round_num, kills, score, countdown=3):
   clock = pygame.time.Clock()
   background = screen.copy()  # snapshot current screen
   splatters = [(random.randint(0, 800), random.randint(0, 600)) for _ in range(15)]
   start_ticks = pygame.time.get_ticks()


   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               return


       elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
       remaining = countdown - elapsed


       if remaining < 0:
           return


       pulse = 0.8 + 0.2 * abs(pygame.math.Vector2(1, 1).rotate(pygame.time.get_ticks() / 50).x)


       screen.blit(background, (0, 0))  # restore game screen snapshot


       for x, y in splatters:
           pygame.draw.circle(screen, BLOOD_RED, (x, y), random.randint(5, 15))


       pygame.draw.rect(screen, (0, 20, 0), (50, 50, 700, 500), 2)


       text = pygame.transform.scale_by(font_big.render("ROUND CLEARED!", True, CRT_GREEN), pulse)
       screen.blit(text, (400 - text.get_width() // 2, 100))


       stats = [
           f"ROUND: {round_num}",
           f"ZOMBIES KILLED: {kills}",
           f"SCORE: {score}",
           "",
           f"NEXT ROUND IN: {remaining}"
       ]
       for i, text in enumerate(stats):
           color = CRT_GLOW if i >= 3 else CRT_GREEN
           rendered = font_small.render(text, True, color)
           screen.blit(rendered, (400 - rendered.get_width() // 2, 220 + i * 40))


       for y in range(0, 600, 3):
           pygame.draw.line(screen, (0, 10, 0), (0, y), (800, y), 1)


       pygame.display.flip()
       clock.tick(60)


#  Test Setup
if __name__ == "__main__":
   # Simulate a game scene
   screen.fill((10, 10, 10))  # dark gray background
   for _ in range(100):
       pygame.draw.circle(screen, (50, 255, 50),
                          (random.randint(0, 800), random.randint(0, 600)),
                          random.randint(2, 4))
   pygame.display.flip()  # render before taking snapshot


   show_win_screen(4, 76, 9350)
   pygame.quit()

