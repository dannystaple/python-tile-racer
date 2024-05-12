# Dojo Racer

A PyGameZero based 2D top down racing game. Using Tiled exported files for the tilemaps.

## Playing

    pgzrun racer.py

Controls are:

* up -> accelerate
* down -> brake
* left, right -> steering

The aim is to drive through the checkpoints to the finish line.

## Features

* Supports [tiled](https://www.mapeditor.org) racing maps.
* Sliding screen window in tile map.
* Car has inertia.
* Checkpoints and single lap win condition.
* Wrong way detection.
* Map boundary collisions.

### Roadmap

* Object layers - barrels, trees. Complicated by the fact that the tileset doesn't have these in the same tile size as the map layer.
* Object collisions.
* Top banner for score/checkpoints player data.
* Laps
* Start and end screens.
* Other racers.
* sound

## Files

* racer.py - The game code. Run this to play.
* Racer.tsx - An inital racetrack file for tiled.
* spritesheet_tiles.json - The tileset to import into the game. Exported as json from tiled.
* racer_map_1.json - Exported racetrack map from tiled.
* map_and_screen_ref.drawio.xml - Load this into draw.io to understand the screen and car relative position model.
* images/ - game image assets

## Code explained (A little)

The GameMap class handles loading a tileset and a map. It creates some setup variables.
This class has code to blit a single tile from the tileset. Tiled uses a single image with many tiles, and
image offsets are used to find them. `blit_tile` handles this.

The GameMap `draw` method takes a map_offset, which is the screen_origin, where 
the screen is relative to the top left of the map. A map is loaded into the `game_map` global for now, and the game is played here.

The function `start_game` prepares the player, and could be used to have a play again type state for the game. In this the player has a `map_rect` variable, which contains player coordinates and rectangle relative to the map. This is where player movements and collisions will be applied.

In the `draw` function, the screen is set to a neutral green, which might be unnecessary if the map is larger than the screen.

The screen origin is calulated by trying to place the players car in the middle of the screen, but then constraining the screen to the boundaries of the map.

We can then draw the map. The players drawn screen coordinates must be based on players map_rect shifted by the screen origin. Once we have that, we can draw the player. Finally there are a couple of player messages.

The function `do_check_points` attempts to collide the players `map_rect` with the check point rectangles. These are on an object layer in tiled, and must be put into the race map in order. So index 0 should be the first check point after the start line. This ensures a player can't simply cheat and win by driving in a circle, as well as the wrong way and win conditions. It must check that the player is moving forward.
There is some complication here in that it must account for the checkpoints looping from the finish line to the start point. 
A special check point named "finish" marks the finish line.

In the `update` function, the keyboard is checked for player movements. A steering value is set, but only applied if the player has speed - slightly car-like, but a bit fake in terms of physics. The angle is modified by the steering.
When up is pressed, a vector is created using polar coordinates of an acceleration value of 2, and the players angle. The -90 is a slight hack based on the sprite files rotation. We add the acceleration to the current speed of the player. When down (brake) is pressed, a similar vector is created and subtracted from the players speed.
If no accelerate or break key is pressed, drag is applied to the car by multiplying the speed vector by 0.9.
Update then updates the players map_rect based on the speed vector, and then does the check points.

The code finally calls the start_game function to set the variables up.

## Game License

CC 1.0 Universal
I encourage pull requests with features and discussion.

## Acknowledgements

Tileset and car images come from the Racing pack at [kenney.nl](https://kenney.nl/assets/racing-pack). These are covered
by the CC 1.0 Universal license.

Learned lots from tutorials at [Game From Scratch](https://www.gamefromscratch.com/post/2015/10/14/Tiled-Map-Editor-Tutorial-Series.aspx)
