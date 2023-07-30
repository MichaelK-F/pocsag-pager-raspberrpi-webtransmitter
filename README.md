# Raspberry Pi transmitter for pocsag pagers with a simple web interface
## WARNING! This is not designed to be secure! Please only run this on your personal network and make sure it is not accessable from outside your network!

This is simple (and most definitly insecure) website built off rpitx (https://github.com/F5OEO/rpitx) to transmit messages from a Raspberry Pi (so far only tested on a raspberry pi 3) to pocsag pagers. 


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
cd /
sudo git clone https://github.com/MichaelK-F/pocsag-pager-raspberrpi-webtransmitter.git
```
##### Starting the server:
```
cd /pocsag-pager-raspberrpi-webtransmitter
python3 app.py
```





##### (Optional) set to automaticly start on boot:
```
crontab -e
```
You will get a message that looks like this:

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
@reboot python3 /pocsag-pager-raspberrpi-webtransmitter/app.py
```
Once it has been typed in press ```Ctrl + x``` then ```y``` then ```Enter```(Optional) set to automaticly start on boot:
To make the changes take effect run ```sudo reboot```



### Feel free to contribute to the repo



