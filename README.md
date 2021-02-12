# "PENDU" with Python (in console and GUI)

Dev. by : Rad-Wane  


## Game play:

The hanging man ("pendu" in french), is a word guessing game where a word is to be guessed based only on the number of its characters. A player have 7 tries to find the word, otherwise he's hung. 

<img src="/img/play.png" height= "300" width="200"/>

This game feature's two playing modes : single player and multi-player:   

<img src="/img/modes.png" height= "300" width="200"/>

The single player mode, once chosen, fetch a random word from `random_words` library. The word is then to be guessed within 7 tries. Each time an entered letter is not in the word, a drawing is made (see table below). 

Lives left | 7 | 6 | 5 | 4 | 3 | 2 | 1 | Hung
:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
 Drawing   | <img src="/img/1.png" height= "100" width="90"/> | <img src="/img/2.png" height= "100" width="90"/> | <img src="/img/3.png" height= "100" width="90"/> | <img src="/img/4.png" height= "100" width="90"/> | <img src="/img/5.png" height= "100" width="90"/> | <img src="/img/6.png" height= "100" width="90"/> | <img src="/img/7.png" height= "100" width="90"/> 

The multi-player mode allows a second player to enter a word, the first player have to guess it :  

<img src="/img/mp1.png" height= "350" width="350"/>

Upon winning or loosing, a `message box` is displayed, showing the correct word, and a restarting with another word feature : 

<img src="/img/final.png" height= "350" width="350"/>

In the file `pendu_console.py` there is a variant of the game that uses Python's console :
<img src="/img/console.png" height= "300" width="300"/>


## The code:

This game uses `tkinter`, the code has comments for clarity. Images used for the game are in `img` file. The screen dimensions chosen are : `300x400`. Besides `tkinter`, I imported `random_words` for generating random words in single player mode.

After initializations and the first screen, player have to choose a mode, and have to click on one of the two buttons displayed. Depending on the button clicked, one of the two function will run : `spm()` or `mpm()`. The first screen is then partially destroyed and the game continue. For further details, see the code : `pendu_gui.py`


