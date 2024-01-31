import tiktoken

def count_tokens_in_text():
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    file_text = open("D:\Source\Courses\open-ai\Transcriptions\Voice Recorder from Microphone_text.txt").read()
    num_tokens = len(encoding.encode(file_text))
    print(num_tokens)

count_tokens_in_text()
