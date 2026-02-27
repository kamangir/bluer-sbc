// version 4.1.1

constexpr uint8_t analogPin = A7;

constexpr uint8_t inputPin = 2;
constexpr uint8_t outputPin = 3;

constexpr uint8_t redPin = 5;
constexpr uint8_t greenPin = 9;
constexpr uint8_t bluePin = 6;

constexpr uint8_t ledPin = 13;

unsigned long delay_time = 500;

unsigned char led_pin_state = 0;

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

void setup()
{
    Serial.begin(9600);

    pinMode(ledPin, OUTPUT);

    pinMode(inputPin, INPUT_PULLUP);
    pinMode(outputPin, OUTPUT);

    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}

void loop()
{

    if (led_pin_state == 0)
    {
        digitalWrite(ledPin, HIGH);
        analogWrite(redPin, 0);
        analogWrite(greenPin, 255);
        analogWrite(bluePin, 0);
    }
    else if (led_pin_state == 1)
    {
        digitalWrite(ledPin, LOW);
        analogWrite(redPin, 0);
        analogWrite(greenPin, 0);
        analogWrite(bluePin, 255);
    }
    else
    {
        digitalWrite(ledPin, LOW);
        analogWrite(redPin, 255);
        analogWrite(greenPin, 0);
        analogWrite(bluePin, 0);
    }

    log("led_pin_state:%d", led_pin_state);

    led_pin_state++;
    if (led_pin_state > 2)
    {
        led_pin_state = 0;
    }

    delay(delay_time);
}
