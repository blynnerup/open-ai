import tkinter
import customtkinter
from tkinter.filedialog import askopenfilename
from tkinter import filedialog


# Functions
def openFileBrowser():
    try:
        path = askopenfilename()
        audio_file_path.set(path)
        print(audio_file_path.get())
    except:
        print('geting file failed')
    shouldEnableTranscribeButton()

def selectDestinationFolder():
    try:
        folder = filedialog.askdirectory()
        transcription_file_path.set(folder)
        print(transcription_file_path.get())        
    except:
        print('setting destination folder failed')
    shouldEnableTranscribeButton()

def shouldEnableTranscribeButton():
    path = audio_file_path.get()
    folder = transcription_file_path.get()
    if path and folder:
        print("true")
        transcribe_button['state'] = "normal"
        transcribe_button.configure(text_color="white")
    else:
        print("false")
        transcribe_button['state'] = "disbaled"
        transcribe_button.configure(text_color="gray")

def transcribeFile():
    print('click')
    # Do Whisper

# Systems settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Audio to Text")

audio_file_path = customtkinter.StringVar(value='')
transcription_file_path = customtkinter.StringVar(value='')

# Label for path to audio source file
label = customtkinter.CTkLabel(app, text="Select audio file for transcription", font=('Trebuchet MS', 18))
label.pack(padx=10, pady=10, side="top", anchor="nw")

# Audio file source path
audio_file_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=audio_file_path)
audio_file_entry.pack(padx=10, side="top", anchor="nw")

# File browser button
select_source_btn = customtkinter.CTkButton(app, text="Select File", command=openFileBrowser)
select_source_btn.pack(padx = 10, pady=10, side="top", anchor="nw")

# Label for destination folder for transcribed file
destination_folder = customtkinter.CTkLabel(app, text="Selected folder for transcribed file")
label.pack(padx = 10, pady=10, side="top", anchor="nw")

# Destination folder for transcribed file
selected_folder = customtkinter.CTkEntry(app, width=350, height=40, textvariable=transcription_file_path)
selected_folder.pack(padx=10, pady=10, side="top", anchor="nw")

# Folder browser button
select_folder_btn =  customtkinter.CTkButton(app, text="Select folder", command=selectDestinationFolder)
select_folder_btn.pack(padx=10, pady=10, side="top", anchor="nw")

# Transcribe button
transcribe_button = customtkinter.CTkButton(app, text="Transcribe", command=transcribeFile, state="normal")
transcribe_button.pack(padx=10, pady=10, side="top", anchor="nw")

# Run app
app.mainloop()

