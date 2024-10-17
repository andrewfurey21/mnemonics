import tkinter as tk
from random import choice
from dataWork import UseData
# Sample words and mnemonics
words = [
    {"word": "Bonjour", "meaning": "Hello (French)", "mnemonic": "Bon = Good, Jour = Day"},
    {"word": "Hola", "meaning": "Hello (Spanish)", "mnemonic": "Sounds like Holla!"},
    # Add more words here

    # word # meaning # mnemonic
]


class FlashcardApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Vocabulary Flashcards")
        self.german = UseData.read_in_german('german.csv')
        print(self.german)
        # inital page to 0 where u choose the language
        self.page = 0
        # Set up labels
        self.word_label =tk.Label(
    root,
    text="Hello, Tkinter!", 
    font=("Helvetica", 24, "bold"),  # Font family, size, and weight
    fg="#ffffff",  # Text color
    bg="#3498db",  # Background color
    padx=20,  # Padding around text horizontally
    pady=20,  # Padding around text vertically
    relief="flat",  # Adds a 3D effect (flat, raised, sunken, ridge, etc.)
    borderwidth=5,  # Border thickness
)
        self.word_label.pack(pady=20)
        
        self.mnemonic_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.mnemonic_label.pack(pady=10)

        # Set up buttons
        self.show_mnemonic_button = tk.Button(root, text="Show Meaning", command=self.show_meaning)
        self.show_mnemonic_button.pack(pady=10)

        self.next_word_button = tk.Button(root, text="Next Word", command=self.next_word)
        self.next_word_button.pack(pady=10)

        # Display the first word
        self.next_word()

    def next_word(self):
        self.current_word = choice(words)
        self.word_label.config(text=self.current_word["word"])
        # remove the mnemonic
        self.mnemonic_label.config(text="")
        self.show_mnemonic_button.config(text="Show Meaning")
    def submit(self):
        # Get the input from the Entry widget
        entered_text = self.input_field.get()
        print(entered_text)

    ### Function called when button show meaning is pressed, make the meaning appear
    def show_meaning(self):
        # self.mnemonic_label.config(text=f"{self.current_word['meaning']}\nMnemonic: {self.current_word['mnemonic']}")
        meaning = self.german[self.page]['meaning']
        mnemonic = self.german[self.page]['mnemonic']
        self.mnemonic_label.config(text=f"{meaning}\nMnemonic: {mnemonic}")
        self.show_mnemonic_button.config(text="Hide Meaning", command=self.hide_meaning)

        ## If no mnemonic then create and save
        if (False):
            self.input_field = tk.Entry(root, width=30)
            self.input_field.pack(pady=10)
            submit_button = tk.Button(root, text="Submit", command=self.submit)
            submit_button.pack(pady=10)

    def hide_meaning(self):
        self.mnemonic_label.config(text="")
        self.show_mnemonic_button.config(text="Show Meaning", command=self.show_meaning)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.geometry("400x600+50+100")
    root.mainloop()