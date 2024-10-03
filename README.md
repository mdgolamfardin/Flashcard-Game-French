# French Word Flash

Welcome to the French-Word-Flash-Card repository! This project is designed to help users learn French vocabulary through a digital flashcard application built with Python. It presents words in French and asks the user to recall the English translation, excluding words from the dataset that the user gets right. 

## Project Structure

This repository includes the following files and directories:

- `main.py` - The main Python script that runs the flashcard application.
- `data/` - Contains CSV files with French and English vocabulary:
  - `french_words.csv` - Primary file with French words and their English translations.
  - `french_words_backup.csv` - Backup file for the vocabulary list.
- `images/` - Contains images used in the flashcard interface:
  - `card_front.png` - Front of the flashcard displaying the French word.
  - `card_back.png` - Back of the flashcard displaying the English translation.
  - `can_recall.png` - Button to click if the user knows the word.
  - `cannot_recall.png` - Button to click if the user doesn't know the word.

## Features

- **Interactive Flashcards**: Click through flashcards to view French words and test your knowledge by recalling the English translation.
- **Data Storage**: Keeps a record of the words yet to learn, excluding learned words from reappearance.

## Technologies
- **Programming Language**: Python 3.12
- **Library**: Tkinter (for the GUI interface)
- **Data Handling**: 
  - **CSV Files**: Used to store and manipulate vocabulary data.
  - **Pandas**: Utilized for efficient data manipulation and analysis of the vocabulary data stored in CSV files.

## Getting Started
To get started with the French-Word-Flash project, you will need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/French-Word-Flash.git
   ```
2. Navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/French-Word-Flash.git
   ```
3. Run the `main.py` script:
  ```bash
    python main.py
  ```

### Alternative Installation (Without Terminal/Command Lines)
1. Download the zip file from [here](https://github.com/mdgolamfardin/French-Word-Flash).
2. Run `main.py` using an IDE (PyCharm for example). Install an IDE if you don't have one already.

## How To Use
The French-Word-Flash application helps you learn French vocabulary through an interactive flashcard system. Here's how to use it effectively:

1. **Interacting with Flashcards**:
   - After the word disappears, decide if you knew the correct English translation.
   - Click the **Green Button** if you knew the answer, or the **Red Button** if you didn't.

2. **Receiving Feedback**:
   - It tracks your progress by deleting the correctly guessed words from the dataset. You can check how many words are left in `french_words.csv`

3. **Session Management**:
   - Continue reviewing words, or close the application to end your session.

## Contributing
Contributions to this project are welcome, especially from fellow learners who are also taking the Udemy Python course. To contribute:

## Acknowledgments
This project is a part of the course "100 Days of Code: The Complete Python Pro Bootcamp", taught by Dr. Angela Yu on Udemy.

## Author
- [mdgolamfardin](https://github.com/mdgolamfardin)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
Enjoy playing Pong, and happy coding!
