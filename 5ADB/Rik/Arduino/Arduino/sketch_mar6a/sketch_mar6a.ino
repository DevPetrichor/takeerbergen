

#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 11, d5 = 10, d6 = 9, d7 = 8;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int redPin= 7;
int greenPin = 6;

void setup() {
  lcd.begin(16, 2); 
  pinMode(redPin,  OUTPUT);              
  pinMode(greenPin, OUTPUT);
}

void  loop() {
  lcd.clear();
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, HIGH);
  lcd.print("GROEN");
  delay(1000);
  lcd.clear();
  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, HIGH);
  lcd.print("ROOD");
  delay(1000);
  

}

