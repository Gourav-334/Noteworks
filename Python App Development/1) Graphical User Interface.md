# $\fbox{Chapter 1: GRAPHICAL USER INTERFACE}$





## **Topic - 1: Tkinter**

```python
import tkinter as tk


# Function to update label when button is clicked
def on_button_click():
    label.config(text="Button Clicked!")


# Create the main window
root = tk.Tk()
root.title("My First Tkinter Window")
root.geometry("400x300")


# Creating a widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root, height=10, width=40)
text.pack()


# Start the Tkinter event loop
root.mainloop()
```
