import os
import argparse
import assemblyai as aai

def writeFile(transcript, args):
    # Create the transcript filename
    base_name = transcript.id
    transcript_filename = f"./transcripts/{base_name}.txt"
    
    # Write the transcript to the file and only file exists create a numbered version
    if os.path.exists(transcript_filename):
        i = 1
        while os.path.exists(transcript_filename):
            transcript_filename = f"./transcripts/{base_name}_{i}.txt"
            i += 1

    with open(transcript_filename, 'w') as f:
        for paragraph in transcript.get_paragraphs():
            f.write(paragraph.text)
            # line break after every paragraph
            f.write("\n\n")

def transcribe(filename: str) -> aai.Transcript:
    config = aai.TranscriptionConfig(
        format_text=True
    )
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(filename)
    return transcript

def main():
    parser = argparse.ArgumentParser(description='Generate meeting transcript, summary, action items')
    parser.add_argument('-f', '--file', type=str, help='The file to process')
    parser.add_argument('-id', '--transcriptId', type=str, help='Assembly.AI transcriptId')
    args = parser.parse_args()

    # check if config vars present
    if not os.environ['ASSEMBLYAI_API_KEY']:
        print('Please make sure all environment variables set')
        return

    # transcribe to file
    transcript = None
    if(args.transcriptId):
        try:
            transcript = aai.Transcript.get_by_id(args.transcriptId)
        except Exception as e:
            print(f"An error occurred while looking up the transcript: {e}")
            return
    else:
        transcript = transcribe(args.file)

    writeFile(transcript, args)

    # summarize to stdout
    result = transcript.lemur.summarize()
    print(result.response)

    # actions to stdout
    result = transcript.lemur.action_items()
    print(result.response)

if __name__ == '__main__':
    main()