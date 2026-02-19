#include "colormap_basic.h"

#include "gpio.h"

void setColormapBasic(uint16_t value)
{
    value &= 0x03FF; // ensure 10-bit input (0–1023)
    value <<= 2;     // shift left 2 bits → now 12-bit

    // Extract 4-bit chunks
    uint8_t r4 = (value >> 8) & 0x0F; // top 4 bits
    uint8_t g4 = (value >> 4) & 0x0F; // middle 4 bits
    uint8_t b4 = value & 0x0F;        // lowest 4 bits

    // Scale 4-bit (0–15) → 8-bit (0–240 approx)
    r = r4 << 4;
    g = g4 << 4;
    b = b4 << 4;

    analogWrite(redPin, r);
    analogWrite(greenPin, g);
    analogWrite(bluePin, b);
}
