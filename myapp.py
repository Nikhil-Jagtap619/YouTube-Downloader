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
# def downloadVideo():
#     choice = qualityChoice.get()
#     error.config(text="url found", fg="green")
#     messagebox.showinfo("YT downloader", "you've selected " + choice)
#     if (str(choice) == qualityChoice[0]) or (str(choice) == qualityChoice[1]):
#         url = YouTube(str(entryBox.get()))
#         video = url.streams.filter(progressive=True, file_extension="mp4").first()
#         video.download(folder_name)

#         messagebox.showwarning("Alert!", "Download Complete!")
#     elif choice == qualityChoice[2]:
#         url = YouTube(str(entryBox.get()))
#         music = url.streams.filter(progressive=True, only_audio=True).first()
#         music.download(folder_name)
#     else:
#         messagebox.showwarning("Warning", "Please select your quality!")


def downloader():
    choice = qualityChoice.get()
    error.config(text="url found", fg="green")
    url = YouTube(str(entryBox.get()))
    video = url.streams.filter(progressive=True, file_extension="mp4").first()
    messagebox.showinfo("download quality", "You selected "+choice )
    video.download(folder_name)
    messagebox.showwarning("status", "Download Complete!")


        

#set workspace width, height and other components(2) 
root = Tk()
root.title("youtube downloader")
root.geometry("500x400+560+200")
root.resizable(width=False, height=False)
root.columnconfigure(0, weight=1) #sets every component in center
image_icon = PhotoImage(file="yticon.png")
root.iconphoto(False, image_icon)

#link paste label
ytLabel = Label(root, text="Enter your URL here", font=("Helvetica", 14))
ytLabel.grid(pady=(10))

#enter box for url pasting
ytEntryVar = StringVar()
entryBox = Entry(root, width=50, textvariable=ytEntryVar)
entryBox.grid(pady=(10))

#error mgs box
#error = messagebox.showwarning("incorrect url")
error = Label(root, text="no url found", fg="red")
error.grid()

#distination to save the video
saveLabel = Label(root, text="Choose your distination folder", font=("arial" ,13))
saveLabel.grid()

#make a button to open the directory
saveEntry = Button(root, text="choose path", width=10, bg="#343a40", fg="#ff4d6d", command=openlocation)
saveEntry.grid(pady=(10))

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
qualityChoice.grid(pady=(20))


#download button
download = Button(root, text="Download", bg="#343a40", fg="#ff4d6d", width=10, command=downloader)
download.grid()

credit = Label(root, text="Made by Senpai_knock", fg="#f28482", font=("impact", 10))
credit.grid(pady=(40))


root.mainloop()

