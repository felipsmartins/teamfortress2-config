#!/bin/bash

# https://github.com/NVIDIA/nvidia-settings/blob/master/src/libXNVCtrl/NVCtrl.h


sudo cpupower frequency-set -g performance
/usr/bin/nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'

# menu GUI: X Screen -> OpenGL Settings -> [Performance] -> Image Setttings 
/usr/bin/nvidia-settings -a '[screen:0]/OpenGLImageSettings=3'

echo "iniciando steam..."
# export STEAM_RUNTIME_PREFER_HOST_LIBRARIES=0
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia steam