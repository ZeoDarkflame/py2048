# 2048 (Basic Game)
The game is available in 2 versions: In both Versions you are supposed to run the Mainline.py file while keeping the GBoard in same Directory
## Windows
* The Game should run on Windows if you have Microsoft C runtime installed, otherwise install it (the game doesn't do this for you)

## Linux
* To run this game on Linux, make sure you have getch installed, if not the game will install it for you on first Startup
* The Game Cannot Install getch if you do not have pip3 installed and the command runs fine on your version

## Rules

* Use the argument -n (or --n) to change the grid size and -w (or --w) to change the winning number, not entering a valid value will result in the defaults being used
* It is recommended to keep the winning number not higher than 2<sup>13</sup> or else the grid would distort, it wouldn't distort otherwise

### Movement
* w (lowercase) &#8594; up
* s (lowercase) &#8594; down
* a (lowercase) &#8594; left
* d (lowercase) &#8594; right
* u (lowercase) &#8594; undo
* z (lowercase) &#8594; quit
 
