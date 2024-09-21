import pgzrun
import random

WIDTH = 800
HEIGHT = 600

FONT_option = (255,255,255)

CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

CENTER = (CENTER_X, CENTER_Y)

ITEMS = ["bags", "battery", "bottle", "chips"]

def draw():
    screen.blit("beground", (0,0))

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0, number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option+ "img")
        new_items.append(items)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index+1)* gap_size
        item.x = new_x_pos
pgzrun.go()