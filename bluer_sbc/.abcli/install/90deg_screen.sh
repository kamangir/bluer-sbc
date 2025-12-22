#! /usr/bin/env bash

function bluer_ai_install_bluer_sbc_screen_rotation() {
    bluer_ai_log "@sbc: screen rotation"

    sudo apt install -y alsa-utils wlr-randr
}

if [[ ! -z "$BLUER_SBC_SCREEN_ROTATION" ]]; then
    bluer_ai_install_module bluer_sbc_90deg_screen 101

    bluer_ai_log "@sbc: screen rotation: $BLUER_SBC_SCREEN_ROTATION"
    wlr-randr --output HDMI-A-1 --transform $BLUER_SBC_SCREEN_ROTATION
fi
