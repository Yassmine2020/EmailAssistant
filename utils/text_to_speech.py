import io
from pydub import AudioSegment
import elevenlabs
from elevenlabs import generate
import base64

def text_to_speech(text):
    # Checking if the Arabic answer is non-empty
    if text:
        # Setting the API key for Eleven Labs TTS service
        elevenlabs.set_api_key("8baca584c9025aa9c7f85e0e4e8ae0c1")
        # Generating audio from the Arabic answer using Eleven Labs TTS
        audio = generate(
            text=text,
            voice="Daniel",  # Choosing the voice for the generated audio
            model='eleven_multilingual_v2'  # Choosing the TTS model
        )
    else:
        print("▶️ empty ar_answer")

    # Converting the generated audio from bytes to an AudioSegment object
    audio = AudioSegment.from_file(io.BytesIO(audio), format="mp3")

    # Exporting the audio to an MP3 file named "output.mp3"
    audio.export("output.mp3", format="mp3")

    return audio