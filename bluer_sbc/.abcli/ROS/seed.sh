#! /usr/bin/env bash

# internal function to bluer_ai_seed.
# seed is NOT local
function bluer_ai_seed_headless_ubuntu_rpi() {
    local target=$1

    seed="${seed}sudo systemctl disable unattended-upgrades$delim"
    seed="${seed}sudo apt remove unattended-upgrades$delim"
    seed="${seed}sudo apt update$delim"
    seed="${seed}sudo apt upgrade$delim"
    seed="${seed}sudo apt install -y python3-venv$delim_section"

    seed="${seed}sudo mkdir -p /etc/systemd/system/getty@tty1.service.d$delim"
    seed="$seed$(bluer_ai_seed add_file $abcli_path_git/bluer-sbc/bluer_sbc/ROS/override.conf /etc/systemd/system/getty@tty1.service.d/override.conf)$delim"
    seed="${seed}sudo systemctl daemon-reexec$delim"
    seed="${seed}sudo systemctl restart getty@tty1$delim_section"

    bluer_ai_seed add_ssh_key

    bluer_ai_seed add_repo

    seed="${seed}touch ~/storage/temp/ignore/headless$delim_section"

    bluer_ai_seed add_bluer_ai_env

    seed="${seed}pip install --upgrade pip --no-input$delim"
    seed="${seed}pip3 install -e .$delim_section"

}
