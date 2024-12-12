# import speech_recognition as sr
# from os import path


from os import getenv
from dotenv import load_dotenv
from openai import OpenAI


# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "./audio/recording.wav")


load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)


# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file


try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`

    f = open("output.txt", "a")
#     f.write(r.recognize_google(audio))


    audio_file = open("./audio/recording.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)
    f.write(transcription.text)
    f.write("\n")
    f.close()
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")

# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


except:
    print("ERROR")
