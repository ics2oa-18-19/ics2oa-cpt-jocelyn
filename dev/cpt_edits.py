import arcade
import random

WIDTH = 500
HEIGHT = 650

#player
player_x = WIDTH / 2
player_y = 50

left_key = False
right_key = False


#zombie
zombie_x = []
zombie_y = []

num = 10

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
    global left_key, right_key, player_x, player_y, zombie_y, zombie_x

    #player
    speed = 8
    if left_key == True:
        player_x -= speed
    elif right_key == True:
        player_x += speed


    #player border
    if player_x < 25:
        player_x = 25
    elif player_x > WIDTH - 25:
        player_x = WIDTH - 25


    #zombie
    for index in range(len(zombie_y)):
        zombie_y[index] -= 5
        if zombie_y[index] < 0:
            zombie_y[index] = random.randrange(HEIGHT + 25, HEIGHT + 250, 70)
            zombie_x[index] = random.randrange(25, WIDTH - 25, 40)


def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y, zombie_x, zombie_y

    arcade.draw_rectangle_filled(player_x, player_y, 45,45, arcade.color.BLUE)
    arcade.draw_line(WIDTH - 25, HEIGHT,WIDTH,120,arcade.color.NAVY_BLUE)
    arcade.draw_line(25, HEIGHT,0,120,arcade.color.NAVY_BLUE)

    for x,y in zip(zombie_x,zombie_y):
        draw_zombie(x,y)


def on_key_press(key, modifiers):
    global left_key, right_key, up_key, down_key

    if key == arcade.key.LEFT:
        left_key = True
    elif key == arcade.key.RIGHT:
        right_key = True



def on_key_release(key, modifiers):
    global left_key, right_key, up_key, down_key

    if key == arcade.key.LEFT:
        left_key = False
    elif key == arcade.key.RIGHT:
        right_key = False


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_zombie(x,y):

    arcade.draw_rectangle_filled(x,y,30,30,arcade.color.MOSS_GREEN)
    arcade.draw_rectangle_filled(x,y-35,30,40,arcade.color.SAND)
    arcade.draw_rectangle_filled(x-10,y-60,10,10,arcade.color.MOSS_GREEN)
    arcade.draw_rectangle_filled(x+10,y-60,10,10,arcade.color.MOSS_GREEN)



if __name__ == '__main__':
    setup()
