import time

import cv2
import pyttsx3

# Initialize the camera
print(">> Getting the camera ready >>")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

voice = 1
speed = 150
volume = 1.0


def change_voice():
    global voice
    print(f"Current voice - {voice}")
    new_voice = input("Please select 0(male) or 1(female): ")
    if 0 <= int(new_voice) <= 5:
        voice = int(new_voice)
        voice_out("This is the new voice")
    else:
        voice_out("Invalid input")


def change_speed():
    global speed
    print(f"Current speed - {speed/50}")
    new_speed = input("Please select your speed from 0-5: ")
    if 0 <= int(new_speed) <= 5:
        speed = int(new_speed)*50
        voice_out("This is the new speed")
    else:
        voice_out("Invalid input")


def change_volume():
    global volume
    print(f"Current volume - {volume*5}")
    new_volume = input("Please select your volume from 1-5: ")
    if 0 < int(new_volume) <= 5:
        volume = int(new_volume)/5
        voice_out("This is the new volume")
    else:
        voice_out("Invalid input")


def capture_image(name):

    for i in range(2):
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('frame', frame)

    # Check for user input to capture the image
    if cv2.waitKey(5000):
        # Save the captured image
        cv2.imwrite(f'{name}.jpg', frame)
        cv2.destroyAllWindows()
        return True
    else:
        return False


def capture_fake():
    voice_out("Currency detected, now scanning")

    for i in range(2):
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('frame', frame)

    # Check for user input to capture the image
    if cv2.waitKey(1):
        # Save the captured image
        cv2.imwrite(f'{"uv"}.jpg', frame)
        cv2.destroyAllWindows()
        return True
    else:
        return False


def voice_out(phrase):
    # Initialize the engine
    engine = pyttsx3.init()

    engine.setProperty('rate', speed)  # Change the rate to adjust the speed of speech

    # Set the voice properties (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)  # Change the index to switch voices

    engine.setProperty('volume', volume)  # Change the rate to adjust the volume of speech

    # Say the text
    engine.say(phrase)

    # Run the engine and wait for the speech to finish
    engine.runAndWait()
