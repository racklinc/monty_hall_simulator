# monty_hall_simulator
A Monty Hall game Simulator. Made to simulate the 66% probability of getting the correct choice if a player switches "doors" under the accepted rules of the game.

This is a python script that is made to simulate a Monty Hall game with the typically accepted rules of the game. There are numerous articles, videos, and a few web-based simulations of the game. I will leave that up to you to research. I hadn't found one that was automated however, so I wanted to make one myself. My interest in making this was that, like most people, the odds of being correct 66% of the time that you switch was not intuitive to me despite much research being done on it. I believed the people who did the articles and videos but I wanted to prove it for myself. A large number of simulations would undoubtedly prove it to me.

Once started it will display a short amount of information and a couple of questions. The first being if you want the player to randomly decide which door to choose on the second round. If answering "y" for yes then it will track randomly selected answers for the second round and track the probability of if the player had always switched and then compare the difference of percentages. Any other response will run the game with the player always switching selections on the second round. The second question is how many times you want to simulate playing the game. Python handles large numbers well, so feel free to put a number in the billions if that satisfies you. It will take a lot of time to do this, on my personal PC it does roughly 10,000 simulations a second.

The actual game engine itself will randomly generate a number between 0-2 (3 options) and assign that as the right answer. It then randomly generates another number between 0-2 (3 options again) and makes that the player's guess. It then determines a wrong reveal (a goat in game venacular) avoiding revealing the player's guess. Then a decision tree splits dependant on your response of whether you want round two to always be switch doors or randomly guess. The default response of just enter selects the other door not revealed that wasn't the first selection. This after a few thousand simulations averages out to 66%. The "y" option will randomly decide and track the random decision and the always switch chances and show the difference. After a few thousand this always averages out to be 49%-51% as most people would expect. Also, I haven't hard-coded this so that it won't accpet invalid responses for the prompts. If you give invalid responses the script will exit with errors.

If round two were truly randomly decided, on the second round, it would be a 50-50 chance, but that is ignoring the psychology aspect of the game and certainly isn't as good as the statistic of being right 66% of the time. This has proven to me that if confronted with this game under the accepted rules, always switch your choice on the second round for the best odds.
