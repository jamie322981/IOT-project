import os
import time
from pynfc import Nfc, Desfire

# Function to play a video using omxplayer
def play_video(video_path):
    os.system(f'omxplayer -b {video_path}')

# Dictionary mapping NFC tag IDs to video file paths
tag_to_video = {
    '3666501505': '/home/walkintheparq/Documents/NFC/video1.mp4',
    '1914068864': '/home/walkintheparq/Documents/NFC/video1.mp4',
    # Add more mappings here
}

# Verify and initialize the NFC reader
device_path = "/dev/bus/usb/001/011"  # Update based on dmesg output
try:
    if not os.path.exists(device_path):
        raise FileNotFoundError(f"Device path {device_path} not found.")
    nfc = Nfc(f"pn532_uart:{device_path}:115200")
except Exception as e:
    print(f"Error initializing NFC reader: {e}")
    exit(1)

# Main loop to continuously poll for NFC tags
try:
    while True:
        # Poll for an NFC tag
        target = nfc.poll()
        
        if target:
            tag_id = target.uid.hex()
            print(f"NFC Tag detected: {tag_id}")
            
            # Look up the video for the detected tag ID
            video_path = tag_to_video.get(tag_id)
            
            if video_path:
                print(f"Playing video: {video_path}")
                play_video(video_path)
            else:
                print("No video mapped for this NFC tag.")
        
        # Sleep for a short period to avoid excessive polling
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Program terminated by user.")
except Exception as e:
    print(f"Unexpected error: {e}")