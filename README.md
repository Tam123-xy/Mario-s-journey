TL12-05
******************************
The elements and characters used in the game are from 'Super Mario Bros,' but the game's design is totally different from it. Mario must pass through the blockers by pressing specific arrow keys. 
The objective is to break the highest scores by passing through as many blockers as possible within a limited time (30 seconds, the seconds might be changed).

Blockers:
Yellow Star: UP arrow key
Mushroom: DOWN arrow key
Turtle: RIGHT arrow key

-The game ends when the timer reaches zero. 
-When Mario passes through a blocker, the player earns one point. The scores will be recorded and output to encourage players to break their own highest scores.
-When Mario successfully passes through 5 blockers continually, an extra 5 seconds may be added to the timer.
-Blockers are static , Mario is animate, but all these will remain their own coordinate. IT IS NOT A DETECT COLLISION GAME
-Pygame

count down timer:
https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame

Intro screen, score screen, animation Mario:
https://youtu.be/AY9MnQ4x3zk?si=XYL4WheW0y4ml7-8

Blocker loop by own :)
***********************************
Variables: Score, highest score, timer
Array: blockers list, animation Mario
*************************************
1)Players press the arrow key. 
TRUE- go through the next blocker
FALSE- will remain the same blocker until the key correct 

2)Timer reaches zero.  TRUE- end the game FALSE- game continue  -Effect music for some conditions -Highest scores
************************************
1) Mario passed through 5 blockers continually , an extra 4 seconds may be added to the timer. 
2) Score -To repeat a list of blockers for Mario to pass through.
3) Animation Mario (like gif)
************************************
Functions
***********************************
Files
*************************************
1) Tam Xin Yi 
-Design, blockers loop,  animation Mario, Time
2) Lew Li Jun 
-Scores loop & highest scores, effect (Background music, sound effects)
