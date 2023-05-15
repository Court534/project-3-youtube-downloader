import tkinter
import customtkinter
from pytube import YouTube

# Download function
def startDownload():
    try:
        # Gets the pasted link and tries to donwload the highest resolution possible
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        # Makes sure the title is white and appears once downloaded
        title.configure(text=ytObject.title, text_color="white")
        finishedLabel.configure(text="")
        video.download()
        # Once the video is downloaded you get a success message in green
        finishedLabel.configure(text="Video Downloaded!", text_color="green")
    except:
        # If the download fails you get an alert in red
        finishedLabel.configure(text="Download Error!", text_color="red")
        
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
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading text
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)







# Run app
app.mainloop()

