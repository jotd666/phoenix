# phoenix500
remake of Phoenix for ECS Amiga

jotd: reverse-engineering, transcode, graphics conversion
no9: music
Christopher from http://www.computerarcheology.com/Arcade/Phoenix/: Z80 disassembly and small RE
PascalDe73: amiga icons
mrv2k: flyer

Features:

- 99% same gameplay (see below for the 1% difference)
- updating highscore is now done in real-time not when restarting a game
- applied Don Hodges fix to avoid score corruption when shooting 3 flying birds


Instructions:

5/fire: insert coin
1/up: start 1P game

left/right joystick/arrows: move ship
fire/ctrl: shoot
2nd button/down/alt: shield


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