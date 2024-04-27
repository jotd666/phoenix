# phoenix500
remake of Phoenix for ECS/AGA Amiga

jotd: reverse-engineering, transcode, graphics conversion
no9: music
Toni Galvez: AGA recolored graphics
Christopher from http://www.computerarcheology.com/Arcade/Phoenix/: Z80 disassembly and small RE
PascalDe73: amiga icons
mrv2k: flyer

Features:

- 99% same gameplay (see below for the 1% difference)
- enhanced colors for AGA version
- updating highscore is now done in real-time not when restarting a game
- applied Don Hodges fix to avoid score corruption when shooting 3 flying birds

Instructions:

5/fire: insert coin
1/up/2nd button: start 1P game

left/right joystick/arrows: move ship
fire/ctrl: shoot
2nd button/down/alt: shield

If 2nd button is pressed once (to start game or to trigger shield) then the game
will disable down for shield.

Extra life at 3000 and 30000 (easiest dipswitch setting)

Cheat keys:

F1: toggle invincibility
F2: toggle infinite lives
F3: add 500 points
F4: skip level

Command line options:

INVINCIBLE: can't be killed
INFLIVES: infinite lives
CHEATKEYS: enable cheatkeys (see above)
B2SHIELD: disable shield with joy up/down, just use 2nd button
STARTLIVES: configure number of lives at start (matches dipswitches)
	
Vulture vertical movement:

I spent too much time trying to understand why vultures didn't go up or at least
very rarely. There are several pseudo-random variables involved and timers. I think
I have transcoded the exact same code as the original but I couldn't reproduce the
same sequence... So instead of losing my mind over this, I implemented a kludge
to force vultures up if they hadn't gone up for too long.
(means: the random value is 0 for too long instead of 1 when it's possible to go up).
Combined to an anti-wrap check which avoids that the vultures attack the player by
rising from the bottom, it works pretty well.

I still don't understand how the original game manages to do that part given the randomness
involved.