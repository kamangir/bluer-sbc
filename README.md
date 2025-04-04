# 🌀 bluer-sbc

🌀 `bluer-sbc` is a [`bluer-ai`](https://github.com/kamangir/bluer-ai) plugin for edge computing on [single board computers](https://github.com/kamangir/blue-bracket). 

```bash
pip install bluer_sbc

# @env dot list
@env dot cp <env-name> local
```

|   |   |   |   |
| --- | --- | --- | --- |
| [![image](https://github.com/kamangir/blue-bracket/raw/main/images/blue3-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/blue3.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/chenar-grove-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/chenar-grove.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/cube-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/cube.md) | [![image](https://github.com/kamangir/blue-bracket/raw/main/images/eye_nano-1.jpg)](https://github.com/kamangir/blue-bracket/blob/main/designs/eye_nano.md) |

```mermaid
graph LR
    camera["@sbc<br>&lt;camera&gt;<br>capture|preview<br>image|video"]

    hardware_validate["@sbc<br>&lt;hardware&gt;<br>validate<br>&lt;options&gt;"]

    session_start["@sbc<br>session<br>start"]

    object["📂 object"]:::folder
    camera_hardware["👁️‍🗨️ camera"]:::folder
    hardware["🖱️ hardware"]:::folder
    UI["💻 UI"]:::folder

    camera_hardware --> camera
    camera --> object
    camera --> UI

    hardware --> hardware_validate
    hardware_validate --> hardware
    hardware_validate --> UI

    hardware --> session_start
    session_start --> hardware
    camera_hardware --> session_start
    session_start --> object
    session_start --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

---

> 🌀 [`blue-sbc`](https://github.com/kamangir/blue-sbc) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-sbc/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-sbc/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-sbc/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-sbc/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-sbc/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-sbc/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-sbc.svg)](https://pypi.org/project/bluer-sbc/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-sbc)](https://pypistats.org/packages/bluer-sbc)

built by 🌀 [`bluer_options-5.32.1`](https://github.com/kamangir/awesome-bash-cli), based on 🌀 [`bluer_sbc-8.2.1`](https://github.com/kamangir/bluer-sbc).


