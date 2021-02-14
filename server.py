import socket
import pyperclip
import speech_recognition as sr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '' #the local ip of your computer
port = 1234
s.bind((ip, port))
s.listen(5)
runforthefirsttime = True
r = sr.Recognizer()

def listen():
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                if "play" in text:
                    return text
                else:
                    pass
            except:
                pass


while runforthefirsttime:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    runforthefirsttime = False

while True:
    if pyperclip.paste() == "l" or pyperclip.paste() == "listen":
        try:
            print("Hello!")
            message = listen()
            clientsocket.send(bytes(message, "utf-8"))
            pyperclip.copy("a")
            print(f"{message}")
        except:
            pass
    else:
        pass
