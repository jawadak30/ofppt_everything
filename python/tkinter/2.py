import tkinter as tk
from time import strftime

class DigitalWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Watch")

        # Create label for displaying time
        self.time_label = tk.Label(root, font=('calibri', 60, 'bold'), background='black', foreground='white')

        # Place the label in the window
        self.time_label.pack(anchor='center')

        # Update the time continuously
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = strftime('%H:%M:%S %p')

        # Update the time label text
        self.time_label['text'] = current_time

        # Call the update_time function after 1000ms (1 second)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    watch = DigitalWatch(root)
    root.mainloop()