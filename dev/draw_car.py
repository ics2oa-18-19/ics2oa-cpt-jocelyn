import arcade


WIDTH = 640
HEIGHT = 480

player_x = WIDTH / 2 - 40/2
player_y = 50

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
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_xywh_rectangle_filled(player_x, player_y, 40, 40, arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(player_x, player_y - 10, 10, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(player_x + 30, player_y - 10, 10, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(player_x + 5, player_y + 20, 30, 15, arcade.color.PALE_ROBIN_EGG_BLUE)
    arcade.draw_xywh_rectangle_filled(player_x, player_y + 5, 10, 5, arcade.color.GOLD)
    arcade.draw_xywh_rectangle_filled(player_x + 30, player_y + 5, 10, 5, arcade.color.GOLD)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
