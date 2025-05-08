import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import openai

openai.api_key = "*get opean ai key"

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for user input and returns the text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) # adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def get_response(prompt):
    """Gets a response from OpenAI's API."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable engine
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I encountered an error."

def main():
    """Main function to run the assistant."""
    speak("Hello! I'm your personal assistant. How can I help you?")

    while True:
        query = listen()

        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        elif "date" in query:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {date}")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "YOUR_MUSIC_DIRECTORY" #replace with your music directory.
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0])) #plays the first song.
            else:
                speak("No music files found in the specified directory.")
        elif "what is" in query or "who is" in query:
            response = get_response(query)
            speak(response)
        elif "exit" in query or "quit" in query or "stop" in query or "goodbye" in query:
            speak("Goodbye!")
            break
        elif query: #if query is not empty, and none of the above.
            response = get_response(query)
            speak(response)

if __name__ == "__main__":
    main()