const char *revision = "2.2.1";

#include "logging.h"
#include "config.h"
#include "gpio.h"

bool led_pin_state = true;

void setup()
{
    delay_time = 500;
    Serial.begin(9600);
    InitGPIO();
}

void loop()
{

    analogWrite(greenPin, 0);

    if (led_pin_state)
    {
        digitalWrite(ledPin, HIGH);
        analogWrite(redPin, 255);
        analogWrite(bluePin, 0);
    }
    else
    {
        digitalWrite(ledPin, LOW);
        analogWrite(redPin, 0);
        analogWrite(bluePin, 255);
    }
    led_pin_state = not led_pin_state;

    delay(delay_time);
}
