#! /usr/bin/env bash

function bluer_sbc_joystick_validate() {
    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_warning "only works on rpi."
        return
    fi

    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)

    [[ "$do_install" == 1 ]] &&
        bluer_sbc_joystick_install

    ls /dev/input/js*
    bluer_ai_log "⬆️ should read like \"/dev/input/js0\"."

    bluer_ai_log "move the joystick sticks and press buttons."
    bluer_ai_eval - \
        sudo jstest /dev/input/js0
}
