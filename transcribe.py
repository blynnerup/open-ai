# import whisper

# model = whisper.load_model("base")

# res = model.transcribe("Dansk.m4a")
# print(res)

import customtkinter

def updateText():
    textbox.configure(state="normal")
    textbox.insert('end', "sometext")
    textbox.configure(state="disabled")

def deleteText():
    textbox.configure(state="normal")
    textbox.delete(0.0, 'end')
    textbox.configure(state="disabled")

# Systems settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("760x480")
app.title("Audio to Text")

textbox = customtkinter.CTkTextbox(app, width=350, height=300, state="disabled")
# textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
# textbox.configure(state="disabled")  # configure textbox to be read-only
textbox.pack(padx=10, pady=10, side="top", anchor="nw")

transcribe_button = customtkinter.CTkButton(app, text="Transcribe", command=updateText)
transcribe_button.pack(padx=10, pady=10, side="top", anchor="nw")

transcribe_button_delete = customtkinter.CTkButton(app, text="Transcribe", command=deleteText)
transcribe_button_delete.pack(padx=10, pady=10, side="top", anchor="nw")
# Run app
app.mainloop()
