#now has differnet screens

import arcade
import random

WIDTH = 500
HEIGHT = 650

current_screen = "menu"


#player
player_x = WIDTH / 2 - 40/2
player_y = 50

health = 100

left_key = False
right_key = False
hit = False

#zombie
zombie_x = []
zombie_y = []
zombie_w = 30
zombie_h = 80

num = 15

for i in range(num):
    x = random.randrange(25, WIDTH - 25,40)
    y = random.randrange(HEIGHT+25,HEIGHT+250,70)
    zombie_x.append(x)
    zombie_y.append(y)

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
    global left_key, right_key, player_x, player_y, zombie_y, zombie_x, health

    if current_screen == "play":
        #player
        speed = 8
        if left_key == True:
            player_x -= speed
        elif right_key == True:
            player_x += speed


        #player border
        if player_x < 10:
            player_x = 10
        elif player_x > WIDTH - 55:
            player_x = WIDTH - 55


        #zombie
        for index in range(len(zombie_y)):
            zombie_y[index] -= 5
            if zombie_y[index] < 0:
                zombie_y[index] = random.randrange(HEIGHT + 25, HEIGHT + 250, 70)
                zombie_x[index] = random.randrange(15, WIDTH - 25, 40)



def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y, zombie_x, zombie_y, zombie_w, zombie_h, hit

    if current_screen == "menu":
        arcade.draw_text("DODGE ZOMBIES", 25, HEIGHT-100,arcade.color.BLACK,36,2000,"Right", "Calibri",True)
        arcade.draw_text("Press Space to play",WIDTH/3,HEIGHT/3,arcade.color.BLACK)
        arcade.draw_text("ESC to return to menu",WIDTH/3,HEIGHT/3.5,arcade.color.BLACK)
        arcade.draw_text("How to Play(a)", WIDTH/3, HEIGHT/2,arcade.color.BLACK)

        arcade.set_background_color(arcade.color.LIGHT_MOSS_GREEN)

    if current_screen == "instructions":
        arcade.draw_text(""" 1. Use left and right arrow keys to move the player.
        2. Your objective is to get as far as you can without dying.
        3. Each time you hit a zombie you lose 10 health
        4. Once your health reaches zero, you lose.
        """)

        arcade.set_background_color(arcade.color.PINK_PEARL)

    if current_screen == "play":
        arcade.set_background_color(arcade.color.ASH_GREY)

        arcade.draw_xywh_rectangle_filled(player_x, player_y, 40,40, arcade.color.RED)

        for x,y in zip(zombie_x,zombie_y):
            draw_zombie(x,y,zombie_w,zombie_h)


def on_key_press(key, modifiers):
    global left_key, right_key, up_key, down_key, current_screen

    if current_screen == "menu":
        if key == arcade.key.SPACE:
            current_screen = "play"

    if current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

        if key == arcade.key.LEFT:
            left_key = True
        elif key == arcade.key.RIGHT:
            right_key = True



def on_key_release(key, modifiers):
    global left_key, right_key, up_key, down_key

    if current_screen == "play":

        if key == arcade.key.LEFT:
            left_key = False
        elif key == arcade.key.RIGHT:
            right_key = False


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_zombie(x,y,w,h):
    # x = 320
    # y = 240
    # w = 30
    # h = 80

    arcade.draw_xywh_rectangle_filled(x, y, w, h/8*3, arcade.color.MOSS_GREEN)
    arcade.draw_xywh_rectangle_filled(x, y-40, w, h/2, arcade.color.SAND)
    arcade.draw_xywh_rectangle_filled(x, y-50, w-20, h/8, arcade.color.MOSS_GREEN)
    arcade.draw_xywh_rectangle_filled(x+20, y-50, w-20, h/8, arcade.color.MOSS_GREEN)

if __name__ == '__main__':
    setup()
