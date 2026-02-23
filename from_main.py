  # Coin controller
        for coin in coins:
            coin.draw(screen)
            if coin.rect.colliderect(player.rect):
                player.coin_sound.play()
                coins.remove(coin)
                player.pickup_coin()
        
        if not player.alive:
            for frame in range(int(frames_since_death / 4)):
                screen.blit(shade_surf_lite_lite, (0, 0))
            player.draw(screen, character_facing)

        if debug_menu:
            debug() # Show debug utils
        else:
            debug_button = font.render(f"Press TAB to open debug menu", True, (255, 255, 255))
            screen.blit(debug_button, (10, 10))
