import io
from pydub import AudioSegment
import elevenlabs
from elevenlabs import generate
import base64

def text_to_speech(text):
    if text:
        try:
            # Generate the audio using Eleven Labs TTS (same as before)
            elevenlabs.set_api_key("8baca584c9025aa9c7f85e0e4e8ae0c1")
            audio = generate(text=text, voice="Daniel", model='eleven_multilingual_v2')
        except Exception as e:
            print(f"An error occurred during audio generation: {e}")
            return None

        try:
            # Save the MP3 audio data to a file
            mp3_path = 'output.mp3'
            with open(mp3_path, 'wb') as audio_file:
                audio_file.write(audio)
            return  str(audio)

        except Exception as e:
            print(f"An error occurred during audio file handling: {e}")