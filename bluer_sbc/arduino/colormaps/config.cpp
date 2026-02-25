#include "config.h"

#include "logging.h"

Config cfg;

void saveConfig()
{
  EEPROM.put(1, cfg);

  log("saveConfig: version=%d, last_save_ms=%lu", cfg.version, cfg.last_save_ms);
}

void loadConfig()
{
  EEPROM.get(1, cfg);

  if (cfg.version != 1)
  {
    log("bad config: version=%d", cfg.version);
    cfg.version = 1;
    cfg.last_save_ms = 0;
    saveConfig();
  }

  log("loadConfig: version=%d, last_save_ms=%lu", cfg.version, cfg.last_save_ms);
}

void updateConfig()
{
  if (millis() - cfg.last_save_ms > 6000UL) // 10 min
  {
    cfg.last_save_ms = millis();
    saveConfig();
  }
}