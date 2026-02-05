int led1 = 2;
int led2 = 3;
int led3 = 4;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char data = Serial.read();

    // Turn all LEDs OFF first
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);

    // Turn ON based on received data
    if (data == '0') {
      digitalWrite(led1, HIGH);
    }
    else if (data == '1') {
      digitalWrite(led2, HIGH);
    }
    else if (data == '2') {
      digitalWrite(led3, HIGH);
    }
  }
}
