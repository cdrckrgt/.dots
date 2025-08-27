#!/bin/sh

let loop=0
while true; do
	if [[ $loop%300 -eq 0 ]]; then
		weather="""$(curl 'https://wttr.in?format=%m\n&u')"""
		let loop=0
	fi
    bat="""$(acpi -b | awk -F', ' '{print $2}' | tr -d ' ')"""
	xsetroot -name " $weather | $(date '+%b %d %a') | $(date '+%H:%M') | $bat "
	let loop=$loop+1
	sleep 1
done
