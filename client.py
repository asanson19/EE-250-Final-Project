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
    PORT = 1050

    # TCP server
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((HOST, PORT))
        while True:
                # Receive and process server message to get file name
                data = s.recv(1024)
                data = data.split(".")
                url = data[-2] + ".mp3"
                play_song(url.decode())

if __name__ == '__main__':
    main()