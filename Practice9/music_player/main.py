import pygame
from player import MusicPlayer

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Music Player")

    player = MusicPlayer("music")

    font = pygame.font.SysFont("Arial", 24)

    running = True

    while running:
        screen.fill((30, 30, 30))

        
        track_text = font.render(
            f"Track: {player.get_current_track()}",
            True,
            (255, 255, 255)
        )
        screen.blit(track_text, (20, 50))

        info_text = font.render(
            "P=Play S=Stop N=Next B=Back Q=Quit",
            True,
            (180, 180, 180)
        )
        screen.blit(info_text, (20, 120))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()

                elif event.key == pygame.K_s:
                    player.stop()

                elif event.key == pygame.K_n:
                    player.next_track()

                elif event.key == pygame.K_b:
                    player.previous_track()

                elif event.key == pygame.K_q:
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()