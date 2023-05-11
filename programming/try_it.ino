
int RightMotor_E_pin = 5;      // 오른쪽 모터의 Enable & PWM
int LeftMotor_E_pin = 6;       // 왼쪽 모터의 Enable & PWM
int RightMotor_1_pin = 8;      // 오른쪽 모터 제어선 IN1
int RightMotor_2_pin = 9;      // 오른쪽 모터 제어선 IN2
int LeftMotor_3_pin = 10;      // 왼쪽 모터 제어선 IN3
int LeftMotor_4_pin = 11;      // 왼쪽 모터 제어선 IN4

#define L_Line A3  // 왼쪽 라인트레이서 센서는 A1 핀에 연결

#define C_Line A4  // 가운데 라인트레이서 센서는 A3 핀에 연결

#define R_Line A5  // 오른쪽 라인트레이서 센서는 A5 핀에 연결

int Rmotor_dir = 1;
int Lmotor_dir = 1;
int motor_s = 1400;     // 모터 속도

volatile unsigned char sen_data=0x00;

void setup() {
  Serial.begin(9600); 
 
  pinMode(RightMotor_E_pin, OUTPUT);
  pinMode(LeftMotor_E_pin, OUTPUT);
  pinMode(RightMotor_1_pin, OUTPUT);
  pinMode(RightMotor_2_pin, OUTPUT);
  pinMode(LeftMotor_3_pin, OUTPUT);
  pinMode(LeftMotor_4_pin, OUTPUT);

  // 라인트레이서 센서는 입력으로 설정
  pinMode(L_Line, INPUT);
  pinMode(C_Line, INPUT);
  pinMode(R_Line, INPUT);

}

void loop() {
  int L = digitalRead(L_Line);
  int C = digitalRead(C_Line);
  int R = digitalRead(R_Line);
// 기호와 능력에 따라 센서의 수는 5개까지 추가 가능함. 이미 작성된 코드를 분석하여 적절히 활용할수 있음.
  if(L==HIGH)sen_data|=0x04;
  else sen_data&=~0x04;
  if(C==HIGH)sen_data|=0x02;
  else sen_data&=~0x02;
  if(R==HIGH)sen_data|=0x01;
  else sen_data&=~0x01;



// sen_data 정보로 이전에 수업때 사용했던 모터제어 함수를 설계/활용 해야함.
//Hint: sen_data에 따른 조건문으로 motor_role함수 활용
//      모터제어함수: motor_role(R_motor,L_motor);

  if sen_data|=0x04
    motor_role(0,100);
  else if sen_data|=0x01
    motor_role(100,0);
  else
    motor_role(1000,1000);
}


void motor_role(int R_motor, int L_motor) {
  if (R_motor > 0) {   // 우측 모터 정회전
    digitalWrite(RightMotor_1_pin, Rmotor_dir);
    digitalWrite(RightMotor_2_pin, !Rmotor_dir);
  }
  else if (R_motor < 0) { // 우측 모터 역회전
    digitalWrite(RightMotor_1_pin, !Rmotor_dir);
    digitalWrite(RightMotor_2_pin, Rmotor_dir);
  }
  else {               // 우측 모터 정지
    digitalWrite(RightMotor_1_pin, LOW);
    digitalWrite(RightMotor_2_pin, LOW);
  }
  if (L_motor > 0) {   // 좌측 모터 정회전
    digitalWrite(LeftMotor_3_pin, Lmotor_dir);
    digitalWrite(LeftMotor_4_pin, !Lmotor_dir);
  }
  else if (L_motor < 0) { // 좌측 모터 역회전
    digitalWrite(LeftMotor_3_pin, !Lmotor_dir);
    digitalWrite(LeftMotor_4_pin, Lmotor_dir);
  }
  else {               // 좌측 모터 정지
    digitalWrite(LeftMotor_3_pin, LOW);
    digitalWrite(LeftMotor_4_pin, LOW);
  }
  analogWrite(RightMotor_E_pin, abs(R_motor));  // 우측 모터 속도값
  analogWrite(LeftMotor_E_pin, abs(L_motor));   // 좌측 모터 속도값
}
