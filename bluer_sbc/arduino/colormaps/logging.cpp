// version 2.1.1

#include "logging.h"

#include <stdarg.h>

bool verbose = true;

void log(const char *format, ...)
{
    if (!verbose)
        return;

    char buffer[80];

    va_list args;
    va_start(args, format);
    vsnprintf(buffer, sizeof(buffer), format, args);
    va_end(args);

    Serial.println(buffer);
}