#include "gpio.h"

void InitGPIO()
{
    pinMode(ledPin, OUTPUT);

    pinMode(inputPin, INPUT_PULLUP);
    pinMode(outputPin, OUTPUT);

    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}