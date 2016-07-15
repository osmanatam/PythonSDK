import ivencloud
import Adafruit_DHT


acr = ivencloud.activate_device("Cloud Secret Key", "Device UID")
print acr.iven_code

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

data = {
 'temperature': temperature,
 'humidity': humidity
}
response = ivencloud.send_data(data)
print response.iven_code
