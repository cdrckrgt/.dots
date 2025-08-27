# /etc/skel/.bash_profile

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.
if [[ -f ~/.bashrc ]] ; then
	. ~/.bashrc
fi

# the following gets executed if we're logging in to tty1 (so no greetd, 
# no tuigreet). 
# for the tuigreet login, see /usr/share/wayland-sessions/hyperland.desktop

# Ensure XDG_RUNTIME_DIR is set
if test -z "$XDG_RUNTIME_DIR"; then
    export XDG_RUNTIME_DIR=$(mktemp -d /tmp/$(id -u)-runtime-dir.XXX)
fi

[ "$(tty)" = "/dev/tty1" ] && ! pidof -s Hyprland >/dev/null 2>&1 && exec "$HOME/.config/hypr/start.sh"
