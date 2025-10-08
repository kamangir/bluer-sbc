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
| [`HC-SR04: ultrasonic-sensor`](./parts/ultrasonic-sensor.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/HC-SR04.jpg?raw=true)](./parts/ultrasonic-sensor.md) 4 x | [`LED, ~2 V forward voltage, 10-20 mA`](./parts/LED.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/led.png?raw=true)](./parts/LED.md) green + red + yellow + 4 x blue | [`Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110`](./parts/Polyfuse.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/polyfuse.png?raw=true)](./parts/Polyfuse.md) optional | [`Raspberry Pi 3B+`](./parts/rpi3bp.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/rpi3bplus.png?raw=true)](./parts/rpi3bp.md)  | [`Raspberry Pi Camera, V1.3https://www.raspberrypi.com/documentation/accessories/camera.html`](./parts/rpi-camera.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/rpi-camera.jpg?raw=true)](./parts/rpi-camera.md)  | [`Resistor, 1/4 watt, 5% tolerance`](./parts/resistor.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/resistor.png?raw=true)](./parts/resistor.md) 7 x 330-470 Ω + N x 2.2 kΩ + N x 3.3 kΩ | [`TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package`](./parts/TVS-diode.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/TVSdiode.png?raw=true)](./parts/TVS-diode.md)  | [`XL4015: 12 VDC -> 5 VDC, 4A`](./parts/XL4015.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/XL4015.png?raw=true)](./parts/XL4015.md)  | [`auto power connectors`](./parts/connector.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/connector.jpg?raw=true)](./parts/connector.md) 3 pairs | [`capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.`](./parts/470-mF.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/capacitor.png?raw=true)](./parts/470-mF.md)  |
| [`double-sided PCB, 9 cm x 7 cm`](./parts/PCB-double-9x7.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/PCB-double-9x7.jpeg?raw=true)](./parts/PCB-double-9x7.md) 2 x | [`push button`](./parts/pushbutton.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/pushbutton.png?raw=true)](./parts/pushbutton.md)  | [`single-sided PCB, 14 cm x 9.5 cm`](./parts/PCB-single-14x9_5.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/pcb-14x9_5cm.jpg?raw=true)](./parts/PCB-single-14x9_5.md) 2 x |  |  |  |  |  |  |  |

1. [HC-SR04: ultrasonic-sensor: 4 x](./parts/ultrasonic-sensor.md).
1. [LED, ~2 V forward voltage, 10-20 mA: green + red + yellow + 4 x blue](./parts/LED.md).
1. [Polyfuse, 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110: optional](./parts/Polyfuse.md).
1. [Raspberry Pi 3B+](./parts/rpi3bp.md).
1. [Raspberry Pi Camera, V1.3https://www.raspberrypi.com/documentation/accessories/camera.html](./parts/rpi-camera.md).
1. [Resistor, 1/4 watt, 5% tolerance: 7 x 330-470 Ω + N x 2.2 kΩ + N x 3.3 kΩ](./parts/resistor.md).
1. [TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package](./parts/TVS-diode.md).
1. [XL4015: 12 VDC -> 5 VDC, 4A](./parts/XL4015.md).
1. [auto power connectors: 3 pairs](./parts/connector.md).
1. [capacitor, 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.](./parts/470-mF.md).
1. [double-sided PCB, 9 cm x 7 cm: 2 x](./parts/PCB-double-9x7.md).
1. [push button](./parts/pushbutton.md).
1. [single-sided PCB, 14 cm x 9.5 cm: 2 x](./parts/PCB-single-14x9_5.md).
