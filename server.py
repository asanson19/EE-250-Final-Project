import datetime as dt
from datetime import datetime
import random
import time, grovepi
import pafy
import socket

def get_audio(url):
    video = pafy.new(url)
    best = video.getbestaudio()
    play_url = best.url

    # return play_url
    return best.url

def get_brightness():
    #light sensor code
    light_input = 0

    grovepi.pinMode(light_input, "INPUT")

    #capture value
    input_value = grovepi.analogRead(light_input)

    if input_value < 50:
        brightness = "Dark"

    elif input_value in range(50, 300):
        brightness = "Mid"

    else:
        brightness = "Bright"

    return brightness

def is_morning():
    ts = dt.datetime.now().time()

    mornStart = dt.time(6,0)
    mornEnd = dt.time(12,0)
    if ts >= mornStart and ts <= mornEnd:
        return True
    else:
        return False
        

def main():
    # YouTube URL Arrays

    # Dark
    # sleepy = ["https://www.youtube.com/watch?v=6EP4vlyYCko", 
    #         "https://www.youtube.com/watch?v=yjBbOn-g5bw",
    #         "https://www.youtube.com/watch?v=fp24dGKx678",
    #         "https://www.youtube.com/watch?v=qMuc20T4AC8",
    #         "https://www.youtube.com/watch?v=Nv3bQao8l3I"]
    # # Mid & NOT Morning
    # chill = ["https://www.youtube.com/watch?v=ic8j13piAhQ", 
    #         "https://www.youtube.com/watch?v=aSJ86cRB7zQ", 
    #         "https://www.youtube.com/watch?v=ke6xTSjnjBs", 
    #         "https://www.youtube.com/watch?v=X2Qz9W76m98", 
    #         "https://www.youtube.com/watch?v=QfEYyw7C2dE"]

    # # Mid & Morning || Bright
    # energetic = ["https://www.youtube.com/watch?v=fp24dGKx678", 
    #             "https://www.youtube.com/watch?v=Q_fmW9RPCqM", 
    #             "https://www.youtube.com/watch?v=3BFTio5296w", 
    #             "https://www.youtube.com/watch?v=NtM3jjLP7AE", 
    #             "https://www.youtube.com/watch?v=aD3HgrfjrAw"]

    sleepy = ["paperplanes.mp3"]
    chill  = ["paperplanes.mp3"]
    energetic = ["paperplanes.mp3"]

    #Server Info
    HOST = "172.20.10.3"
    PORT = 1050

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            url = ""
            brightness = get_brightness()
            if brightness == "Dark":
                url = random.choice(sleepy)
            elif brightness == "Mid" and not is_morning():
                url = random.choice(chill)
            else:
                url = random.choice(energetic)
            s.sendto(url.encode(), (HOST, PORT))
            time.sleep(0.5)

if __name__ == '__main__':
    main()
    

