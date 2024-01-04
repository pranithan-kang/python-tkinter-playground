import tkinter as tk

# Tkinter Window
root_window = tk.Tk()

# Window Settings
root_window.title("My Window")
root_window.geometry("800x600")
root_window.configure(background="black")

tk.Label(root_window, text="Hello World", bg="white", fg="black").pack()

tk.Button(root_window, text="Quit", command=root_window.quit).pack()

root_window.mainloop()