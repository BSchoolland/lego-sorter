// import a servo library
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
void setup() {

  // attach the servo object to pin 9
  myservo.attach(9);
  // set the servo to 90 degrees
  myservo.write(90);
  pinMode(13, OUTPUT);
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}

void loop() {
  // wait for serial data, then echo it
  if (Serial.available() > 0) {
    char inByte = Serial.read();
    Serial.write(inByte);
    if (inByte == '1') {
      digitalWrite(13, HIGH);

      myservo.write(120);
    } else if (inByte == '0') {
      digitalWrite(13, LOW);

      myservo.write(70);
    }
  }
}
