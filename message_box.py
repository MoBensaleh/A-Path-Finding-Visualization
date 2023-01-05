import pygame

BLACK = (0, 0, 0)

def show_dialog(screen, message):
    """
    Display a dialog box with a message, a "Restart" button, and a "Quit" button.
    Return "restart" if the user clicks "Restart" or "quit" if the user clicks "Quit".
    """
    # Set up the dialog box dimensions and position
    dialog_width = 300
    dialog_height = 200
    dialog_x = (screen.get_width() - dialog_width) // 2
    dialog_y = (screen.get_height() - dialog_height) // 2

    # Create a dialog box surface and fill it with a white color
    dialog_surface = pygame.Surface((dialog_width, dialog_height))
    dialog_surface.fill((255, 255, 255))

    # Create a rectangular outline around the dialog box
    pygame.draw.rect(dialog_surface, (0, 0, 0), (0, 0, dialog_width, dialog_height), 1)

    # Create the text surface and rectangle for the message
    font = pygame.font.Font(None, 36)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (dialog_width // 2, dialog_height // 2 - 50)

    # Create the "Restart" button surface and rectangle
    restart_surface = font.render("Restart", True, (0, 0, 0))
    restart_rect = restart_surface.get_rect()
    restart_rect.center = (dialog_width // 2 - 75, dialog_height // 2 + 50)

    # Create the "Quit" button surface and rectangle
    quit_surface = font.render("Quit", True, (0, 0, 0))
    quit_rect = quit_surface.get_rect()
    quit_rect.center = (dialog_width // 2 + 75, dialog_height // 2 + 50)

    # Blit the text and button surfaces onto the dialog box surface
    dialog_surface.blit(text_surface, text_rect)
    dialog_surface.blit(restart_surface, restart_rect)
    dialog_surface.blit(quit_surface, quit_rect)

    # Blit the dialog box surface onto the screen
    screen.blit(dialog_surface, (dialog_x, dialog_y))
    pygame.display.flip()
    # Run a loop to handle user interaction with the dialog box
    running = True
    while running:
        for event in pygame.event.get():
       
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Convert mouse coordinates to dialog box coordinates
                mouse_x_in_dialog = mouse_x - dialog_x
                mouse_y_in_dialog = mouse_y - dialog_y
                if restart_rect.collidepoint(mouse_x_in_dialog, mouse_y_in_dialog):
                    # Create a surface with the same dimensions and color as the background
                    bg_surface = pygame.Surface((screen.get_width(), screen.get_height()))
                    bg_surface.fill(BLACK)

                    # Blit the background surface over the dialog box
                    screen.blit(bg_surface, (0, 0))
                    pygame.display.update()
                    return "restart"
                elif quit_rect.collidepoint(mouse_x_in_dialog , mouse_y_in_dialog):
                    return "quit"