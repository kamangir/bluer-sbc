#! /usr/bin/env bash

function test_bluer_sbc_help() {
    local options=$1

    local module
    for module in \
        "@sbc" \
        \
        "@camera" \
        "@camera capture" \
        "@camera capture image" \
        "@camera capture video" \
        "@camera preview" \
        \
        "@joystick" \
        "@joystick install" \
        "@joystick validate" \
        \
        "@parts" \
        "@parts adjust" \
        "@parts cd" \
        "@parts edit" \
        "@parts open" \
        \
        "@sbc adafruit_rgb_matrix" \
        "@sbc adafruit_rgb_matrix validate" \
        \
        "@sbc hat" \
        "@sbc hat input" \
        "@sbc hat output" \
        "@sbc hat validate" \
        \
        "@sbc lepton" \
        "@sbc lepton capture" \
        "@sbc lepton preview" \
        \
        "@sbc pypi" \
        "@sbc pypi browse" \
        "@sbc pypi build" \
        "@sbc pypi install" \
        \
        "@sbc pytest" \
        \
        "@sbc rpi" \
        "@sbc rpi fake_display" \
        \
        "@sbc scroll_phat_hd" \
        "@sbc scroll_phat_hd validate" \
        \
        "@sbc sparkfun_top_phat" \
        "@sbc sparkfun_top_phat validate" \
        \
        "@sbc test" \
        "@sbc test list" \
        \
        "@sbc unicorn_16x16" \
        "@sbc unicorn_16x16 validate" \
        \
        "grove info" \
        "grove validate" \
        "grove validate oled_128x64" \
        \
        "bluer_sbc"; do
        bluer_ai_eval ,$options \
            bluer_ai_help $module
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done

    return 0
}
