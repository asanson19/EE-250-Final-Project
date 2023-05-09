import datetime as dt
from datetime import datetime
import random
import time, grovepi
import socket

def get_brightness():
    """ Returns level of brightness.

    Works by reading the intensity of light from the GrovePi light sensor and assigning it a light level based on 2 threshold values.
    Light levels are \"Dark\", \"Mid\", and \"Bright\".

    Returns:
        brightness (string): The level of light intensity.
    """
    #light sensor input port
    light_input = 0

    grovepi.pinMode(light_input, "INPUT")

    #capture value
    input_value = grovepi.analogRead(light_input)

    #assigns light level
    if input_value < 50:
        brightness = "Dark"

    elif input_value in range(50, 300):
        brightness = "Mid"

    else:
        brightness = "Bright"

    return brightness

def morning():
    """Returns a bool for whether it is morning or not.

    Works by using the datetime library to get the current time and returning True if it is between 6am and 12pm.

    Returns:
        bool: Bool for whether it is morning or not.
    """
    # Get Time
    ts = dt.datetime.now().time()

    # Check if time
    mornStart = dt.time(6,0)
    mornEnd = dt.time(12,0)
    if ts >= mornStart and ts <= mornEnd:
        return True
    else:
        return False
        

def main():
    #Music file arrays

    sleepy = ["paperplanes.mp3.", "WelcometoWonderland.mp3.", "Halcyon.mp3.", "DosOruguitas.mp3.", "Nothing.mp3."]
    chill  = ["CruelSummer.mp3.", "Papercuts.mp3.", "CrashCourse.mp3.", "wemadeit.mp3.", "SummerNights.mp3."]
    energetic = ["Halcyon.mp3.", "StillIntoYou.mp3.", "NeverGonnaGiveYouUp.mp3.", "WeBuiltThisCity.mp3.", "VIRGOSGROOVE.mp3."]

    #Server Info
    HOST = "172.20.10.3"
    PORT = 1050

    #Create TCP server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Socket created")
        s.bind((HOST, PORT))
        print("Server binded")
        s.listen()
        print("Listening for client...")
        conn, addr = s.accept()
        print("Client accepted")
        while True:
                file = ""

                # Generate random file name based on light level and time
                brightness = get_brightness()
                if brightness == "Dark":
                    file = random.choice(sleepy)
                elif brightness == "Mid" and not morning():
                    file = random.choice(chill)
                else:
                    file = random.choice(energetic)
                conn.sendall(file.encode())
                time.sleep(0.5)

if __name__ == '__main__':
    main()
    

