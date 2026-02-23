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




def show_lose_screen(round_num, kills, score):
   clock = pygame.time.Clock()
   splatters = [(random.randint(0, 800), random.randint(0, 600)) for _ in range(15)]


   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               pygame.quit()
               sys.exit()


       pulse = 0.8 + 0.2 * abs(pygame.math.Vector2(1, 1).rotate(pygame.time.get_ticks() / 50).x)


       screen.fill(BLACK)


       for x, y in splatters:
           pygame.draw.circle(screen, BLOOD_RED, (x, y), random.randint(5, 15))


       pygame.draw.rect(screen, (0, 20, 0), (50, 50, 700, 500), 2)


       text = pygame.transform.scale_by(font_big.render("GAME OVER", True, CRT_GREEN), pulse)
       screen.blit(text, (400 - text.get_width() // 2, 100))


       stats = [
           f"ROUND REACHED: {round_num}",
           f"ZOMBIES KILLED: {kills}",
           f"FINAL SCORE: {score}",
           "",
           "PRESS ESC TO QUIT"
       ]
       for i, text in enumerate(stats):
           color = CRT_GLOW if i >= 3 else CRT_GREEN
           rendered = font_small.render(text, True, color)
           screen.blit(rendered, (400 - rendered.get_width() // 2, 220 + i * 40))


       for y in range(0, 600, 3):
           pygame.draw.line(screen, (0, 10, 0), (0, y), (800, y), 1)


       pygame.display.flip()
       clock.tick(60)


# Test run
if __name__ == "__main__":
   # Fake background
   screen.fill(BLACK)
   for _ in range(100):
       pygame.draw.circle(screen, BLOOD_RED,
                          (random.randint(0, 800), random.randint(0, 600)),
                          random.randint(2, 5))


   show_lose_screen(5, 87, 12500)

