#include <WiFi.h>
#include <HTTPClient.h>
 
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
}
 
void loop() {
  if ((WiFi.status() == WL_CONNECTED)) { 
    HTTPClient http;
 
    http.begin("http://1ba3-35-193-131-231.ngrok.io/");
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
