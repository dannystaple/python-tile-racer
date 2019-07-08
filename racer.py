from pygame import Vector2, image
from pgzero import loaders
import json

import os.path

WIDTH = 800
HEIGHT = 800
screen_hw = WIDTH/2
screen_hh = HEIGHT/2
player = Actor("car_yellow_small.png")
player.max_speed_squared = 400


class GameMap:
    def __init__(self, tile_filename, map_filename):
        self.tileset = None
        self.tile_image = None
        self.tile_layers = None
        self.object_dict = None
        self.check_point_rects = []
        self.check_points = []
        self.starting_grid = []
        self.load_tileset(tile_filename)
        self.load_map(map_filename)

    def load_tileset(self, tile_filename):
        with open(os.path.join(loaders.root, tile_filename)) as fd:
            self.tileset = json.load(fd)
        self.tile_image = image.load(os.path.join(loaders.root, self.tileset['image']))

    def load_map(self, map_filename):
        with open(os.path.join(loaders.root, "racer_map_1.json")) as fd:
            self.tilemap = json.load(fd)
        self.width = self.tilemap['width'] * self.tilemap['tilewidth']
        self.height = self.tilemap['height'] * self.tilemap['tileheight']

        self.tile_layers = [layer for layer in self.tilemap['layers'] if layer['type']=='tilelayer']

        object_layers = (layer for layer in self.tilemap['layers'] if layer['type']=='objectgroup')
        self.object_dict = {layer['name']:layer for layer in object_layers}
        self.check_points = self.object_dict['check_points']['objects']

        self.check_point_rects = []
        for check_point in self.check_points:
            self.check_point_rects.append(
                Rect(check_point['x'], check_point['y'], check_point['width'], check_point['height']))

        self.starting_grid = self.object_dict['starting_grid']['objects']

    def blit_tile(self, screen_pos, tile_number):
        if tile_number == 0:
            return
        tile_number -= 1
        row = tile_number // self.tileset['columns']
        column = tile_number % self.tileset['columns']
        ts_x = (self.tileset['spacing'] + self.tileset['tilewidth']) * column
        ts_y = (self.tileset['spacing'] + self.tileset['tileheight']) * row
        screen.surface.blit(self.tile_image, screen_pos,
            area=(ts_x, ts_y, self.tileset['tilewidth'], self.tileset['tileheight']))

    def draw(self, map_offset):
        for layer in self.tile_layers:
            row = 0
            column = 0
            for tile in layer.get('data', []):
                screen_x = column * self.tilemap['tilewidth'] - map_offset[0]
                screen_y = row * self.tilemap['tileheight'] - map_offset[1]
                if screen_x < WIDTH and screen_y < HEIGHT and \
                        (screen_x + self.tilemap['tilewidth'] >= 0) and \
                        (screen_y + self.tilemap['tileheight'] >= 0):
                    self.blit_tile((screen_x, screen_y), tile)
                column += 1
                if column >= layer['width']:
                    column = 0
                    row += 1

game_map = GameMap("spritesheet_tiles.json", "racer_map_1.json")


def start_game():
    player.map_rect = Rect(game_map.starting_grid[0]['x'], game_map.starting_grid[0]['y'], player.width, player.height)
    player.speed = Vector2(0, 0)
    player.lap = 1
    player.won = False
    player.last_check_point = len(game_map.check_points) - 2
    player.wrong_way = False
    player.next_checkpoint = 0

def draw():
    screen.fill((39,174,96))
    screen_origin = (
        min(max(0, player.map_rect.x - screen_hw), game_map.width - WIDTH),
        min(max(0, player.map_rect.y - screen_hh), game_map.height - HEIGHT)
    )
    game_map.draw(screen_origin)

    player.x = player.map_rect.x - screen_origin[0]
    player.y = player.map_rect.y - screen_origin[1]
    player.draw()
    if player.won:
        screen.draw.text("You win!", (WIDTH//2, HEIGHT//2), fontsize=24, color='white')
    elif player.wrong_way:
        screen.draw.text("Wrong way!", (WIDTH//2, HEIGHT//2), fontsize=24, color='orange')
    else:
        screen.draw.text(str(player.next_checkpoint), (WIDTH//2, HEIGHT//2), fontsize=24, color='orange')


def do_check_points():
    collision_index = player.map_rect.collidelist(game_map.check_point_rects)
    # Only collide if it's different, and is a collision.
    if collision_index != -1 and collision_index != player.last_check_point:
        expected_right_way_checkpoint = (player.last_check_point + 1) % len(game_map.check_points)

        if collision_index == player.next_checkpoint:
            player.next_checkpoint += 1
            if game_map.check_points[collision_index]['name'] == 'finish':
                player.won = True
            player.wrong_way = False
        elif collision_index == expected_right_way_checkpoint:
            player.wrong_way = False
        else:
            player.wrong_way = True
        player.last_check_point = collision_index


def update():
    steering = 0
    pls = player.speed.length_squared()
    if keyboard.left:
        steering = +5
    if keyboard.right:
        steering = -5
    if steering and pls > 0:
        player.angle += steering
        player.speed.rotate_ip(steering)
        player.map_rect.width = player.width
        player.map_rect.height = player.height
    if keyboard.up:
        if pls < player.max_speed_squared:
            speed = Vector2()
            speed.from_polar((2, player.angle-90))
            player.speed += speed
    elif keyboard.down:
        if pls > 2:
            brake = Vector2()
            brake.from_polar((2, player.angle-90))
            player.speed -= brake
        else:
            player.speed = Vector2(0, 0)
    else:
        player.speed *= 0.9
    if pls > 0.5:
        player.map_rect.x -= player.speed.x
        player.map_rect.y += player.speed.y

    do_check_points()

start_game()