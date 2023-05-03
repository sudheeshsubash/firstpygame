import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        command = r.recognize_google(audio)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    
    return command

# call the voice command function
def say(command):
     # respond to the voice command
        if "hello" in command:
            engine.say("Hello amal")
        elif "good morning" in command:
            engine.say("good morning, happy nice day")
        elif "goodbye" in command:
            engine.say("Goodbye!")
            global run
            run = False
        else:
            engine.say("Sorry, I didn't understand that command.")

        engine.runAndWait()



if __name__ == '__main__':
    run = True
    while run:
        
        command = voice_command()
        say(command)