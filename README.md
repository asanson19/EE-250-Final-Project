# EE-250-Final-Project

Group Members:
1. Richard Ochoa Jr.
2. Ana Sanson

Demo
https://drive.google.com/file/d/16qDXDTIcqbdzC4QLjuXCHyf5e6dJFQqr/view?usp=share_link

Instructions
1. Download all the files in the Server and Client directories on the respective devices.
2. On the client's terminal, run the following command:
    $ pip install -r requirements.txt
3. On the server's terminal, ensure that the GrovePi software is downloaded. If not, run the following commands:
    $ sudo apt-get install curl #in case it’s not there
    $ sudo curl -kL dexterindustries.com/update_grovepi | bash
    $ cd ~/Dexter/GrovePi/Firmware
    $ ./firmware_update.sh #getting errors with avrdude? check here
    $ sudo reboot # rebooting will drop the ssh connection
    # wait a moment and reconnect via SSH
    $ cd ~/Dexter/GrovePi/Software/Python
    $ python grove_firmware_version_check.py
4. Ensure the VLC Media Player is downloaded on the client's device.
5. Run the respective python files with the server being run first. Enjoy listening!

External Libraries
python-vlc: A library used to interact with the VLC Media Player application.