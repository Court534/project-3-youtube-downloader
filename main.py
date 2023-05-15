import tkinter
import customtkinter
from pytube import YouTube

# System setting (This will adapt to the users system setting e.g light/dark mode)
customtkinter.set_appearance_mode("System")

# Sets the default color scheme to blue 
customtkinter.set_default_color_theme("blue")

# Creating the frame for the app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements 
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
# Adding padding
title.pack(padx=10, pady=10)

# Link input 
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack

# Run app
app.mainloop()

