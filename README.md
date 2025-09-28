# Number Guessing Game

A simple Python number guessing game where the player tries to guess a randomly generated number between 1 and 10.

## Description

This is a console-based game where the computer generates a random number between 1 and 10, and the player has to guess it. The game provides hints ("go a little high" or "go a little low") and tracks the number of attempts taken to guess correctly.

## Features

- Random number generation between 1-10
- Real-time feedback on guesses (too high/too low)
- Attempt counter
- Simple and intuitive gameplay
- Input validation (requires integer input)

## How to Play

1. Run the Python script
2. Enter a number between 1 and 10 when prompted
3. Receive hints if your guess is too high or too low
4. Continue guessing until you find the correct number
5. The game will display how many attempts it took you to win

## Code Structure

```python
import random
num = random.randint(1, 10)  # Generate random number
tries = 0  # Initialize attempt counter

while True:
    # Get player's guess
    # Check if guess matches random number
    # Provide feedback and count attempts
##Example Gameplay
enter any number between 1 to 10: 5
go a little low
enter any number between 1 to 10: 8
go a little high  
enter any number between 1 to 10: 7
you are right you guess this number in 3 tries
