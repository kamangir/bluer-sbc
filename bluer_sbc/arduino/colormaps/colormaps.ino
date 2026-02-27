// version 3.1.1

#include "logging.h"
#include "config.h"
#include "gpio.h"
#include "colormap_update.h"

void setup()
{
    Serial.begin(9600);
    // loadConfig();
    InitGPIO();
}

void loop()
{
    digitalWrite(ledPin, HIGH);

    // updateConfig();
    updateColormap();

    digitalWrite(ledPin, LOW);
    delay(delay_time);
}
