# swallow-head

- head of [swallow computer](./swallow.md), without the DC motor drivers.
- used for [swallow design](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/swallow) backs and [rangin](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/rangin) tops.

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/01.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/01.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/02.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/02.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/03.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/03.jpg?raw=true) |
| [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/04.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/04.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/05.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/05.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/06.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/swallow/design/head-v1/06.jpg?raw=true) |

## parts

|   |   |   |   |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`16 AWG wire`](./parts/16-awg-wire.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/16-awg-wire.jpeg?raw=true)](./parts/16-awg-wire.md) 40 cm x (red + black/blue) | [`HC-SR04: ultrasonic-sensor`](./parts/ultrasonic-sensor.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/HC-SR04.jpg?raw=true)](./parts/ultrasonic-sensor.md) 4 x | [`LED, ~2 V forward voltage, 10-20 mA`](./parts/LED.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/led.png?raw=true)](./parts/LED.md) green + red + yellow + 4 x blue | [`Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110`](./parts/Polyfuse.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/polyfuse.png?raw=true)](./parts/Polyfuse.md) optional | [`Raspberry Pi 3B+`](./parts/rpi3bp.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/rpi3bplus.png?raw=true)](./parts/rpi3bp.md)  | [`Raspberry Pi Camera, V1.3https://www.raspberrypi.com/documentation/accessories/camera.html`](./parts/rpi-camera.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/rpi-camera.jpg?raw=true)](./parts/rpi-camera.md)  | [`Resistor, 1/4 watt, 5% tolerance`](./parts/resistor.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/resistor.png?raw=true)](./parts/resistor.md) 7 x 330-470 Ω + N x 2.2 kΩ + N x 3.3 kΩ | [`TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package`](./parts/TVS-diode.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/TVSdiode.png?raw=true)](./parts/TVS-diode.md)  | [`XL4015: 12 VDC -> 5 VDC, 4A`](./parts/XL4015.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/XL4015.png?raw=true)](./parts/XL4015.md)  | [`auto power connectors`](./parts/connector.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/connector.jpg?raw=true)](./parts/connector.md) 1 female |
| [`capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.`](./parts/470-mF.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/capacitor.png?raw=true)](./parts/470-mF.md)  | [`double-sided PCB, 9 cm x 7 cm`](./parts/PCB-double-9x7.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/PCB-double-9x7.jpeg?raw=true)](./parts/PCB-double-9x7.md) 2 x | [`dupont cables, female to female`](./parts/dupont-cables.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/dupont-cables.jpg?raw=true)](./parts/dupont-cables.md) 1 x 30 cm + 1 x 10 cm | [`nuts, bolts, and spacers`](./parts/nuts-bolts-spacers.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/nuts-bolts-spacers.jpg?raw=true)](./parts/nuts-bolts-spacers.md) M2: (2 x bolt + 2 x 5 mm + 4 x nut) + M2.5: (4 x bolt + 8 x 10 mm + 4 x nut) + M3: (1 x bolt + 3 x 35 mm + 3 x 25 mm + 7 x 15 mm + 4 x 5 mm + 5 x nut) | [`pin headers`](./parts/pin-headers.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/pin-headers.jpg?raw=true)](./parts/pin-headers.md) 1 x (female, 2 x 40 -> 2 x 20) + 1 x (male, 2 x 40 -> 4 x 6 + 4 x 2 + 2 x 20) | [`plexiglass, 2 mm or 2.5 mm thickness`](./parts/plexiglass.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/plexiglass.jpg?raw=true)](./parts/plexiglass.md) 14 cm x 9.5 cm | [`push button`](./parts/pushbutton.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/pushbutton.png?raw=true)](./parts/pushbutton.md)  | [`single-sided PCB, 14 cm x 9.5 cm`](./parts/PCB-single-14x9_5.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/pcb-14x9_5cm.jpg?raw=true)](./parts/PCB-single-14x9_5.md) 2 x | [`solid cable 1-1.5 mm^2`](./parts/solid-cable-1-15.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/solid-cable-1-15.jpg?raw=true)](./parts/solid-cable-1-15.md) 10 cm x (red + black/blue) | [`strong thread`](./parts/strong-thread.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/strong-thread.jpg?raw=true)](./parts/strong-thread.md) 1 m |
| [`white terminal`](./parts/white-terminal.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/white-terminal.jpg?raw=true)](./parts/white-terminal.md) 2 x |  |  |  |  |  |  |  |  |  |

1. [16 AWG wire](./parts/16-awg-wire.md): 40 cm x (red + black/blue).
1. [HC-SR04: ultrasonic-sensor](./parts/ultrasonic-sensor.md): 4 x.
1. [LED, ~2 V forward voltage, 10-20 mA](./parts/LED.md): green + red + yellow + 4 x blue.
1. [Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110](./parts/Polyfuse.md): optional.
1. [Raspberry Pi 3B+](./parts/rpi3bp.md).
1. [Raspberry Pi Camera, V1.3https://www.raspberrypi.com/documentation/accessories/camera.html](./parts/rpi-camera.md).
1. [Resistor, 1/4 watt, 5% tolerance](./parts/resistor.md): 7 x 330-470 Ω + N x 2.2 kΩ + N x 3.3 kΩ.
1. [TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package](./parts/TVS-diode.md).
1. [XL4015: 12 VDC -> 5 VDC, 4A](./parts/XL4015.md).
1. [auto power connectors](./parts/connector.md): 1 female.
1. [capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.](./parts/470-mF.md).
1. [double-sided PCB, 9 cm x 7 cm](./parts/PCB-double-9x7.md): 2 x.
1. [dupont cables, female to female](./parts/dupont-cables.md): 1 x 30 cm + 1 x 10 cm.
1. [nuts, bolts, and spacers](./parts/nuts-bolts-spacers.md): M2: (2 x bolt + 2 x 5 mm + 4 x nut) + M2.5: (4 x bolt + 8 x 10 mm + 4 x nut) + M3: (1 x bolt + 3 x 35 mm + 3 x 25 mm + 7 x 15 mm + 4 x 5 mm + 5 x nut).
1. [pin headers](./parts/pin-headers.md): 1 x (female, 2 x 40 -> 2 x 20) + 1 x (male, 2 x 40 -> 4 x 6 + 4 x 2 + 2 x 20).
1. [plexiglass, 2 mm or 2.5 mm thickness](./parts/plexiglass.md): 14 cm x 9.5 cm.
1. [push button](./parts/pushbutton.md).
1. [single-sided PCB, 14 cm x 9.5 cm](./parts/PCB-single-14x9_5.md): 2 x.
1. [solid cable 1-1.5 mm^2](./parts/solid-cable-1-15.md): 10 cm x (red + black/blue).
1. [strong thread](./parts/strong-thread.md): 1 m.
1. [white terminal](./parts/white-terminal.md): 2 x.
