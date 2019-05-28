import arcade


WIDTH = 500
HEIGHT = 650

player_x = WIDTH / 2
player_y = 50

left_key = False
right_key = False
up_key = False
down_key = False

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
    global left_key, right_key, player_x, player_y

    speed = 8
    if left_key == True:
        player_x -= speed
    elif right_key == True:
        player_x += speed
    elif up_key == True:
        player_y += speed
    elif down_key == True:
        player_y -= speed

    if player_x < 25:
        player_x = 25
    elif player_x > WIDTH - 25:
        player_x = WIDTH - 25
    elif player_y < 25:
        player_y = 25
    elif player_y > 100:
        player_y = 100


def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y

    arcade.draw_rectangle_filled(player_x, player_y, 45,45, arcade.color.BLUE)
    arcade.draw_line(400, HEIGHT,WIDTH,120,arcade.color.NAVY_BLUE)
    arcade.draw_line(100, HEIGHT,0,120,arcade.color.NAVY_BLUE)


def on_key_press(key, modifiers):
    global left_key, right_key, up_key, down_key

    if key == arcade.key.LEFT:
        left_key = True
    elif key == arcade.key.RIGHT:
        right_key = True
    elif key == arcade.key.UP:
        up_key = True
    elif key == arcade.key.DOWN:
        down_key = True



def on_key_release(key, modifiers):
    global left_key, right_key, up_key, down_key

    if key == arcade.key.LEFT:
        left_key = False
    elif key == arcade.key.RIGHT:
        right_key = False
    elif key == arcade.key.UP:
        up_key = False
    elif key == arcade.key.DOWN:
        down_key = False


def on_mouse_press(x, y, button, modifiers):
    pass



if __name__ == '__main__':
    setup()
