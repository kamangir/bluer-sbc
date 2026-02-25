#include "gpio.h"

void InitGPIO()
{
    pinMode(ledPin, OUTPUT);

    pinMode(inputPin, INPUT_PULLUP); // set D2 as input
    pinMode(outputPin, OUTPUT);      // set D3 as output

    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}