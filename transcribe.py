import sys
sys.path.insert(1, '../mlx-examples/whisper/')

import whisper
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio file')
    parser.add_argument('-f', '--file', type=str, help='The file to transcribe')
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("audio file not found: ", args.file)
        exit()

    result = whisper.transcribe(model="base", audio=args.file, fp16=False)
    print(result["text"])

if __name__ == '__main__':
    main()