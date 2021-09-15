#include <WiFi.h>
#include <HTTPClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 5
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
 
const char* ssid = "cookie2";
const char* password =  "0317137263";
 
void setup() {
  Serial.begin(115200);
  delay(1000);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  } 
  Serial.printf("\n got connected  ");
  Serial.print(WiFi.localIP()); 
  Serial.print(", ");
  Serial.println(WiFi.macAddress());
  sensors.begin();
}
 
void loop() {
  if ((WiFi.status() == WL_CONNECTED)) { 
    HTTPClient http;

    sensors.requestTemperatures();
    delay(1000);
    float tempC = sensors.getTempCByIndex(0);
    Serial.printf("temp=%.1f\n", tempC);
 
    http.begin("http://1ba3-35-193-131-231.ngrok.io/?temp="+String(tempC));
    int httpCode = http.GET();
 
    if (httpCode > 0) {
        String payload = http.getString();
        Serial.println(httpCode);
        Serial.println(payload);
      }
    else {
      Serial.println("Error on HTTP request");
    }
    http.end();
  }
  delay(5000);
}
