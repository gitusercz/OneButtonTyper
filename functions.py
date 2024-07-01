import pygame
import os

def play_wav(file_name):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Define the path to the WAV file
    wav_file_path = os.path.join('resources', file_name)

    # Check if the file exists
    if not os.path.isfile(wav_file_path):
        print(f"File '{file_name}' not found in the 'resources' folder.")
        return

    # Load the WAV file
    pygame.mixer.music.load(wav_file_path)

    # Play the WAV file
    pygame.mixer.music.play()

    # Keep the script running long enough to hear the audio
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
if __name__ == "__main__":
    play_wav('your_audio_file.wav')  # Replace with the name of your WAV file
