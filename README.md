# basketball_language
This repository contains a python language compiler that will understand basketball play-by-play commands and return a boxscore for players mentioned in the play-by-play. It will take cleaned up commands from a website like espn.com and will produce a boxscore similar to a boxscore on nba.com or espn.com.

This language runs by reading through a text file of basketball play-by-play commands. To create a command, it must start with a first and last name using capital letters to create a player. It must then be followed by an action (make, miss, steal, block, rebound, assist, turnover or foul). In the case that the action was a make or miss, it must be fouled by the shot that was attempted (Giannis Antetokounmpo misses two pointer). A two pointer, three pointer, or free throw can follow the make or miss command. For a rebound, it must be followed by the category of rebound (Giannis Antetokounmpo rebound defensive). This category can be either defensive or offensive. The return will be a final boxscore using 18 categories that classify the traditional stats in a basketball game. 

The interesting part about this language is that, after cleaning up to data to fit the requirements, this language can produce full and accuarate boxscores for any basketball game that uses play-by-play regardless of the league or country the game will be played in. Further steps could then be taken to produce advanced stats from the boxscore this language produces.

To run this language, use the command: python3 basketball.py (txt file)
Ex: python3 basketball.py sample1.txt
