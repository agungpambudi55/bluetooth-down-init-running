# Created on Mar 2020
# Agung Pambudi <agung.pambudi5595@gmail.com>

sudo killall hciattach
if grep -a Zero /proc/device-tree/model; then
  raspi-gpio set 45 op dl
  sleep 1
  raspi-gpio set 45 op dh
else
  /opt/vc/bin/vcmailbox 0x38041 8 8 128 0
  sleep 1
  /opt/vc/bin/vcmailbox 0x38041 8 8 128 1
fi
sudo btuart