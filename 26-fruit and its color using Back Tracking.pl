% Define fruits and their possible colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(kiwi, brown).

% Predicate to check if a given fruit has a specified color
has_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Predicate to find all fruits with a specified color using backtracking
fruits_with_color(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl,
    fail. % Backtrack to find more fruits with the same color

% Example queries:
% To find the color of a specific fruit:
% ?- has_color(apple, Color).
%
% To find all fruits with a specified color:
% ?- fruits_with_color(red).
