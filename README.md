## Hunt the Wumpus

The object of Hunt the Wumpus is to guide an adventurer to kill the Wumpus, find its
hidden gold, and escape alive. The Wumpus lives in a large cave of rooms arranged in
a 4 x 4 grid, where each room at has most four tunnels leading to the rooms to the
north, east, south, and west.
The adventurer starts the game in a random empty room in the Wumpus’ cave. Their
starting position is also the location of the escape rope that they will use to escape after they’ve completed their task.

## To run the application

Make sure you have python 2.7 installed. Then run `python wumpus.py`.


### How to Play

Each turn you may take one of two actions to guide the adventurer.
	
<b>Move:</b> You can move through a tunnel to an adjacent room.

<b>Fire an Arrow:</b> The adventurer has three arrows. You can aim each arrow by firing it into an adjacent room.If the arrow enters the Wumpus’ room, it pierces the Wumpus’ heart and kills the monster. If the adventurer runs out of arrows without having killed the Wumpus, you lose. 

If you wander into the room with the Wumpus, it will hear you and eat you. 

When the adventurer is in a room directly adjacent to a room containing an hazard, the player receives a message.

### Hazards
<b>Bottomless pits:</b> Two of the rooms have a bottomless pit in it, if the adventurer goes there, he falls into the pit, dies, and you lose. 

<b>Super bats:</b> Two rooms have super bats. If the adventurer enters the room that contains super bats, an angry bat grabs him and takes him to some other room at random.

<b>Gold:</b> The gold is a treasure sitting in a room that does not contain a hazard. If the adventurer is in a room containing gold, he automatically picks it up and takes it with him. 
