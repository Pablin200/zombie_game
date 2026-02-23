game_state = "intermission"
running = True


# Define upgrades
lvl_move_speed = 1 # Changes player.speed
lvl_fire_rate = 1 # Changes player.fire_rate
lvl_reload_speed = 1 # Changes player.reload_speed
lvl_bullet_speed = 1 # Changes bullet.speed
lvl_ammo_capacity = 1 # Changes player.max_ammo
# Cost per upgrade
cost_move_speed = 12
cost_fire_rate = 8
cost_reload_speed = 6
cost_bullet_speed = 4
cost_ammo_capacity = 7


# Upgrade stats and refresh upgrade prices
def register_upgrade(upgrade):
   match upgrade:
       case "move_speed":
           global lvl_move_speed
           lvl_move_speed += 1
           if lvl_move_speed == 2:
               player.speed = 2.9
               global cost_move_speed
               cost_move_speed = 24
           if lvl_move_speed == 3:
               player.speed = 3
               lvl_move_speed = "MAX"


       case "fire_rate":
           global lvl_fire_rate
           lvl_fire_rate += 1
           global cost_fire_rate
           cost_fire_rate += 4
           player.fire_rate -= 0.1
           if lvl_fire_rate == 7:
               lvl_move_speed = "MAX"


       case "reload_speed":
           global lvl_reload_speed
           lvl_reload_speed += 1
           global cost_reload_speed
           cost_reload_speed += 3
           player.reload_speed -= 0.1
           if lvl_reload_speed == 7:
               lvl_reload_speed = "MAX"


       case "bullet_speed":
           global lvl_bullet_velocity
           lvl_bullet_velocity += 1
           global cost_bullet_speed
           cost_bullet_speed += 2
           bullet.speed += 2
           if lvl_bullet_velocity == 5:
               lvl_bullet_velocity = "MAX"


       case "mag_size":
           global lvl_ammo_capacity
           lvl_ammo_capacity += 1
           global cost_ammo_capacity
           cost_ammo_capacity += 3
           player.max_ammo += 1
           if lvl_ammo_capacity == 12:
               lvl_ammo_capacity = "MAX"




