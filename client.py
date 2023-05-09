import vlc
import socket

def play_song(filename):
    """Plays the inputed audiofile.

    Works by using the vlc library to open a VLC media player and playing the audio through the VLC media player application.

    Arguments:
        filename (string): Name of file to be played.
    """
    # State Variables
    is_opening = False
    is_playing = False

    # Open VLC and play
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(filename)
    media.get_mrl()
    player.set_media(media)
    player.play()

    # Player states
    good_states = [
    	"State.Playing", 
    	"State.NothingSpecial", 
    	"State.Opening"
    ]
    
    # State Variable Machine
    while str(player.get_state()) in good_states:
        if str(player.get_state()) == "State.Opening" and is_opening is False:
            print("Status: Loading")
            is_opening = True

        if str(player.get_state()) == "State.Playing" and is_playing is False:
            print("Status: Playing")
            is_playing = True

    # Finish playing when done
    print("Status: Finish")
    player.stop()

def main():
    # Server Info
    HOST = "172.20.10.3"
    PORT = 1051

    # TCP server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Socket created")
        s.connect((HOST, PORT))
        print("Server connected")
        while True:
            # Receive and process server message to get file name
            data = s.recv(1024)
            data = data.decode()
            print(data)
            data = data.split(".")
            print(data)
            url = data[-3] + ".mp3"
            print(url)
            play_song(url)

if __name__ == '__main__':
    main()