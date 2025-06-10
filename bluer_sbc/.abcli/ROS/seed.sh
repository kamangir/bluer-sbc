#! /usr/bin/env bash

# internal function to bluer_ai_seed.
# seed is NOT local
function bluer_ai_seed_headless_ubuntu_rpi() {
    local target=$1

    seed="${seed}sudo systemctl disable unattended-upgrades$delim"
    seed="${seed}sudo apt remove unattended-upgrades$delim"
    seed="${seed}sudo apt update && sudo apt upgrade$delim_section"

}
