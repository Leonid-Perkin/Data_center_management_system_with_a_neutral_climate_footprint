#include <ArduinoJson.h>
DynamicJsonDocument doc(2048);


#define MIN_OUTDOOR_TEMP -35
#define MAX_OUTDOOR_TEMP 20
#define sensor_pin A0

int outdoor_temp;
int heat_pump_external_temp;
int heat_pump_internal_temp;
int termal_unit_external_temp;
int termal_unit_internal_temp;

int ext_int_diff;

bool heating_flag;
bool cooler_on_flag;
void setup() {
  Serial.begin(9600);
  pinMode(sensor_pin, INPUT);
  doc["otdoor_temp"] = outdoor_temp;
  doc["heat_pump_internal_temp"] = heat_pump_internal_temp;
  doc["heat_pump_external_temp"] = heat_pump_external_temp;
  doc["termal_unit_external_temp"] = termal_unit_external_temp;
  doc["termal_unit_internal_temp"] = termal_unit_internal_temp;
  doc["heating_flag"] = heating_flag;
  doc["cooler_on_flag"] = cooler_on_flag;
  char buffer[100];
}

void loop() {
  outdoor_temp = map(analogRead(sensor_pin), 0, 1023, MIN_OUTDOOR_TEMP, MAX_OUTDOOR_TEMP);
  ext_int_diff = map(outdoor_temp, MIN_OUTDOOR_TEMP, 8, 15, 5);
  if(outdoor_temp == -35){
    termal_unit_external_temp = 95;
    heating_flag = true;
  }
  if(outdoor_temp == -30){
    termal_unit_external_temp = 89;
    heating_flag = true;
  }
  if(outdoor_temp == -25){
    termal_unit_external_temp = 84;
    heating_flag = true;
  }
  if(outdoor_temp == -20){
    termal_unit_external_temp = 78;
    heating_flag = true;
  }
  if(outdoor_temp == -15){
    termal_unit_external_temp = 72;
    heating_flag = true;
  }
  if(outdoor_temp == -10){
    termal_unit_external_temp = 65;
    heating_flag = true;
  }
  if(outdoor_temp == -5){
    termal_unit_external_temp = 59;
    heating_flag = true;
  }
  if(outdoor_temp == 0){
    termal_unit_external_temp = 52;
    heating_flag = true;
  }
  if(outdoor_temp == 8){
    termal_unit_external_temp = 41;
    heating_flag = true;
  }

  if(outdoor_temp >= 10){
    heating_flag = false;
  }
  termal_unit_internal_temp = termal_unit_external_temp - 10;
  heat_pump_internal_temp = 40;
  heat_pump_external_temp = heat_pump_internal_temp - ext_int_diff;

  if(heat_pump_external_temp > 33){
    cooler_on_flag = true;
  }
  else{
    cooler_on_flag = false;
  }
  doc["otdoor_temp"] = outdoor_temp;
  doc["heat_pump_internal_temp"] = heat_pump_internal_temp;
  doc["heat_pump_external_temp"] = heat_pump_external_temp;
  doc["termal_unit_external_temp"] = termal_unit_external_temp;
  doc["termal_unit_internal_temp"] = termal_unit_internal_temp;
  doc["heating_flag"] = heating_flag;
  doc["cooler_on_flag"] = cooler_on_flag;
  

  Serial.print(outdoor_temp);
  Serial.print(", ");
  Serial.print(heat_pump_internal_temp);
  Serial.print(", ");
  Serial.print(heat_pump_external_temp);
  Serial.print(", ");
  Serial.print(termal_unit_external_temp);
  Serial.print(", ");
  Serial.print(termal_unit_internal_temp);
  Serial.print(", ");
  Serial.print(heating_flag);
  Serial.print(", ");
  Serial.println(cooler_on_flag);
  delay(1000);
}
