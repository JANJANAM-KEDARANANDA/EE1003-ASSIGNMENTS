#include <Arduino.h>

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH); // Turn LED on
    delay(1000);                     // Wait 1 second
    digitalWrite(LED_BUILTIN, LOW);  // Turn LED off
    delay(5000);                     // Wait 1 second
}