while running:
   #------------INTERMISSION MENU------------
   # Displays the next round number, your current amount of coins, stat levels and upgrade costs
   # Features a button upgrade stats with coins, and a button to procede to next round
   elif game_state == "intermission":


       # Initialize game state variables | GAME STATE ALWAYS STARTS AT FRAME 0
       if frame == 0:
           screen.fill((10, 10, 10))  # Dark gray background


           # Draw circles on screen
           for _ in range(100):
               pygame.draw.circle(screen, (50, 255, 50),(random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT)), random.randint(2, 4))


           background = screen.copy()  # snapshot current screen


           splatters = [(random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT)) for _ in range(15)]
           pulse = 0.8 + 0.2 * abs(pygame.math.Vector2(1, 1).rotate(pygame.time.get_ticks() / 50).x)


           # NEXT WAVE BUTTON VARIABLES
           next_wave_button_text = font_small.render("PROCEED TO NEXT WAVE", True, config.CRT_GLOW)
           next_wave_button_rect = next_wave_button_text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + 100))
           # Add a background rectangle for the button
           next_wave_button_bg = pygame.Rect(next_wave_button_rect.left - 20, next_wave_button_rect.top - 10,
                                             next_wave_button_rect.width + 40, next_wave_button_rect.height + 20)


           # --------UPGRADE-MENU-VARIABLES-HERE--------
           upgrade_options = [
               {"label": "Fire Rate", "level": lvl_fire_rate, "cost": cost_fire_rate, "key": "fire_rate"},
               {"label": "Reload Speed", "level": lvl_reload_speed, "cost": cost_reload_speed, "key": "reload_speed"},
               {"label": "Mag Size", "level": lvl_ammo_capacity, "cost": cost_ammo_capacity, "key": "mag_size"},
               {"label": "Move Speed", "level": lvl_move_speed, "cost": cost_move_speed, "key": "move_speed"},
               {"label": "Bullet Speed", "level": lvl_bullet_speed, "cost": cost_bullet_speed, "key": "bullet_speed"},
           ]


           upgrade_buttons = []
           button_width = 180
           button_height = 80
           spacing = 10
           start_x = (config.WIDTH - (button_width + spacing) * 3 + spacing) // 2
           start_y = config.HEIGHT // 2 - 80


           selected_upgrade = None




           # --------UPGRADE-MENU-VARIABLES-HERE--------


       # Event checks
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()


       screen.blit(background, (0, 0))  # restore game screen snapshot


       for x, y in splatters:
           pygame.draw.circle(screen, config.BLOOD_RED, (x, y), random.randint(5, 15))


       screen.blit(shade_surf, (0, 0))


       text = pygame.transform.scale_by(font_big.render("ROUND CLEARED!", True, config.CRT_GREEN), pulse)
       screen.blit(text, (config.WIDTH // 2 - text.get_width() // 2, 100))


       # --------UPGRADE-MENU-CODE-HERE--------
   coins_text = font_small.render(f"Coins: {player.coins}", True, config.CRT_GREEN)
   coins_rect = coins_text.get_rect(center=(config.WIDTH // 2, 150))
   screen.blit(coins_text, coins_rect)


   # Draw upgrade buttons
   upgrade_buttons = []
   for i, upgrade in enumerate(upgrade_options):
       row = i // 3
       col = i % 3
       x = start_x + col * (button_width + spacing)
       y = start_y + row * (button_height + spacing)


       rect = pygame.Rect(x, y, button_width, button_height)
       upgrade_buttons.append((rect, upgrade["key"]))


       pygame.draw.rect(screen, config.CRT_GREEN if selected_upgrade == upgrade["key"] else (0, 100, 0), rect, 2,
                        border_radius=5)


       label = font_small.render(f"{upgrade['label']}", True, config.CRT_GREEN)
       level = font_small.render(f"Lvl. {upgrade['level']}", True, config.CRT_GREEN)
       cost = font_small.render(f"{upgrade['cost']} coins", True, config.CRT_GREEN)


       screen.blit(label, (x + 10, y + 10))
       screen.blit(level, (x + 10, y + 35))
       screen.blit(cost, (x + 10, y + 60))


   # Confirm upgrade button
   confirm_rect = pygame.Rect(start_x + 2 * (button_width + spacing), start_y + (button_height + spacing), button_width,
                              button_height)
   pygame.draw.rect(screen, config.CRT_GREEN, confirm_rect, 2, border_radius=5)
   confirm_text = font_small.render("Confirm\nUpgrade", True, config.CRT_GREEN)
   screen.blit(confirm_text, (confirm_rect.x + 10, confirm_rect.y + 20))


   # Handle mouse events
   if pygame.mouse.get_pressed()[0]:
       mouse_pos = pygame.mouse.get_pos()


       for rect, key in upgrade_buttons:
           if rect.collidepoint(mouse_pos):
               selected_upgrade = key


       if confirm_rect.collidepoint(mouse_pos) and selected_upgrade:
           upgrade_costs = {
               "fire_rate": cost_fire_rate,
               "reload_speed": cost_reload_speed,
               "mag_size": cost_ammo_capacity,
               "move_speed": cost_move_speed,
               "bullet_speed": cost_bullet_speed,
           }
           if player.coins >= upgrade_costs[selected_upgrade]:
               player.coins -= upgrade_costs[selected_upgrade]
               register_upgrade(selected_upgrade)
               selected_upgrade = None  # reset after upgrade




       # register_upgrade("") # "move_speed", "fire_rate", "reload_speed", "bullet_speed", "mag_size"
       # --------UPGRADE-MENU-CODE-HERE--------


       # NEXT WAVE BUTTON START
       # Check if mouse is hovering over the button
       mouse_pos = pygame.mouse.get_pos()
       mouse_hovering_next_wave = next_wave_button_bg.collidepoint(mouse_pos)
       # Hover effect
       if mouse_hovering_next_wave:
           pygame.draw.rect(screen, config.CRT_GREEN, next_wave_button_bg, border_radius=5)
           next_wave_button_text = font_small.render("PROCEED TO NEXT WAVE", True,
                                                     (0, 0, 0))  # Black text when hovering
       else:
           pygame.draw.rect(screen, (0, 50, 0), next_wave_button_bg, border_radius=5)


       screen.blit(next_wave_button_text, next_wave_button_rect)# Draw the button text


       if mouse_hovering_next_wave and pygame.mouse.get_pressed()[0]:  # Check for click
           game_state = "game"
           wave.start_wave()
           bullet_count = 0
           player.ammo = player.max_ammo
       # NEXT WAVE BUTTON END


       for y in range(0, config.HEIGHT, 3):
           pygame.draw.line(screen, (0, 10, 0), (0, y), (config.HEIGHT, y), 1)


       # Refresh display
       pygame.display.flip()
       clock.tick(config.FPS)
   #------------INTERMISSION MENU------------
