int switchState = 1;
void setup() 
  {
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(2, INPUT);
  
}

void loop() 
  {
    switchState = digitalRead (2);
    if (switchState == HIGH) {
      digitalWrite (3, HIGH);
      digitalWrite (4, LOW);
      digitalWrite (3, LOW);
    }
      else{
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, HIGH);
        delay(1000);
        digitalWrite(4, HIGH);
        digitalWrite(5, LOW);
        delay(1000);

      }

}
