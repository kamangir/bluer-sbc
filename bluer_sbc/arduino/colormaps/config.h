#ifndef CONFIG_H
#define CONFIG_H

#include <Arduino.h>
#include <EEPROM.h>

struct Config
{
    uint16_t version;
    uint32_t last_save_ms;
};

extern Config cfg;

void saveConfig();
void loadConfig();
void updateConfig();

extern unsigned long delay_time;

#endif
