PiMusicPlayer, Made by: Benjir

INSTALLATION GUIDE(ON THE PI):

1.Run "sudo apt install mpv"
2.Install these libraries with "sudo pip3 install <name>": requests, youtube-search, bs4
3.Set the local ip of the host machine in "server.py"
4.(OPTIONAL) You can make it run on boot with crontab or any way you like.

INSTALLATION GUIDE(ON THE PC):
1.Install python3 if you didn't already have it
2.Install these libraries with "pip install <name>": SpeechRecognition, pyperclip
3.Check your computer's local ip with "ipconfig" in the command prompt.
4.Type your computer's local ip to the "ip" variable on line 6.


USE GUIDE:

1.Start server.py on your pc, and then run client.py on your pi.
2.On your server.py (I suggest you to run this on your main pc) copy "l" or "listen" and then say "play" and the music you want to listen to
3.Your text appears in the console, and shows you what the computer understood
4.It plays the music you wanted. (You can't really stop it, I'll make a function for it later)