from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
#import bmp280
import BME280        #importing BME280 library
import ssd1306       #importing OLED library

#i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
oled=ssd1306.SSD1306_I2C(128,32,i2c)

while True:
  oled.fill(0)
  bme = BME280.BME280(i2c=i2c)          #BME280 object created
  temperature = str(bme.temperature)          #reading the value of temperature
  humidity = str(bme.humidity)                      #reading the value of humidity
  pressure = str(bme.pressure)                   #reading the value of pressure

  print('Temperature is: ', temperature)    #printing BME280 values
  print('Humidity is: ', humidity)
  print('Pressure is: ', pressure)
  oled.text("Temp. "+temperature, 0, 0)
  oled.text("AP "+pressure, 0, 20)
  oled.text("Hum. "+humidity, 0,40)
  oled.show()                          #display pix
  sleep(10)           #delay of 10s
