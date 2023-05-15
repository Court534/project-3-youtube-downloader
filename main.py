import tkinter
import customtkinter
from pytube import YouTube

# Download function
def startDownload():
    try:
        # Gets the pasted link and tries to donwload the highest resolution possible
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
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

# Create a progress bar
def on_progress(stream, chunk, bytes_remaining):
    # Get the total size of the file to be downloaded, in bytes
    total_size = stream.filesize
    # Calculate how many bytes have been downloaded so far by subtracting the bytes remaining from the total size
    bytes_downloaded = total_size - bytes_remaining
     # Calculate the percentage of the file that has been downloaded
    percentage_completion = bytes_downloaded / total_size * 100
     # Convert the percentage to an integer and then to a string to use it in the GUI
    per = str(int(percentage_completion))
     # Update the text of the 'percentage' widget to show the current percentage completion
    percentage.configure(text=per + "%")
    # Force an update of the GUI
    percentage.update()
  
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

# Create download progress bar
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Finished downloading text
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)







# Run app
app.mainloop()

