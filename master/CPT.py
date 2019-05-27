import arcade


WIDTH = 640
HEIGHT = 480

player_x = 320
player_y = 100

left_key = False
right_key = False

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global left_key, right_key, player_x

    if left_key == True:
        player_x -= 7
    elif right_key == True:
        player_x += 7

    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH:
        player_x = WIDTH


def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y

    arcade.draw_circle_filled(player_x, player_y, 30, arcade.color.BLUE)


def on_key_press(key, modifiers):
    global left_key, right_key

    if key == arcade.key.LEFT:
        left_key = True
    elif key == arcade.key.RIGHT:
        right_key = True



def on_key_release(key, modifiers):
    global left_key, right_key

    if key == arcade.key.LEFT:
        left_key = False
    elif key == arcade.key.RIGHT:
        right_key = False


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
