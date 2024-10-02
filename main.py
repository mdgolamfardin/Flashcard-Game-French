import tkinter as tk
import pandas as pd
import random

# ------------------------------ Constants ------------------------------------------ #
# Defining constant values for background color and language labels
BACKGROUND_COLOR = "#B1DDC6"  # Light green background color for the app
FRENCH = "French"  # Label for French language
ENGLISH = "English"  # Label for English language

# ------------------------------ Variables / Data ------------------------------------------ #
# Reading the French-English word data from a CSV file and converting it into a list of dictionaries
data = pd.read_csv("data/french_words.csv")  # Load the CSV data into a pandas DataFrame
fr_word_list = data.to_dict(orient="records")  # Convert the DataFrame to a list of dictionaries
random_fr_word = random.choice(fr_word_list)  # Select a random word from the list for the initial display


# ------------------------------ Functions ------------------------------------------ #
# Function to flip the flashcard to show the English word after 3 seconds
def flip():
    # Re-enable the right and wrong buttons after flipping the card
    right_btn.config(state="normal")
    wrong_btn.config(state="normal")

    # Change the flashcard image to the back side
    canvas.itemconfig(card_image, image=back_img)

    # Display the English translation of the current word
    english_word = random_fr_word["English"]
    canvas.itemconfig(card_title, text=f"English", fill="white")  # Update the title to English
    canvas.itemconfig(card_word, text=f"{english_word}", fill="white")  # Update the word to its English translation


# Function to display a new French word flashcard
def new_card():
    global random_fr_word  # Declare the global variable to update the current random word

    # Choose a new random word from the list
    random_fr_word = random.choice(fr_word_list)

    # Disable the right and wrong buttons until the card is flipped
    right_btn.config(state="disabled")
    wrong_btn.config(state="disabled")

    # Display the French word on the front of the flashcard
    french_word = random_fr_word["French"]
    canvas.itemconfig(card_title, text=f"French", fill="black")  # Set the title to French
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")  # Display the French word
    canvas.itemconfig(card_image, image=front_img)  # Set the image to the front of the card

    # Schedule the flip function to run after 3 seconds
    window.after(3000, flip)


# Function to handle the right button click (correct answer)
def right_btn_action():
    # Remove the current word from the list (considered learned)
    fr_word_list.remove(random_fr_word)

    # Save the remaining words back to the CSV file, so the learned words are not repeated
    remaining_list_df = pd.DataFrame(fr_word_list)
    remaining_list_df.to_csv("data/french_words.csv", index=False)

    # Display a new French word flashcard
    new_card()


# ------------------------------ UI LAYOUT ------------------------------------------ #
# Creating the main application window
window = tk.Tk()
window.title("Flashcard Game French")  # Set the window title
window.config(width=900, height=626, bg=BACKGROUND_COLOR, pady=50,
              padx=50)  # Configure window size, background color, and padding

# Load images for the flashcards and buttons
front_img = tk.PhotoImage(file="images/card_front.png")  # Image for the front of the flashcard
back_img = tk.PhotoImage(file="images/card_back.png")  # Image for the back of the flashcard
right_img = tk.PhotoImage(file="images/right.png")  # Image for the right (correct) button
wrong_img = tk.PhotoImage(file="images/wrong.png")  # Image for the wrong (incorrect) button

# Create a canvas for displaying the flashcards
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                   highlightthickness=0)  # Set canvas size and background color
card_image = canvas.create_image(400, 263, image=front_img)  # Position the flashcard image at the center of the canvas
card_title = canvas.create_text(400, 150, text=FRENCH, font=("Arial", 40, "italic"),
                                fill='black')  # Display the language title
card_word = canvas.create_text(400, 263, text="WORD", font=("Arial", 60, "bold"), fill='black')  # Display the word text
canvas.grid(row=0, column=0, columnspan=2)  # Position the canvas in the grid layout

# Create the wrong button with its corresponding image and action
wrong_btn = tk.Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_card)
wrong_btn.grid(row=1, column=0)  # Position the wrong button in the grid layout

# Create the right button with its corresponding image and action
right_btn = tk.Button(image=right_img, highlightthickness=0, borderwidth=0, command=right_btn_action)
right_btn.grid(row=1, column=1)  # Position the right button in the grid layout

# Start by displaying a new French word flashcard
new_card()

# Start the Tkinter main loop to listen for user interaction
window.mainloop()
