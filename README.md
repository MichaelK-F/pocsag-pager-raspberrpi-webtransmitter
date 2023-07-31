# Raspberry Pi transmitter for pocsag pagers with a simple web interface
## WARNING! This is not designed to be secure! Please only run this on your personal network and make sure it is not accessable from outside your network!

This is simple (and most definitly insecure) website built off rpitx (https://github.com/F5OEO/rpitx) to transmit messages from a Raspberry Pi (so far only tested on a raspberry pi 3 with 64 bit Raspberry Pi OS) to pocsag pagers. 


### How to set up:
#### Prerequisites:



##### Install python, git, and install flask (web server):
```
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install flask
```
##### Copy this repository to the device:
```
cd ~
sudo git clone https://github.com/MichaelK-F/pocsag-pager-raspberrpi-webtransmitter.git
```

##### Starting the server:
```
cd ~/pocsag-pager-raspberrpi-webtransmitter
python3 app.py
```





##### (Optional) set to automaticly start on boot:
```
crontab -e
```
You will get a message that looks like this if you have never run crontab before:

```
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.tiny
  3. /bin/ed

Choose 1-3 [1]:
```
Unless you know exactly what you are doing, select ```1```
Once that is done you will need to go to the bottom of the file and type in this:
```
@reboot python3 ~/pocsag-pager-raspberrpi-webtransmitter/app.py
```
Once it has been typed in press ```Ctrl + x``` then ```y``` then ```Enter```(Optional) set to automaticly start on boot:
To make the changes take effect run ```sudo reboot```
Once this has been done, the server will automaticly start on boot.

#### Connecting the antena
Plug a wire on GPIO 4, means Pin 7 of the GPIO header. This acts as the antenna. The optimal length of the wire depends the frequency you want to transmit on, but it works with a few centimeters for local testing.

#### Accessing the website
To access the website go to ```http://youripadress:8080```
To find your ip adress type in ```hostname -I```




### Feel free to contribute to the repo

### Credits:
Actual program that sends the pocsag messages: https://github.com/F5OEO/rpitx
Icon: Pager by iconfield from Noun Project (CC BY 3.0)

