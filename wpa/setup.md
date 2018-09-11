# setup

## ssh

flash 2018-06-27-raspbian-stretch.zip

put ssh.txt and wpa_supplicant.conf on boot.

```sh
$ ssh pi@raspberry.local

interface eth0
static ip_address=172.20.10.{num}/24
static routers=172.20.10.1
```

A USB
B センサー

lora_GW : 172.20.10.2
A1 : 172.20.10.10
A2 : 172.20.10.11
A3 : 172.20.10.12
B1 : 172.20.10.5
B2 : 172.20.10.6 人感センサ

繋がらない時
iPhoneの共有をON/OFFしてみる。

## git

git clone https://github.com/suzu6/acerola.git
sudo chmod 755 /home/pi/acerola/raspi/*

# change each device
sed -e 's/A1/A3/' /home/pi/acerola/raspi/usb_power_controler.py > /home/pi/acerola/raspi/usb_power_controler.py

## usb

```sh
# get libraly
sudo apt-get install libusb-dev
wget http://www.gniibe.org/oitoite/ac-power-control-by-USB-hub/hub-ctrl.c
gcc -O2 hub-ctrl.c -o hub-ctrl-armhf-static -lusb -static
sudo cp hub-ctrl-armhf-static /usr/local/bin/hub-ctrl


# install firebase
sudo pip install firebase-admin
sudo pip install python-firebase


# test
python /home/pi/acerola/raspi/usb_power_controler.py

```

sudo crontab -e

@reboot    /home/pi/acerola/raspi/run_usb.sh