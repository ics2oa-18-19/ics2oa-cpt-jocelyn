import arcade


WIDTH = 500
HEIGHT = 650

health = 50


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
    arcade.draw_xywh_rectangle_filled(275,600,200,35,arcade.color.GOLDEN_POPPY)
    arcade.draw_xywh_rectangle_filled(285,605,180,25,arcade.color.GOLDEN_BROWN)
    arcade.draw_xywh_rectangle_filled(285,605,180*health/100,25,arcade.color.RED)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
