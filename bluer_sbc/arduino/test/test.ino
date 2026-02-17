const int ledPin = 13;   // L LED is on pin 13
const int inputPin = 2;  // D2
const int outputPin = 3; // D3

const char *revision = "1.1.1";

void setup()
{
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT_PULLUP); // set D2 as input
    pinMode(outputPin, OUTPUT);      // set D3 as output
}

void loop()
{
    const int delay_time = 50;

    digitalWrite(ledPin, HIGH);
    delay(delay_time);

    int state = digitalRead(inputPin);
    digitalWrite(outputPin, 1 - state);

    digitalWrite(ledPin, LOW);
    delay(delay_time);
}
