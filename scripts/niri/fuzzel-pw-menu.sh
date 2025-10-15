#!/bin/sh

choice=$(printf "Logout\nReboot\nShutdown\nLockdown" | fuzzel -w 10 -di)
case $choice in
Logout) niri msg action quit ;;
Reboot) reboot ;;
Shutdown) poweroff ;;
Lockdown) swaylock ;;
esac
