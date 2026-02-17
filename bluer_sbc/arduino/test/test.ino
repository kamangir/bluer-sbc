const char *revision = "1.3.1";

const bool verbose = 1;

char buffer[50];

const int analogPin = A7;

const int inputPin = 2;
const int outputPin = 3;

const int redPin = 5;
const int greenPin = 6;
const int bluePin = 9;

const int ledPin = 13;

const int delay_time = 10;

int max_value;
int value;
int direction = 1;

uint8_t r;
uint8_t g;
uint8_t b;

void setup()
{
    Serial.begin(9600);

    pinMode(ledPin, OUTPUT);

    pinMode(inputPin, INPUT_PULLUP); // set D2 as input
    pinMode(outputPin, OUTPUT);      // set D3 as output

    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}

void setColor_basic(uint16_t value)
{
    value &= 0x03FF; // ensure 10-bit input (0–1023)
    value <<= 2;     // shift left 2 bits → now 12-bit

    // Extract 4-bit chunks
    uint8_t r4 = (value >> 8) & 0x0F; // top 4 bits
    uint8_t g4 = (value >> 4) & 0x0F; // middle 4 bits
    uint8_t b4 = value & 0x0F;        // lowest 4 bits

    // Scale 4-bit (0–15) → 8-bit (0–240 approx)
    r = r4 << 4;
    g = g4 << 4;
    b = b4 << 4;

    analogWrite(redPin, r);
    analogWrite(greenPin, g);
    analogWrite(bluePin, b);
}

void setColor_rainbow(int value)
{
    value = constrain(value, 0, 1023);

    // Map 0–1023 → 0–1535 (6 regions × 256)
    int scaled = map(value, 0, 1023, 0, 1535);

    int region = scaled / 256; // which color region (0–5)
    int offset = scaled % 256; // position within region (0–255)

    r = 0, g = 0, b = 0;

    switch (region)
    {
    case 0:
        r = 255;
        g = offset;
        b = 0;
        break; // Red → Yellow
    case 1:
        r = 255 - offset;
        g = 255;
        b = 0;
        break; // Yellow → Green
    case 2:
        r = 0;
        g = 255;
        b = offset;
        break; // Green → Cyan
    case 3:
        r = 0;
        g = 255 - offset;
        b = 255;
        break; // Cyan → Blue
    case 4:
        r = offset;
        g = 0;
        b = 255;
        break; // Blue → Magenta
    case 5:
        r = 255;
        g = 0;
        b = 255 - offset;
        break; // Magenta → Red
    }

    analogWrite(redPin, r);
    analogWrite(greenPin, g);
    analogWrite(bluePin, b);
}

void log()
{
    if (verbose)
    {
        sprintf(buffer, "value=%d/%d -> r=%d, g=%d, b=%d", value, max_value, r, g, b);
        Serial.println(buffer);
    }
}

void loop()
{
    digitalWrite(ledPin, HIGH);
    delay(delay_time);

    max_value = analogRead(analogPin); // 0–1023

    if (direction == 1)
    {
        value++;
        if (value > max_value)
        {
            value = max_value;
            direction = -1;
        }
    }
    else
    {
        value--;
        if (value < 0)
        {
            value = 1;
            direction = 1;
        }
    }

    int state = 1 - digitalRead(inputPin);
    digitalWrite(outputPin, state);

    if (state == 1)
    {
        value = max_value;
    }

    setColor_rainbow(value);

    log();

    digitalWrite(ledPin, LOW);
    delay(delay_time);
}
