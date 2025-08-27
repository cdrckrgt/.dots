# connecting to travel wifi automatically on startup
# this file gets called by hyprland.conf, and is run with 
#   exec-once ~/.scripts/travelwifi/sh
# TODO: extend this to connect to any one of multiple trusted wifis

# kill existing wpa_supplicants, if they exist
pidof wpa_supplicant >/dev/null
if [[ $? -ne 1 ]] ; then
    echo 'killing running wpa_supplicant...'
    sudo killall wpa_supplicant 1>/dev/null 2>/dev/null
    sleep 1
fi
#
# unblock wifi if it's soft blocked at startup
rfkill unblock wlan

# connect to wifi
sudo wpa_supplicant -B -i wlp130s0 -c /etc/wpa_supplicant/wpa_supplicant-travelwifi.conf &
