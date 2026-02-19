#include "colormap_rainbow.h"

#include "gpio.h"

void setColormapRainbow(int value)
{
    value = constrain(value, 0, 1023);

    // Map 0–1023 → 0–1535 (6 regions × 256)
    int scaled = map(value, 0, 1023, 0, 1535);

    int region = scaled / 256; // which color region (0–5)
    int offset = scaled % 256; // position within region (0–255)

    r = 0, g = 0, b = 0;

    switch (region)
    {
    case 0:
        r = 255;
        g = offset;
        b = 0;
        break; // Red → Yellow
    case 1:
        r = 255 - offset;
        g = 255;
        b = 0;
        break; // Yellow → Green
    case 2:
        r = 0;
        g = 255;
        b = offset;
        break; // Green → Cyan
    case 3:
        r = 0;
        g = 255 - offset;
        b = 255;
        break; // Cyan → Blue
    case 4:
        r = offset;
        g = 0;
        b = 255;
        break; // Blue → Magenta
    case 5:
        r = 255;
        g = 0;
        b = 255 - offset;
        break; // Magenta → Red
    }

    analogWrite(redPin, r);
    analogWrite(greenPin, g);
    analogWrite(bluePin, b);
}