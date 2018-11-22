import Adafruit_DHT
import time
import threading


class Sensor:
    def __init__(self):
        self.pin = 4
        self.sensor = Adafruit_DHT.DHT22

    def get_data(self):
        humidity, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temp * 9 / 5.0 + 32, humidity

    def start(self, daemon=True, period=1):
        """This method starts a thread"""
        t = threading.Thread(target=self.run, args=[1])
        if daemon:
            t.daemon = True
        t.start()

    def run(self, period):
        """This method periodically polls the sensor and writes to a DB"""
        while True:
            # temp, humidity = self.get_temp()
            print('Working')

            time.sleep(period)


if __name__ == '__main__':
    sensor = Sensor()
    sensor.start()
    time.sleep(5)