# Build alexa

 Used different libraries like,
  speech_recognization : For recognize the voice.
  pyttsx3 : Used for convert text into speech.
  pywhatkit : Play a YouTube video,Perform a Google Search etc.
  datetime
  wikipedia
  pyjokes
**talk()** for returning response in voice.It used engine obj of pyttsx3 which use **say()** method to speak text.
**take_command()** for taking input from user and check particular word exist in command to search else it give error. If condition true, its call **run_alexa()** function and perform as per user instruction.
  
