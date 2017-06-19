# MTG-Counter
mtg life counter in python/kivy

MTG life counter program.
Made in kivy it contains two files, main.py and Life.kv.
Main.py contains program logic, such as method calls when a button is clicked.
Life.kv contains widget behavior, such as placement and text.

Functionality:  
-Clicking the "start" button will begin the countdown timer in the center top of screen.  
upon reaching zero the timer will display "TIME" in red and stop counting down.  
-Clicking the "round" button will stop and reset the count down timer to 50:00.  
-The round time is displayed int XX:YY where XX is time in minutes and YY is time in seconds.  
A typical round of magic the gathering is 50 minutes.  
-Clicking the "game" button will reset the life totals of both players to 20.  
This will not affect time and can be done regardless of if timer is running or not.  
-The buttons above and below the life counts will increase or descrease the count by 1.
