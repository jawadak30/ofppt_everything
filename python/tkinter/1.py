import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter Website!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Website")

# Create widgets
label = tk.Label(root, text="Welcome to My Tkinter Website", font=("Helvetica", 16))
button = tk.Button(root, text="Click me!", command=on_button_click)

# Place widgets in the window
label.pack(pady=20)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()