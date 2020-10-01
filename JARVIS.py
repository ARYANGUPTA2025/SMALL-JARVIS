import os
import pyttsx3
import speech_recognition as sr

#    code to change the voice of the pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

choices1 = ["chrome", "firefox", "notepad", "control panel", "explorer"]
choices2 = ["youtube", "reddit", "instagram", "facebook", "gmail", "twitter", "google", "whatsapp"]
browser = ["chrome", "firefox"]


def takecmd():
    To take vouice input & convert it into Text String

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening... ")
        r.non_speaking_duration = 0.1
        r.pause_threshold = 0.1
        r.energy_threshold = 300
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"{query}\n")
            return query
        
        except Exception as e:
            print(e)
            print(" Say that again Please")
            return "None"

def Output(A):
    print(A)
    engine.say(A)
    


Output("\n\nTHIS CHAT BOT CAN HELP YOU OPEN BASIC APPLICATIONS\nFor ex: 'open instagram' or 'start firefox'\n'Stop or Exit to exit the chatbot ")
while True:
    A = 0
    # _choice = input("\nHey, What can i help you with? : ")
    Output("\nHey, What can i help you with? : ")
    _choice = takecmd()
    _choice = _choice.lower()
    

    for i in choices1:
        if i in _choice:
            os.system("start " + i)
            Output("Sure, opening " + i)
            A=1
            break

    if A==0:
        for i in choices2:         
            if (i in _choice) or (_choice in i):
                # gm = input("Sure, In which browser you want me to open : ")
                Output("Sure! In which browser you want me to open ? : ")
                
                gm = takecmd()
                gm = gm.lower()

                for j in browser:
                    if j in gm:
                        Output("Sure opening " + i + " in " + gm + "browser")
                        os.system("start " + j + " " + i + ".com")
                        A=1
                        break

    if A==0:
        #windows media player done
        if "wmplayer" in _choice or "musicplayer" in _choice or "start music player" in _choice or "windows media player" in _choice:
            Output("Sure, opening windows media player")
            os.system("start wmplayer")
            A=1

        #control panel done
        elif ("settings" in _choice or "control pannel" in _choice or "control panel" in _choice):
            Output("Sure, opening control panel.")
            os.system("start control panel")
            A=1

        #some easter eggs done
        elif ("fire" in _choice):
            Output("Do you want me to open firefox ?")
            com_fire = takecmd()

            if (com_fire == 'yes') or (com_fire == 'y'):
                Output("OK")
                os.system("start firefox")
                Output("Anything else i can do for you, let me know.")
                A=1
            else:
                Output("OK!")
                A=1

        elif (("i" in _choice and "am feeling" in _choice) and ("sad" in _choice)):
            Output("\nDont be sad \n Everything will be fine")
            Output("Let me play some funny videos for you to watch")
            os.system("start chrome https://youtu.be/Zr3PukaVXFo")
            Output("Here you go, thank me later")
            A=1

        elif (("i" in _choice and "am feeling" in _choice) and ("happy" in _choice or "great" in _choice)):
            Output("\nThats great, i am happy to hear that :D \n Here is a song i want you to listen, it will make you feel energetic")
            os.system("start chrome https://www.youtube.com/watch?v=j8GSRFS-8tc")
            Output("Enjoy")
            A=1

        elif ("hello" in _choice or "hi" in _choice or "namastey" in _choice):
            Output("Hello, Dear User, I am your personal 'chatbot', Chat with me and tell me what to do for you :D")
            A=1
    
        elif ("thanks" in _choice or "thank you" in _choice or "thankyou" in _choice):
            Output("Your Welcome, My friend")
            A=1

        #exit done
        elif ("close" in _choice or "exit" in _choice or "stop" in _choice or "bye" in _choice):
            Output("Sure!, Thank you for using chatbot :D\nPROGRAM CREATED BY\n  RANBEER DHANRAJ GUPTA")
            break

        elif("love you" in _choice):
            Output("I love you too..., Stay happy, Take Care")
    if A==0:
        Output("Sorry Sir, I can not understand !!!")
