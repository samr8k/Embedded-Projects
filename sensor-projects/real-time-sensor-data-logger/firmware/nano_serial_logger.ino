// Real-Time Sensor Data Logger
// Arduino Nano

const int sensorPin = A0;
unsigned long lastSend = 0;
const unsigned long interval = 100; // milliseconds

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (millis() - lastSend >= interval) {
    lastSend = millis();

    int rawValue = analogRead(sensorPin);
    float voltage = rawValue * (5.0 / 1023.0);

    // Send data in CSV format
    Serial.print(rawValue);
    Serial.print(",");
    Serial.println(voltage);
  }
}
