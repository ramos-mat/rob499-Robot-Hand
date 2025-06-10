#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

// LCD connected to digital GPIO pins (parallel LCD, not I2C)
const int rs = 26, en = 25, d4 = 33, d5 = 32, d6 = 35, d7 = 34;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Keypad setup
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {19, 18, 5, 4};    // Connect to R1, R2, R3, R4
byte colPins[COLS] = {15, 2, 13, 12};   // Connect to C1, C2, C3, C4
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Servo Driver (PCA9685)
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  // Default I2C addr = 0x40
#define SERVOMIN 150  // Pulse length for 0 degrees
#define SERVOMAX 600  // Pulse length for 180 degrees

// Define 9 movements with 5 servo positions each
int positions[9][5] = {
  {90, 90, 90, 90, 90},     // Position 1 – All neutral
  {45, 90, 90, 90, 90},     // Position 2 – Servo 1
  {90, 45, 90, 90, 90},     // Position 3 – Servo 2
  {90, 90, 135, 90, 90},    // Position 4 – Servo 3
  {90, 90, 90, 45, 90},     // Position 5 – Servo 4
  {90, 90, 90, 90, 135},    // Position 6 – Servo 5
  {30, 30, 150, 150, 90},   // Position 7 – combo
  {120, 60, 90, 90, 60},    // Position 8 – combo
  {45, 135, 90, 45, 135}    // Position 9 – combo
};

void setup() {
  // I2C for PCA9685 (SDA = D21, SCL = D22 on ESP32)
  Wire.begin(21, 22);
  pwm.begin();
  pwm.setPWMFreq(60);  // Recommended frequency for servos

  // LCD setup
  lcd.begin(16, 2);  // 16 columns, 2 rows
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Ready");
}

void loop() {
  char key = keypad.getKey();

  if (key && key >= '1' && key <= '9') {
    int index = key - '1';

    // Show message on LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Position ");
    lcd.print(key);

    // Move all 5 servos to position
    for (int i = 0; i < 5; i++) {
      int angle = positions[index][i];
      int pulse = map(angle, 0, 180, SERVOMIN, SERVOMAX);
      pwm.setPWM(i, 0, pulse);  // Channel, on=0, off=pulse
    }

    delay(1000); // optional pause
  }
}
