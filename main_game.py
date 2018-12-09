# 3rd party imports
import libtcodpy as tcod

# Game files
import constants

# Set FPS
tcod.sys_set_fps(constants.LIMIT_FPS)


def handle_keys():
    key = tcod.console_wait_for_keypress(True)

    global player_x, player_y

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    elif key.vk == tcod.KEY_ESCAPE:
        return True  # exit game

    # movement keys
    elif tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y = player_y - 1

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y = player_y + 1

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x = player_x + 1


# Setting the font
tcod.console_set_custom_font(constants.font_path, constants.font_flags)

# Initializing the screen
window_title = 'Project Rogue-Like'
full_screen = False
tcod.console_init_root(constants.GAME_WIDTH, constants.GAME_HEIGHT, window_title, full_screen)

# Initializing the player
player_x = constants.GAME_WIDTH // 2
player_y = constants.GAME_HEIGHT // 2

# Main loop
while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)

    tcod.console_flush()
    tcod.console_put_char(0, player_x, player_y, ' ', tcod.BKGND_NONE)

    # handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
