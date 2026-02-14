#! /usr/bin/env bash

function bluer_sbc_joystick() {
    local task=${1:-validate}

    local function_name=bluer_sbc_joystick_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_sbc.joystick "$@"
}

bluer_ai_source_caller_suffix_path /joystick
