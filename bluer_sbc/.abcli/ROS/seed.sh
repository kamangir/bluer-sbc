#! /usr/bin/env bash

# internal function to bluer_ai_seed.
# seed is NOT local
function bluer_ai_seed_headless_ubuntu_rpi() {
    local target=$1

    seed="${seed}sudo systemctl disable unattended-upgrades$delim"
    seed="${seed}sudo apt remove unattended-upgrades$delim"
    seed="${seed}sudo apt update && sudo apt upgrade$delim_section"

    seed="${seed}sudo mkdir -p /etc/systemd/system/getty@tty1.service.d$delim"
    seed="$seed$(bluer_ai_seed add_file $abcli_path_git/bluer-sbc/bluer_sbc/ROS/override.conf /etc/systemd/system/getty@tty1.service.d/override.conf)$delim"
    seed="${seed}sudo systemctl daemon-reexec$delim"
    seed="${seed}sudo systemctl restart getty@tty1$delim_section"

}
