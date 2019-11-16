#!/bin/sh

terminal_wm_class="ActiveDesktop"
terminal_exec="python3 /home/afoninz/projects/longway/active.py https://google.com"

# no terminal started, so start one
if [ -z "`wmctrl -lx | grep ActiveDesktop`" ]; then
    $terminal_exec &
else
    wmctrl -x -a $terminal_wm_class
fi;
