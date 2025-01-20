import tkinter as tk

# Dictionary for word translation (replace this with an API call in a real application)
translations = {
    'hello': 'Hola',
    'goodbye': 'Adiós',
    'apple': 'Manzana',
    # Add more translations as needed
}

class WordTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Translator")

        self.entry = tk.Entry(root, width=40)
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_word)
        self.translation_label = tk.Label(root, text="Translation will appear here")

        self.entry.pack(pady=10)
        self.translate_button.pack(pady=5)
        self.translation_label.pack(pady=10)

    def translate_word(self):
        word = self.entry.get().lower()
        translation = translations.get(word, "Translation not found")
        self.translation_label.config(text=translation)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordTranslator(root)
    root.mainloop()