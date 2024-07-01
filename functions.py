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

# Function to read the config file
def read_config():
    config = {}
    try:
        with open("config.txt", "r") as file:
            for line in file:
                if '=' in line:
                    name, value = line.strip().split("=")
                    config[name.strip()] = value.strip()
    except FileNotFoundError:
        print("Config file not found. Using default settings.")
    return config

# Function to get config value by name
def get_config_value(config, name, default=None, value_type=str):
    return value_type(config.get(name, default))
