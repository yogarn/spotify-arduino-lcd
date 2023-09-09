#include <LiquidCrystal.h>
LiquidCrystal lcd(2, 3, 4, 5, 6, 7); // assign lcd pin

void setup() {
  lcd.begin(16, 2); // set up 16x2 lcd screen
  Serial.begin(9600); // initialize serial
}

void loop() {
  // check if there's input from serial
  if (Serial.available()) {
    lcd.clear(); // clear lcd screen
    lcd.setCursor(0, 0);  // set lcd cursor to upper left
    String song_name = Serial.readString();  //read song name
    song_name.trim(); // remove any whitespace
    lcd.print(song_name); // print song name to lcd screen
    delay(100); // give a time for python file to send another serial input
    lcd.setCursor(0, 1); // set lcd cursor to the next line
    String artist_name = Serial.readString(); // read artist name
    artist_name.trim(); // remove any whitespace
    lcd.print(artist_name);  // print artist name
  }
}
