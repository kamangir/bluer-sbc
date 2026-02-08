#! /usr/bin/env bash

function bluer_sbc_joystick_install() {
    if [[ "$abcli_is_rpi" == true ]]; then
        sudo apt update
        sudo apt install -y joystick
        sudo apt install -y python3-pygame
    fi
}
