import imageio
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from PIL import Image
import os

# Specify the path to the ImageMagick binary
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# List of image file paths with their durations (in seconds) and corresponding text
image_files_with_durations_and_texts = [
    ("image1.jpg", 5, "This is Image 1"),
    ("image2.jpg", 5, "This is Image 2"),
    ("image3.jpg", 5, "This is Image 3"),
]

# Resize all images to the same size
def resize_images(image_paths, size=(640, 480)):
    resized_images = []
    for path, duration, text in image_paths:
        resized_path = f"resized_{path}"
        if os.path.exists(resized_path):
            resized_images.append((resized_path, duration, text))
            continue
        img = Image.open(path)
        img_resized = img.resize(size)
        img_resized.save(resized_path)
        resized_images.append((resized_path, duration, text))
    return resized_images

# Resize images
image_files_with_durations_and_texts = resize_images(image_files_with_durations_and_texts)

# Create individual clips for each image with the specified duration and add text
clips = []
for image_path, duration, text in image_files_with_durations_and_texts:
    image_clip = ImageSequenceClip([image_path], durations=[duration])
    text_clip = TextClip(text, fontsize=24, color='white').set_duration(duration).set_position('center')
    composite_clip = CompositeVideoClip([image_clip, text_clip])
    clips.append(composite_clip)

# Concatenate all the image clips
video_clip = concatenate_videoclips(clips, method="compose")

# Audio file path
audio_file = "audio.mp3"

# Load the audio file
audio_clip = AudioFileClip(audio_file)

# Set the audio to the video
video_with_audio = video_clip.set_audio(audio_clip)

# Set the duration of the video to match the audio
video_with_audio = video_with_audio.set_duration(audio_clip.duration)

# Export the final video
video_with_audio.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac", fps=24)