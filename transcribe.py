import sys
sys.path.insert(1, './whisper-mlx/')
#sys.path.append('./whisper-mlx/whisper/')


import whisper
import os

#speech_file = "./NovemberBoarddMeeting.m4a"
#speech_file = "~dragones/.cache/whisper/alice.mp3"
#text = whisper.transcribe(speech_file)["text"]
#print(text)

audio_file = os.path.join(
    os.path.expanduser("~"),
#    ".cache/whisper/alice.mp3",
    "Code/mlx-examples/whisper/NovemberBoardMeeting.m4a",
)

# print current folder name
# print(os.getcwd())

# print out all files in current folder
# print(os.listdir(os.getcwd()))

if not os.path.exists(audio_file):
    print("audio file not found: ", audio_file)
    exit()

#model = whisper.load_model("small")
#result = whisper.transcribe(audio_file, fp16=False)
result = whisper.transcribe(model="tiny", audio=audio_file, fp16=False)
print(result["text"])

# Save as a TXT file with hard line breaks
#output_directory = "./transcripts/"

# check if output_directory exists.  if not, create it
#if not os.path.exists(output_directory):
#    os.makedirs(output_directory)

#txt_writer = get_writer("txt", output_directory)
#txt_writer(result, "NovemberBoardMeeting.m4a")
