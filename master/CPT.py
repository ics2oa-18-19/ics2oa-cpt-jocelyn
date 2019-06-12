import arcade
import random

WIDTH = 500
HEIGHT = 650

current_screen = "menu"


#player
player_x = WIDTH / 2 - 40/2
player_y = 50

health = 100
player_speed = 7

left_key = False
right_key = False


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

zombie_speed = 5
zombie_loop = 0

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
    global left_key, right_key, player_x, player_y, zombie_y, zombie_x, health, current_screen,player_speed, zombie_speed, zombie_loop

    if current_screen == "play":
        # player

        if left_key == True:
            player_x -= player_speed
        elif right_key == True:
            player_x += player_speed

        # player border
        if player_x < 10:
            player_x = 10
        elif player_x > WIDTH - 55:
            player_x = WIDTH - 55

        # zombie
        for index in range(len(zombie_y)):
            zombie_y[index] -= zombie_speed
            if zombie_y[index] < 0 or health == 0:
                zombie_y[index] = random.randrange(HEIGHT + 25, HEIGHT + 250, 70)
                zombie_x[index] = random.randrange(15, WIDTH - 25, 40)

        if zombie_y[0] <= 0:
            zombie_loop += 1
            print(f"loop {zombie_loop}")
            if zombie_loop % 5 == 0:
                zombie_speed += 1
                print(f"speed: {zombie_speed}")


        # collision
        for i in range(len(zombie_x)):
            if (zombie_x[i] >= player_x and zombie_x[i] <= player_x + 45 and
                zombie_y[i] <= player_y and zombie_y[i] >= player_y - 45 or
                zombie_x[i] + zombie_w >= player_x and zombie_x[i] + zombie_w <= player_x + 45 and
                zombie_y[i] <= player_y and zombie_y[i] >= player_y - 45):
                    health -= 10
                    zombie_y[i] = random.randrange(HEIGHT + 25, HEIGHT + 250, 70)

        if health == 0:
            current_screen = "dead"
            for index in range(len(zombie_y)):
                    zombie_y[index] = random.randrange(HEIGHT + 25, HEIGHT + 250, 70)
                    zombie_x[index] = random.randrange(15, WIDTH - 25, 40)



    if current_screen == "dead":
        health = 100


def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y, zombie_x, zombie_y, zombie_w, zombie_h, health

    if current_screen == "menu":
        arcade.draw_text("DODGE ZOMBIES", 25, HEIGHT-100,arcade.color.BLACK,36,2000,"Right", "Calibri",True)
        arcade.draw_text("Press Space to play",WIDTH/3,HEIGHT/3,arcade.color.BLACK)
        arcade.draw_text("How to Play(a)", WIDTH/3, HEIGHT/2.5,arcade.color.BLACK)

        arcade.set_background_color(arcade.color.LIGHT_MOSS_GREEN)

    if current_screen == "instructions":

        arcade.draw_text("How to Play:", 20, HEIGHT-50,arcade.color.BLACK,24)
        arcade.draw_text(""" 
        1. Use left and right arrow keys to move the player.
        2. Your objective is to get as far as you can without dying.
        3. Each time you hit a zombie you lose 10 health
        4. Once your health reaches zero, you lose.
        """, 0, HEIGHT-HEIGHT/3,arcade.color.BLACK)
        arcade.draw_text("ESC to return to menu",WIDTH/3,50,arcade.color.BLACK)

        arcade.set_background_color(arcade.color.PINK_PEARL)

    if current_screen == "play":
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        #player
        draw_car(player_x, player_y)

        #zombie
        for x,y in zip(zombie_x,zombie_y):
            draw_zombie(x,y,zombie_w,zombie_h)

        #healthbar
        arcade.draw_xywh_rectangle_filled(275, 600, 200, 35, arcade.color.GOLDEN_POPPY)
        arcade.draw_xywh_rectangle_filled(285, 605, 180, 25, arcade.color.GOLDEN_BROWN)
        arcade.draw_xywh_rectangle_filled(285, 605, 180 * health / 100, 25, arcade.color.RED)

    if current_screen == "dead":
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text("DUN", 25, HEIGHT-100,arcade.color.RED,36,2000,"left","Calibri",True)
        arcade.draw_text("DUN", 300, HEIGHT - 150, arcade.color.RED, 36, 2000, "left", "Calibri", True)
        arcade.draw_text("DUN", 100, HEIGHT - 200, arcade.color.RED, 36, 2000, "left", "Calibri", True)
        arcade.draw_text("You Died", WIDTH/4,HEIGHT/2,arcade.color.WHITE,40)
        arcade.draw_text("ESC to return to menu",WIDTH/3,50,arcade.color.WHITE)

def on_key_press(key, modifiers):
    global left_key, right_key, up_key, down_key, current_screen, health

    if current_screen == "menu":
        if key == arcade.key.A:
            current_screen = "instructions"
        if key == arcade.key.SPACE:
            current_screen = "play"

    if current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

    if current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

        if key == arcade.key.LEFT:
            left_key = True
        elif key == arcade.key.RIGHT:
            right_key = True

    if current_screen == "dead":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"


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

    arcade.draw_xywh_rectangle_filled(x, y, w, h/8*3, arcade.color.LIGHT_MOSS_GREEN)
    arcade.draw_xywh_rectangle_filled(x, y-40, w, h/2, arcade.color.SAND)
    arcade.draw_xywh_rectangle_filled(x, y-50, w-20, h/8, arcade.color.LIGHT_MOSS_GREEN)
    arcade.draw_xywh_rectangle_filled(x+20, y-50, w-20, h/8, arcade.color.LIGHT_MOSS_GREEN)

def draw_car(x,y):
    arcade.draw_xywh_rectangle_filled(x, y, 40, 40, arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(x, y - 10, 10, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 30, y - 10, 10, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 5, y + 20, 30, 15, arcade.color.PALE_ROBIN_EGG_BLUE)
    arcade.draw_xywh_rectangle_filled(x, y + 5, 10, 5, arcade.color.GOLD)
    arcade.draw_xywh_rectangle_filled(x + 30, y + 5, 10, 5, arcade.color.GOLD)


if __name__ == '__main__':
    setup()
