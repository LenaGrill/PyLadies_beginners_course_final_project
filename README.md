# PyLadies_beginners_course_final_project

Things to improve:
1. Head of the snake should be a different symbol, to be easier recognized.
2. Number of X should be counted as score achieved. Makes it more interesting to play again.
3. Game ends when there is no more possible move.
4. impossible moves could be counted (when the position is already occupied or moving out of the map) and could be limited; 
    e.g. after 5 impossible moves/wrong tries, game ends.
6. [Currently, food is added during every loop. There is soon too much food in the map. Limit food adding to every time food is eaten.]
    => this was changed => new food is only added, when old one is eaten. But: currently, the food adding stops after a while, because new food is only added when old food is eaten and the coordinate is not occupied. If new food coordinate is occupied, no food is present and no new food will be added. Change by using loop.

