// version 2.1.1

#ifndef GPIO_H
#define GPIO_H

#include <Arduino.h>

constexpr uint8_t analogPin = A7;

constexpr uint8_t inputPin = 2;
constexpr uint8_t outputPin = 3;

constexpr uint8_t redPin = 5;
constexpr uint8_t greenPin = 9;
constexpr uint8_t bluePin = 6;

constexpr uint8_t ledPin = 13;

void InitGPIO();

#endif
