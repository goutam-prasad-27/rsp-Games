Here's the explanation of the code:

**Imports:**

* `random`: This library is used to generate random choices for the computer (bot) in the game.

**Variables:**

* `rps`: This list stores the three possible choices for Rock, Paper, and Scissors in the game.
* `userName`: This variable stores the player's name, which is retrieved through user input.

**Main Loop (`while True`):**

* This loop keeps the game running until the player decides to exit. Inside the loop:
    * `userScore` and `botScore` are initialized to 0 for each round.
    * The user is presented with a menu:
        * Option 1: Start the game.
        * Option 2: Learn the game rules.
        * Option 3: Exit the game.
    * Based on the user's choice:
        * **Option 1 (Start Game):**
            * A loop runs for 5 rounds (controlled by `game` variable).
            * Inside the round loop:
                * The user is prompted to choose Rock (1), Paper (2), or Scissors (3).
                * Based on the user's input, a corresponding choice is assigned to `userChoice`.
                * The computer's choice (`botChoice`) is randomly selected from the `rps` list.
                * The winner of the round is determined by comparing `userChoice` and `botChoice`.
                    * If it's a tie (both choices are the same), the game is a draw, and both scores are incremented by 1.
                    * If the user wins (according to Rock-Paper-Scissors rules), the user's score increases by 1.
                    * Otherwise, the bot's score increases by 1.
            * After all rounds are played:
                * The winner of the match (user or bot) is declared based on the final scores.
                * A draw message is displayed if scores are equal.
        * **Option 2 (Learn Rules):**
            * The game rules are printed, explaining how each choice wins against another.
        * **Option 3 (Exit Game):**
            * A goodbye message is displayed with the user's name, and the loop breaks, ending the game.
        * **Invalid Choice:**
            * If the user enters an invalid option (not 1, 2, or 3), an error message is displayed.
