import socket
import time
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '' #host machine's local ip
port = 1234
s.connect((ip, port))


while True:
    time.sleep(1)
    msg = s.recv(1024)
    message = msg.decode("utf-8")
    if "play" in message:
        message.replace("play", "")
        results = YoutubeSearch(f'{message}', max_results=1).to_dict()
        url1 = results[0]['url_suffix']
        url = " https://youtube.com" + url1
        p = subprocess.Popen(
        "mpv" + url + " --no-video --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
        shell=True)
        title = results[0]['title']
        print(f"Playing {title}")


