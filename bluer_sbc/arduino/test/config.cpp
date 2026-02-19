#include "config.h"

Config cfg;

void saveConfig()
{
  EEPROM.put(0, cfg);

  // TODO: log
}

void loadConfig()
{
  EEPROM.get(0, cfg);

  if (cfg.version != 1)
  {
    cfg.version = 1;
    cfg.last_save_ms = 0;
    saveConfig();
  }
}

void updateConfig()
{
  if (millis() - cfg.last_save_ms > 600000UL) // 10 min
  {
    cfg.last_save_ms = millis();
    saveConfig();
  }
}