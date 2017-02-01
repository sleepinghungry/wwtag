#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
# This is a tutorial for writing Interactive Fiction with the BWX Adventure Game Engine.
# Ignore the magic before this point (feel free to ask if you are curious).
#
# First we need to import everything we need from the Game engine (a module called 'advent'):

# Allows access to the bwx_adventure module
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bwx_adventure.advent import *
# for cloud9
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

# These are the things that you can use to build your game.
# For example, a Location is a place the player can be, like a room, corridor, meddow, etc.
# The ones in all CAPS are directions that the player can use to move from one Location to another.

# Now we are ready to make our game.

# First, you need to create your game and give it a name:

game = Game("Brightworks Adventure")

# In Python, you create or change a 'variable' by simply assigning to it with '='.
# Here we are creating the variable 'game'.  We are assigning it the result of
# the function call Game("...").  A function is a bit of code defined elsewhere which
# is run when it's name is used with some arguments in paramenthesis '()'
# (in this case the string "Brightworks Adventure").
# This 'statement' creates your game and stores it in the 'variable' named 'game'.

# Now we want to create some locations.  We are going to recreate Brightworks!
# Let's start out on the sidewalk.

# Again we are going to create a 'variable', this time named 'sidewalk' and assign it
# the result of calling a function:

sidewalk = game.new_location(
  "DYLANS BRAIN",
  "Welcome to sesame street, this is a dark and dangerous place, leave before it is too late. *YOU SEE A SIGN IS SAY'S 'EXIT HEAD EAST' ")

# In this case we are calling a function which is part of our game.
# This is indicated by using a '.' after 'game' to get the function from 'game'.
# That function 'new_location' takes two arguments:
#   a short description (in this case 'Sidewalk')
#   a long description (in this case 'There ....')
# Again, the arguments are in parentheses '()' and are separated by a comma.
# Leaving out the comma is a common mistake and python will report a error like:
#
# File "tutorial1.py", line 38, in <module>
#     "Sidewalk"
# File "advent.py", line 214, in new_location
#     return self.add_location(Location(*args))
#   TypeError: __init__() takes exactly 3 arguments (2 given)
#
# This indicates that the error is on line 38 in tutorial1.py.  The rest of the lines
# show more context and give the error.  These error messages can be confusing, so if
# you have trouble with an error consult a collaborator.

# Let's create another location, this time the long description will be surrounded by
# triple quotes """.  This enables us to write the description over multiple lines:

vestibule = game.new_location(
  "CANADA",
""" *evil laughter* YOU ARE TRAPPED BOI, NOW YOU WILL GET EATEN ALIVE BY UNICORNS ,RUN TO THE NORTH! """)

# Again, make sure to end with """ and to close the parenthesis) and use a comma between
# the short and long description.

# Now we need to connect the two locations together.  Again, we are going to create
# a connection using a function.  This time we are not going to to assign it to a variable,
# but don't worry that it will simply vanish, instead it will be stored in the game.

game.new_connection("POO BRICK WALL", sidewalk, vestibule, EAST, WEST)


# The 'new_connection' function takes a name for the connection, two locations and
# two directions or lists of directions.  Again, the arguments are separated by commas
# and the lists of directions are separated by commas.  We could also have said:
# game.new_connection("Glass Door", sidewalk, vestibule, EAST, WEST)
# if we didn't want the player to be able to say "in" to enter the door.

# Now we are going to add our player at the starting location:

player = game.new_player(sidewalk)

# We assign our player to the variable 'player' even though we are not going to do anything
# with the player in this tutorial.

# Finally, we run the game.   You can run the game by typing 'python tutorial1.py' or by
# hitting 'Run' on trinket.io.
apocalypse = game.new_location(
    " apocalypse",
    """ whew, your not in dylan's brain. Trust me it's safer here. OH NO HE'S COMING...JOHN CENA! """)
game.new_connection("HORSE'S BUTT", vestibule, apocalypse, NORTH, SOUTH)

THE CLUB = game.new_location(
  "THE CLUB"
  """ *YOU ENTER A WELL LIT WINDOWLESS ROOM* you see a guide across the room""")
game.new_connection("pot of gold", apocalypse, the club, UP, DOWN)
  

game.run() 
