#!/bin/bash

# https://github.com/NVIDIA/nvidia-settings/blob/master/src/libXNVCtrl/NVCtrl.h

GAME_ID=440
# https://docs.mastercomfig.com/en/latest/os/linux/
# https://docs.mastercomfig.com
# https://developer.valvesoftware.com/wiki/Command_Line_Options#Steam_.28Windows.29
# obs.: se deixar no steam client (launch options do game) deveria funcionar tambem

LAUNCH_OPTIONS="SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0 -novid -nojoy -nosteamcontroller -nohltv -particles 1 -precachefontchars -noquicktime -nostartupsound"

sudo cpupower frequency-set -g performance
/usr/bin/nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'
# menu GUI: X Screen -> OpenGL Settings -> [Performance] -> Image Setttings 
/usr/bin/nvidia-settings -a '[screen:0]/OpenGLImageSettings=3'

echo "iniciando steam..."
export STEAM_RUNTIME_PREFER_HOST_LIBRARIES=0
steam -applaunch $GAME_ID $LAUNCH_OPTIONS
