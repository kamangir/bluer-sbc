#! /usr/bin/env bash

function bluer_sbc_joystick_validate() {
    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_warning "only works on rpi."
        return
    fi

    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)
    local use_python=$(bluer_ai_option_int "$options" python 1)

    [[ "$do_install" == 1 ]] &&
        bluer_sbc_joystick_install

    if [[ "$use_python" == 1 ]]; then
        bluer_ai_eval - \
            python3 -m \
            bluer_sbc.joystick \
            validate \
            "$@"
    else
        ls /dev/input/js*
        bluer_ai_log "⬆️ should read like \"/dev/input/js0\"."

        bluer_ai_log "move the joystick sticks and press buttons."
        bluer_ai_eval - \
            sudo jstest /dev/input/js0
    fi
}
