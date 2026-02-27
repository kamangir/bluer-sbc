// version 2.1.1

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

constexpr unsigned long delay_time = 20;

#endif
