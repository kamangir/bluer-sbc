#include "colormap_update.h"

#include "colormap_rainbow.h"
#include "colormap_vars.h"
#include "gpio.h"
#include "logging.h"

int value;
const int value_step = 10;
int direction = 1;

void updateColormap()
{
    int max_value = analogRead(analogPin); // 0–1023

    value += direction * value_step;
    if (direction == 1 && value > max_value)
    {
        value = max_value;
        direction = -1;
    }
    if (direction == -1 && value < 0)
    {
        value = 0;
        direction = 1;
    }

    int state = 1 - digitalRead(inputPin);
    digitalWrite(outputPin, state);

    int value_to_show = value;
    if (state == 1)
    {
        value_to_show = max_value;
    }
    setColormapRainbow(value_to_show);

    log("value:%d, max_value:%d, r:%d, g:%d, b:%d", value, max_value, r, g, b);
}