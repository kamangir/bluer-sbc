#! /usr/bin/env bash

function bluer_sbc_action_git_before_push() {
    bluer_sbc build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "current" ]] &&
        return 0

    bluer_sbc pypi build
}
