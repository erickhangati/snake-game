# Quiz Game

This is a simple quiz game implemented in Python. It prompts the user with True or False questions and checks if the answer is correct.

## How to Use

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Navigate to the project directory in your terminal.
4. Run the `main.py` file using Python.
5. Answer the True or False questions prompted in the terminal.
6. After answering all questions, your final score will be displayed.

## Files

- `quiz_brain.py`: Contains the `QuizBrain` class responsible for managing the quiz logic.
- `question_model.py`: Defines the `Question` class representing a single question.
- `data.py`: Contains the list of questions and answers used in the quiz.
- `main.py`: The main script that initializes the quiz and runs the game loop.

## How It Works

The `main.py` script reads the list of questions from `data.py`, creates `Question` objects, and then initializes a `QuizBrain` object with these questions. It then runs a loop, asking each question in turn until all questions are answered.

## Dependencies

This project has no external dependencies beyond Python itself.