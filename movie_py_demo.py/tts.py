from tortoise.api import TextToSpeech
from tortoise.utils.audio import save_wav

# Initialize the Tortoise TTS model
tts = TextToSpeech()

# Define the text to synthesize
text = "Hello! This is a demonstration of Tortoise Text-to-Speech."

# Generate speech from text
voice_samples, conditioning_latents = None, None  # Use default voice
speech = tts.tts(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents)

# Save the generated speech to a WAV file
output_path = "output_speech.wav"
save_wav(speech, output_path)

print(f"Speech synthesis complete. Audio saved to {output_path}.")