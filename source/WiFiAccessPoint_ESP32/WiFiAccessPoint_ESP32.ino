#include <WiFi.h>

// Set these to your desired credentials.
const char *ssid = "canine_guard_AP";
const char *password = "yourPassword";

// Specify the static IP address you want for the ESP32 AP, along with the gateway and subnet mask.
IPAddress local_IP(192, 168, 1, 1);
IPAddress gateway(192, 168, 1, 1); // Typically, the gateway is the same as the AP IP for small networks
IPAddress subnet(255, 255, 255, 0);

void setup() {
  Serial.begin(115200);
  Serial.println("Setting up Access Point...");

  // Configure the ESP32 WiFi AP with the static IP address
  if(!WiFi.softAPConfig(local_IP, gateway, subnet)) {
    Serial.println("STA Failed to configure");
  }

  // Start the ESP32 WiFi AP
  if(!WiFi.softAP(ssid, password)) {
    Serial.println("Soft AP creation failed.");
    while (1); // If AP creation fails, halt the program
  } else {
    // If the AP is successfully created, print the static IP
    Serial.print("AP IP address: ");
    Serial.println(local_IP);
  }
}

void loop() {
  // Nothing to do here
}
