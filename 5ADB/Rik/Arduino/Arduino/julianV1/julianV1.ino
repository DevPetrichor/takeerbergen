
#include <LiquidCrystal.h> //library 
#include <dht.h> //library
#define outPin 7 //outPin is op 7
dht DHT;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); //lcd isntellen
const int trigPin = 9; //trigPin is op 9
const int echoPin = 10; //echoPin is op 10
float duration, distance; //variables

void setup() { //doet 1x keer
  lcd.begin(16, 2); //Start het scherm met 16 op 2
  pinMode(trigPin, OUTPUT); //trigPin is een output
  pinMode(echoPin, INPUT); //echoPin is een input
  Serial.begin(9600); //begin Serial monitor
  }

void loop() { //blijft herhalen
	int readData = DHT.read11(outPin); //lees data uit sensor
	float t = DHT.temperature; //Zet variable
	float h = DHT.humidity; //Zet variable
  digitalWrite(trigPin, LOW); //zet trigPin op LOW
  delayMicroseconds(2); //Wacht 2 microseconden
  digitalWrite(trigPin, HIGH); //zet trigPin op HIGH
  delayMicroseconds(10); //wacht 10 microseconden
  digitalWrite(trigPin, LOW); //zet trigPin op LOW
  duration = pulseIn(echoPin, HIGH); //duration berekenen
  distance = (duration*.0343)/2; //afstand berekenen
  Serial.print("Distance: "); //print distance in serial monitor
  Serial.println(distance); //print variable distance in serial monitor
  lcd.print("Afstand:"); //print afstand op lcd
  lcd.print(distance); //print variable distance op lcd
  lcd.print(" cm"); //print cm op lcd
  lcd.setCursor(0, 1); //plaats de cursor van lcd op 2e rij
  lcd.print("Temp:"); //print temp op lcd
  lcd.print(t); //print variable t op lcd
  lcd.print( "Vocht:"); //print vocht op lcd
  lcd.print(h); //print variable h op lcd
  delay(200); //wacht 0.2 seconden
  lcd.clear(); //maak lcd leeg
}