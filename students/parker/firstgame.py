from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object
world = BasicGameWorld()

# Hi Parker, Eping here.  I added quotes in this line of code so it would work:
#dungeon = world.create_location("Virgo palace, in the dungeon")

Virgo_palace = world.create_location("Virgo palace", "in the dungeon")

Espilcen = world.create_location ("Espilcen", " you are in the beautiful world of Espilcen.")

dungeon = world.create_location("dungeon cell", "you are standing in a dark, musty dungeon cell. there is a steel door at the front of the cell")

world.create_connection("door", dungeon, hallway, [IN, FORWARD], [NOT_DIRECTION])

hallway = world.create_location("hallway", "a long hallway is on the other side of the door.")

world.create_connection("door", hallway, dungeon, [IN, FORWARD], [OUT, BACK]) 

dungeon.create_object("metal", "you see a piece of metal on the ground")

door.make_requirement(metal)
                                
world.create_connection("trapdoor", hallway, room [IN, DOWN], [OUT, UP])

hallway.create_container("box", "there is a box on the ground next to the trapdoor.")

box.make_requirement(metal)

hallway.create_object ("key", "the key to the trapdoor is inside the box")

trapdoor.make_requirement(key)

world.create_location ("room", "a dimly lit room is on the other side of the trapdoor")

hallway.create_object("key", "you take the key out of the box and unlock the trapdoor")                             
                                
# So...your key can only be a requirement for a location or a connection.  It can't
# be a requirement for another object.  I'd recommend making your air_vent a
# connection between Espilcen and a new location.

game = BasicGameEngine(world)
game.run()
