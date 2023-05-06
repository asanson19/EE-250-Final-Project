import vlc
import socket

def play_song(url):
    is_opening = False
    is_playing = False

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    media.get_mrl()
    player.set_media(media)
    player.play()

    good_states = [
    	"State.Playing", 
    	"State.NothingSpecial", 
    	"State.Opening"
    ]
    
    while str(player.get_state()) in good_states:
        if str(player.get_state()) == "State.Opening" and is_opening is False:
            print("Status: Loading")
            is_opening = True

        if str(player.get_state()) == "State.Playing" and is_playing is False:
            print("Status: Playing")
            is_playing = True

    print("Status: Finish")
    player.stop()

def main():
    HOST = "172.20.10.3"
    PORT = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            url = s.recvfrom(1024)
            play_song(url.decode())

if __name__ == '__main__':
    main()