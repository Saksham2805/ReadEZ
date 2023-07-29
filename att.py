import pvleopard
from pydub import AudioSegment
# from pydub.utils import make_chunks

def crop_audio(input_mp3, start_time, end_time, cropped_mp3):
    audio = AudioSegment.from_mp3(input_mp3)

    # Calculate the start and end positions in milliseconds
    start_ms = start_time * 1000
    end_ms = end_time * 1000

    # Crop the audio segment
    cropped_audio = audio[start_ms:end_ms]

    # Export the cropped audio to a new MP3 file
    cropped_audio.export(cropped_mp3, format="mp3")
    return cropped_mp3
def audio_to_text(CROPPED_AUDIO):
    leopard = pvleopard.create(access_key="CBt7IGZqr4Ar4y29YdpwSRjvc3XczJUkOLF1+cpyywrbe7ZtjX2Hyg==")
    transcript, words = leopard.process_file(CROPPED_AUDIO)
    return transcript

if __name__ == "__main__":
    input_mp3_file = r"C:\Users\ASUS\Downloads\MBp1.mp3"
    output_mp3_file = "cropped.mp3"
    start_time_seconds = 40  # Start time in seconds
    end_time_seconds = 140    # End time in seconds
    CROPPED_AUDIO = crop_audio(input_mp3_file, start_time_seconds, end_time_seconds, output_mp3_file) 
    transcript = audio_to_text(CROPPED_AUDIO)   
    with open("transcript.txt", "w", encoding="utf-8") as file:
        file.write(transcript)