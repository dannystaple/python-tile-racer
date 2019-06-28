from pygame import Vector2, image
from pgzero import loaders
from tile_settings import get_tile_set, TILESIZE
import json


import os.path

WIDTH = 800
HEIGHT = 800
car = Actor("car_yellow_1.png")
car.x = WIDTH//2
car.y = HEIGHT//2
car.speed = Vector2(0, 0)
car.max_speed_squared = 36


def load_tile_set():
    with open(os.path.join(loaders.root, "spritesheet_tiles.json")) as fd:
        tileset = json.load(fd)
    tile_image = image.load(os.path.join(loaders.root, tileset['image']))

    return tile_image, tileset

def load_map():
    with open(os.path.join(loaders.root, "racer_map_1.json")) as fd:
        tilemap = json.load(fd)
    return tilemap

tile_image, tileset = load_tile_set()
tilemap = load_map()

def blit_tile(screen_pos, tile_number):
    if tile_number == 0:
        return
    tile_number -= 1
    row = tile_number // tileset['columns']
    column = tile_number % tileset['columns']
    ts_x = (tileset['spacing'] + tileset['tilewidth']) * column
    ts_y = (tileset['spacing'] + tileset['tileheight']) * row
    screen.surface.blit(tile_image, screen_pos, area=(ts_x, ts_y, tileset['tilewidth'], tileset['tileheight']))


def draw_map():
    for layer in tilemap['layers']:
        row = 0
        column = 0
        for tile in layer.get('data', []):
            screen_x = column * tilemap['tilewidth']
            screen_y = row * tilemap['tileheight']
            if screen_x < WIDTH and screen_y < HEIGHT:
                blit_tile((screen_x, screen_y), tile)
            column += 1
            if column >= layer['width']:
                column = 0
                row += 1

def draw_grid():
    draw_map()


"""    for row_num, row in enumerate(tiles):
        for col_num, tile in enumerate(row):
            if tile:
                tile_files[tile].x = col_num * TILESIZE
                tile_files[tile].y = row_num * TILESIZE
                tile_files[tile].draw()
"""

def draw():
    screen.fill((39,174,96))
    draw_grid()
    car.draw()

def update():
    steering = 0
    if keyboard.left:
        steering = +5
    if keyboard.right:
        steering = -5
    if steering and car.speed.length_squared() > 0:
        car.angle += steering
        car.speed.rotate_ip(steering)
    if keyboard.up:
        if car.speed.length_squared() < car.max_speed_squared:
            speed = Vector2()
            speed.from_polar((1, car.angle-90))
            car.speed += speed
    else:
        car.speed *= 0.9
    car.x -= car.speed.x
    car.y += car.speed.y