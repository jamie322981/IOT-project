import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import subprocess

# Initialize the RFID reader
reader = SimpleMFRC522()

# Dictionary to map RFID tags to video files
tag_to_video = {
    '3666501505': '/path/to/video1.mp4',
    '0987654321': '/path/to/video2.mp4'
    # Add more tag-video mappings as needed
}

try:
    while True:
        print("Hold a tag near the reader")
        tag_id, text = reader.read()

        # Convert the tag_id to a string (the keys in tag_to_video are strings)
        tag_id_str = str(tag_id)
        print(f"Tag ID: {tag_id_str}")

        if tag_id_str in tag_to_video:
            video_path = tag_to_video[tag_id_str]
            print(f"Video path to play: {video_path}")

            # Check if the video file exists
            try:
                with open(video_path, 'r') as f:
                    print(f"Found video file: {video_path}")
            except FileNotFoundError:
                print(f"Error: Video file not found: {video_path}")
                continue

            # Stop any currently playing video
            subprocess.call(['pkill', 'vlc'])

            # Play the video using VLC
            print(f"Playing video: {video_path}")
            subprocess.call(['vlc', '--fullscreen', '--play-and-exit', video_path])
        else:
            print("Unknown tag")

finally:
    GPIO.cleanup()