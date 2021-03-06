#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 5
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
  
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println();
  sensors.begin();
  Serial.println("Begin");
}
 
void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  Serial.printf("temp= %.1f\n", tempC);
}
