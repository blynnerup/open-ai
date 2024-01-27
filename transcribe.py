import whisper

model = whisper.load_model("base")

res = model.transcribe("Dansk.m4a")
print(res)