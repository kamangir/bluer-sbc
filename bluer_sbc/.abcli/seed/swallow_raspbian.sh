#! /usr/bin/env bash

# internal function to bluer_ai_seed.
# seed is NOT local
function bluer_ai_seed_swallow_raspbian() {
    bluer_ai_seed add_repo repo=bluer-ugv
    seed="${seed}pip3 install -e .$delim_section"

    seed="${seed}sudo apt install -y libopenblas-dev$delim"

    seed="${seed}cd$delim"
    seed="${seed}wget https://github.com/nmilosev/pytorch-arm-builds/releases/download/v1.13.0/torch-1.13.0-cp39-cp39-linux_armv7l.whl$delim"
    seed="${seed}pip3 install torch-1.13.0-cp39-cp39-linux_armv7l.whl$delim_section"

    bluer_ai_seed add_repo repo=bluer-algo
    seed="${seed}pip3 install -e .$delim_section"
}
