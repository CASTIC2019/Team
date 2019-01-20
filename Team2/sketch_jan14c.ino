#include <Servo.h>

Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
Servo servo_6;

void setup()
{
  Serial.begin(9600);
  servo_2.attach(2);
  servo_3.attach(3);
  servo_4.attach(4); 
  servo_5.attach(5);
  servo_6.attach(6);
}

void loop()
{
  if (Serial.read() == 'a') {
    servo_2.write(30);
    delay(1000);
    servo_2.write(60);
    delay(1000);

  }
  if (Serial.read() == 'b') {
    servo_3.write(30);
    delay(1000);
    servo_3.write(60);
    delay(1000);

  }
  if (Serial.read() == 'c') {
    servo_4.write(30);
    delay(1000);
    servo_4.write(30);
    delay(1000);

  }
  if (Serial.read() == 'd') {
    servo_5.write(30);
    delay(1000);
    servo_5.write(60);
    delay(1000);

  }
  if (Serial.read() == 'e') {
    servo_6.write(30);
    delay(1000);
    servo_6.write(60);
    delay(1000);

  }

}
