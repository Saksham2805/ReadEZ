from gtts import gTTS
import os

def text_to_audio(input_file, language='en', output_file='output.mp3'):
    """
    Convert text from a file to audio using Google Text-to-Speech (gTTS) library.

    Parameters:
        input_file (str): The path to the input text file.
        language (str): The language code (default is 'en' for English).
        output_file (str): The name of the output audio file (default is 'output.mp3').

    Returns:
        None
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ')

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    print(f"Text from {input_file} converted to audio and saved as {output_file}")

if __name__ == "__main__":
    input_text_file = r"C:\Users\ASUS\transcript.txt"
    text_to_audio(input_text_file)
