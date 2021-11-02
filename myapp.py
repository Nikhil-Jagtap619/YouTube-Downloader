#import all necessary libraries(1)
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube #youtube library to download videos


#write backend codes(3)
folder_name = ""

#file location directory
def openlocation():
    global folder_name
    folder_name = filedialog.askdirectory()
    if len(folder_name)>1:
        locationError.config(text=folder_name, fg="green")
    else:
        messagebox.showwarning("Warning!","please choose a folder!")

#download video funtion
def downloadVideo():
    choice = qualityChoice.get()
    url = entryBox.get()

    if len(url)>1:
        error.config(text="url found", fg="green")
        yt = YouTube(url)

        if choice == qualityChoice[0]:
            select = yt.streams.filter(progressive=True).first()
        elif choice == qualityChoice[1]:
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
        elif choice == qualityChoice[2]:
            select = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showwarning("Warning!","choose your quality")

    #download video 
    select.download(folder_name)
    messagebox.showwarning("Download Status","Download Complete!")
        

#set workspace width, height and other components(2) 
root = Tk()
root.title("youtube downloader")
root.geometry("500x460+560+200")
root.resizable(width=False, height=False)
root.columnconfigure(0, weight=1) #sets every component in center

#link paste label
ytLabel = Label(root, text="Enter your URL here", font=("Helvetica", 14))
ytLabel.grid()

#enter box for url pasting
ytEntryVar = StringVar()
entryBox = Entry(root, width=50, textvariable=ytEntryVar)
entryBox.grid()

#error mgs box
#error = messagebox.showwarning("incorrect url")
error = Label(root, text="no url found", fg="red")
error.grid()

#distination to save the video
saveLabel = Label(root, text="Choose your distination folder", font=("arial" ,13))
saveLabel.grid()

#make a button to open the directory
saveEntry = Button(root, text="choose path", width=10, bg="#343a40", fg="#ff4d6d", command=openlocation)
saveEntry.grid()

#location error if user doesnt choose the path
#locationError = messagebox.showwarning("choose your destination")
locationError = Label(root, text="no path selected", fg="red")
locationError.grid()

#download Quality label
qualityLabel = Label(root, text="Quality", font=("arial", 13))
qualityLabel.grid()

#choices of video quality
choices = ["720p", "144p", "only audio"]
qualityChoice = ttk.Combobox(root, values=choices)
qualityChoice.grid()

#download button
download = Button(root, text="Download", bg="#343a40", fg="#ff4d6d", width=10, command=downloadVideo)
download.grid()



root.mainloop()

