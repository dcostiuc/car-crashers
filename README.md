# ![An orange car representing the game logo](https://github.com/dan440402/car-crashers/blob/master/icon.png "Game Logo")  Car Crashers Game
By Daniel Costiuc  
Version 3

_Created using Python 3 and Pygame.
Based on the tutorials offered on pythonprogramming.net_


Description
---------
Play as a car that avoids falling blocks!

If the block hits your car, or your car hits the borders of the window, you will crash (the car).

With each block that falls down, the `speed` and `width` of the block increases, thus increasing difficulty. 

This is visualized by having the block slowly become more red.

There is no limit for these increases, so the game will always become _exponentially hard_ after around `20` blocks,   
and will be _impossible_ without "cheating" after `30` blocks 😅.   

This makes it fun and challenging for the player to obtain a higher score!

<details>
  <summary> Easter Egg </summary>  
  It is also fun to test the "cheat"/AI mode and see the highest score that it can get. 
  
  </br> See the Controls section for more information.
</details>


Features
---------
- `Main Menu` screen

- 2 cars to choose from (+ 1 "secret" car)

- Functioning game mechanics

- `Game Over` screen

- `Pause` feature

- `High-score` feature

- Functioning buttons


Controls
---------
Use the `mouse` to click on buttons and navigate through the screens.

Select a car by `clicking` on it.

When in-game, use `left` and `right` arrow keys to move the car.

Press and hold `shift` to give yourself boosts (or simply hold `shift` to always go fast).

Press `p` while playing as the car to pause the game, and press `p` again or click `Continue` to resume.

Press `q` while playing as the car to quit the game, or click on `Quit` whenever it is shown.

Press `b` to go back from the high-score screen to the game over screen, or click on the `Back` button.

Toggle `g` for "cheat"/AI mode:  
<details>
  <summary> Spoilers </summary>  
  
  </br>The game will be played for you through a basic AI, and you may find it hard to move the car manually while in this mode.</br>
  &nbsp;&nbsp;&nbsp;&nbsp; The original idea was to test the AI, though you can try to move it if you would like to.  
  
  Due to the nature of the game, you will still inevitably crash around a certain point even with the AI's help.
</details>
