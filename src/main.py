import pygame
import button
import chessMain

pygame.init()

# create game window
SCREEN_WIDTH = 901
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")
logo = pygame.image.load('../assets/images/chess _logo.png')
pygame.display.set_icon(logo)
background = pygame.image.load('../assets/images/background.jpg')


# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (0, 0, 0)

# load button images
# resume_img = pygame.image.load("../assets/images/button_resume.png").convert_alpha()
# options_img = pygame.image.load("../assets/images/button_options.png").convert_alpha()
# quit_img = pygame.image.load("../assets/images/button_quit.png").convert_alpha()
# video_img = pygame.image.load('../assets/images/button_video.png').convert_alpha()
# audio_img = pygame.image.load('../assets/images/button_audio.png').convert_alpha()
# keys_img = pygame.image.load('../assets/images/button_keys.png').convert_alpha()
# back_img = pygame.image.load('../assets/images/button_back.png').convert_alpha()
playwithcomputer_img = pygame.image.load('../assets/images/button_play-with-computer.png').convert_alpha()
playwithfriend_img = pygame.image.load('../assets/images/button_play-with-friend.png').convert_alpha()

# create button instances
# resume_button = button.Button(304, 125, resume_img, 1)
# options_button = button.Button(297, 250, options_img, 1)
# quit_button = button.Button(336, 375, quit_img, 1)
# video_button = button.Button(226, 75, video_img, 1)
# audio_button = button.Button(225, 200, audio_img, 1)
# keys_button = button.Button(246, 325, keys_img, 1)
# back_button = button.Button(332, 450, back_img, 1)
playwithcomputer_button = button.Button(270, 365, playwithcomputer_img, 1)
playwithfriend_button = button.Button(270, 455, playwithfriend_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def main():
    # game variables
    game_paused = True
    menu_state = "main"
    # game loop
    run = True
    while run:
        # screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        # check if game is paused
        if game_paused == True:
            # check menu state
            draw_text('CHOOSE OPTION', font, TEXT_COL, 265, 70)
            if menu_state == "main":
                '''
                # draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
                if quit_button.draw(screen):
                    run = False
                '''
                if playwithcomputer_button.draw(screen):
                    menu_state = "play with computer"
                if playwithfriend_button.draw(screen):
                    menu_state = "play with friend"

            if menu_state == "play with computer":
                if __name__ == '__main__':
                    chessMain.playwithcomputer = True
                    chessMain.main()
                menu_state = "main"

            if menu_state == "play with friend":
                if __name__ == '__main__':
                    chessMain.playwithcomputer = False
                    chessMain.main()
                menu_state = "main"
            '''
            # check if the options menu is open
            if menu_state == "options":
                # draw the different options buttons
                if video_button.draw(screen):
                    print("Video Settings")
                if audio_button.draw(screen):
                    print("Audio Settings")
                if keys_button.draw(screen):
                    print("Change Key Bindings")
                if back_button.draw(screen):
                    menu_state = "main"
            '''
            '''
            if menu_state == "play with computer":
                print("play with computer")
                menu_state = "main"
            if menu_state == "play with friend":
                print("play with friend")
                menu_state = "main"
            '''
        else:
            draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
