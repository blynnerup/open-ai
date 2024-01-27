import customtkinter
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import whisper
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# Functions
def openFileBrowser():
    try:
        path = askopenfilename()
        audio_file_path.set(path)
        print(audio_file_path.get())
    except:
        print('geting file failed')
    shouldEnableTranscribeButton()
    setDefaultFileName()

def selectDestinationFolder():
    try:
        folder = filedialog.askdirectory() + "/"
        transcription_file_path.set(folder)
        print(transcription_file_path.get())        
    except:
        print('setting destination folder failed')
    shouldEnableTranscribeButton()

def setDefaultFileName():
    default_name = audio_file_path.get().rsplit('/', 1)[-1]
    default_name_update_filetype = default_name.rsplit('.', 1)[0] + "_text.txt"
    print(default_name_update_filetype)
    output_file_name.set( default_name_update_filetype)
    print(default_name)

def shouldEnableTranscribeButton():
    path = audio_file_path.get()
    folder = transcription_file_path.get()
    if path and folder:
        transcribe_button.configure(state="normal")
        transcribe_button.configure(text_color="white")
    else:
        transcribe_button['state'] = "disbaled"
        transcribe_button.configure(text_color="gray")

def transcribeFile():
    updateProgramOutput("Transcribing")
    # Do Whisper
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path.get(), language="da")
    
    with open(transcription_file_path.get() + output_file_name.get(), "w", encoding="utf-8") as file:
        file.write(result["text"])
        file.close()
    # print(result["text"])

    updateProgramOutput("Done")
    generate_corrected_transcript()

def updateProgramOutput(updateMessage):
    textbox.configure(state="normal")
    textbox.insert('end', updateMessage + "\n")
    textbox.configure(state="disabled")
    app.update()

def generate_corrected_transcript():
    # print(transcription_file_path.get() + output_file_name.get())
    updateProgramOutput("Preparing to correct file contents")
    with open("Hobbitten_dk_text2.txt", encoding="utf-8") as f: text_file_content = f.read()
    #system_prompt = "You are correcting a transcript of an audio file, where a person have read the first passages of the book The Hobbit in danish. Your task is to correct the transcribed text so that false words are in line with the text in The Hobbit, still in danish."
    system_prompt = "Can you tell me from which book the text is from? The text is in danish."
    corrected_transcript = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_file_content}
        ],
        max_tokens=100,
    )
    updateProgramOutput("File has been corrected.")
    content = corrected_transcript.choices[0].message.content
    print(corrected_transcript.choices[0].message.content)
    

# Systems settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("760x480")
app.title("Audio to Text")
app.grid

audio_file_path = customtkinter.StringVar(value='')
transcription_file_path = customtkinter.StringVar(value='')
output_file_name = customtkinter.StringVar(value='')

# Label for path to audio source file
label = customtkinter.CTkLabel(app, text="Select audio file for transcription", font=('Trebuchet MS', 18))
label.grid(row=0, column=0, padx=10, sticky="nw")

# Audio file source path
audio_file_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=audio_file_path, state="disabled")
audio_file_entry.grid(row=1, column=0, padx=10, sticky="nw")

# File browser button
select_source_btn = customtkinter.CTkButton(app, text="Select File", command=openFileBrowser)
select_source_btn.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

# Label for destination folder for transcribed file
destination_folder = customtkinter.CTkLabel(app, text="Selected folder for transcribed file", font=('Trebuchet MS', 18))
destination_folder.grid(row=3, column=0, padx=10, sticky="nw")

# Destination folder for transcribed file
selected_folder = customtkinter.CTkEntry(app, width=350, height=40, textvariable=transcription_file_path, state="disabled")
selected_folder.grid(row=4, column=0, padx=10, sticky="nw")

# Folder browser button
select_folder_btn =  customtkinter.CTkButton(app, text="Select folder", command=selectDestinationFolder)
select_folder_btn.grid(row=5, column=0, padx=10, pady=10, sticky="nw")

# Label for optional file name
output_file_name_label = customtkinter.CTkLabel(app, text="(Optional) Provide file name", font=('Trebuchet MS', 18))
output_file_name_label.grid(row=6, column=0, padx=10, sticky="nw")

# Optional output file name
output_file_name_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=output_file_name)
output_file_name_entry.grid(row=7, column=0, padx=10, sticky="nw")

# Transcribe button
transcribe_button = customtkinter.CTkButton(app, text="Transcribe", command=transcribeFile, state="disabled")
transcribe_button.grid(row=8, column=0, padx=10, pady=10, sticky="nw")

# Label for progress
progress_label = customtkinter.CTkLabel(app, text="Program output", font=('Trebuchet MS', 18))
progress_label.grid(row=0, column=1, padx=10, sticky="nw")

# Textbox
textbox = customtkinter.CTkTextbox(app, width=350, height=300)
textbox.grid(row=1, column=1, rowspan=7, padx=10, sticky="ne")

# Run app
app.mainloop()

