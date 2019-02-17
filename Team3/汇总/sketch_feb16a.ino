#include <Servo.h>

int val='0';
Servo servo_1;

void servo1_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_1.read();
  if (move_speed >= 1000) {
      servo_1.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_1.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_1.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_1.write(target_angle);
    }
  }
}

Servo servo_2;

void servo2_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_2.read();
  if (move_speed >= 1000) {
      servo_2.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_2.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_2.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_2.write(target_angle);
    }
  }
}

Servo servo_4;

void servo4_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_4.read();
  if (move_speed >= 1000) {
      servo_4.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_4.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_4.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_4.write(target_angle);
    }
  }
}

Servo servo_6;

void servo6_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_6.read();
  if (move_speed >= 1000) {
      servo_6.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_6.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_6.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_6.write(target_angle);
    }
  }
}

Servo servo_8;

void servo8_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_8.read();
  if (move_speed >= 1000) {
      servo_8.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_8.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_8.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_8.write(target_angle);
    }
  }
}

Servo servo_10;

void servo10_move(int target_angle,int move_speed){
  int servo_angle;
  servo_angle=servo_10.read();
  if (move_speed >= 1000) {
      servo_10.write(target_angle);
  }
  else {
  if(target_angle-servo_angle>0){
    for(int a=0;a<target_angle-servo_angle;a++){
      servo_10.write(servo_angle+a);
      delay(1000/move_speed);
    }
  }
  else if(target_angle-servo_angle<0){
    for(int a=0;a<servo_angle-target_angle;a++){
      servo_10.write(servo_angle-a);
      delay(1000/move_speed);
    }
  } else {
      servo_10.write(target_angle);
    }
  }
}

void setup()
{
  
  Serial.begin(9600);
  servo_1.attach(2);

  servo_2.attach(3);

  servo_4.attach(4);

  servo_6.attach(6);

  servo_8.attach(8);

  servo_10.attach(10);

}

void loop()
{
if(Serial.available())
    val = Serial.read();

 // }
  
// Serial.println(i);  
  if (val == 'A') 
  {
     Serial.println("1");  
    servo1_move(100,16);
    servo1_move(40,16);
    delay(100);
    servo1_move(100,16);

  }
  if (val == 'B') {
     Serial.println("2");  
    servo2_move(100,16);
    servo2_move(160,16);
    delay(100);
    servo2_move(100,16);

  }
  if (val == 'C') {
    Serial.println("3");  
    servo4_move(100,16);
    servo4_move(160,16);
    delay(100);
    servo4_move(100,16);

  }
  if (val == 'D') {
    Serial.println("4");  
    servo6_move(100,16);
    servo6_move(160,16);
    delay(100);
    servo6_move(100,16);

  }
  if (val == 'E') {
    Serial.println("5");  
    servo8_move(100,16);
    servo8_move(160,16);
    delay(100);
    servo8_move(100,16);

  }
  if (val== 'F') {
    Serial.println("6");  
    servo10_move(100,16);
    servo10_move(160,16);
    delay(100);
    servo10_move(100,16);

  }

}
