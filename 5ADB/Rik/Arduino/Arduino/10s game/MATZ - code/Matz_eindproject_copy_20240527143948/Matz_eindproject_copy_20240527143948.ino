#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 11, d5 = 10, d6 = 9, d7 = 8;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const int buttonPin = 0;

unsigned long startTime;
bool counting = false;
bool displayOn = true;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);

  lcd.begin(16, 2);
  lcd.print("Spel laden.");
  delay(500);
  lcd.clear();
  lcd.print("Spel laden..");
  delay(500);
  lcd.clear();
  lcd.print("Spel laden...");
  delay(500);
  lcd.clear();
  lcd.print("Druk knop om");
  lcd.setCursor(0, 1);
  lcd.print("te beginnen");
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    delay(200); 
    if (!counting) {
      counting = true;
      displayOn = true;
      startTime = millis();
      lcd.clear();
    } else {
      unsigned long stopTime = millis();
      unsigned long elapsedTime = stopTime - startTime;

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Tijd: ");
      lcd.print(elapsedTime / 1000.0, 3);
      lcd.print("s");

      Serial.print("Time: ");
      Serial.println(elapsedTime / 1000.0, 3);

      counting = false;
    }
  }

  if (counting) {
    unsigned long elapsedTime = millis() - startTime;
    if (displayOn && elapsedTime <= 4000) {
      lcd.setCursor(0, 0);
      lcd.print("Tijd: ");
      lcd.print(elapsedTime / 1000.0, 3);
      lcd.print("s");
    } else if (elapsedTime > 4000) {
      lcd.clear();
      displayOn = false;
    }
  }
}


