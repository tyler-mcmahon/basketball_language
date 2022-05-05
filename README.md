# basketball_language
This repository contains a python language compiler that will understand basketball play-by-play commands and return stat lines for players included.

To create a command, it must start with a first and last name using capital letters to create a player. It must then be followed by an action (made, missed, steal, block, rebound). In the case that the action was a steal, another name must be provided for who the ball was stolen from (player 1 steals from player 2). The same is true for a block (player 1 blocks player 2). The return will be a final statline for each player name that was included.
