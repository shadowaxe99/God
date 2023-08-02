```python
import speech_recognition as sr

# Shared variables
voiceCommandHistory = []

# Voice command schema
VoiceCommandSchema = {
    "command": "",
    "timestamp": "",
    "processed": False
}

def processVoiceCommand():
    """
    Function to process voice commands from the user.
    """
    # Initialize recognizer
    r = sr.Recognizer()

    # Record audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = r.recognize_google(audio)
        print(f"You said: {command}\n")

        # Save command to history
        voiceCommand = VoiceCommandSchema.copy()
        voiceCommand["command"] = command
        voiceCommandHistory.append(voiceCommand)

        # TODO: Add command processing logic here

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return command
```