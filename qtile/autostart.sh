#!/bin/bash

# echo "Autostart script executed" > ~/autostart.log
# picom -b 
killall libxcomposite
lxsession &
volumeicon &
picom --experimental-backend --config ~/.config/picom/picom.conf &
feh --bg-fill --randomize ~/Pictures/nordic-wallpapers &
