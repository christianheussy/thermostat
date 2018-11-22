import RPi.GPIO as GPIO
import time


class Relay:
    def __init__(self, channel=17):
        self.channel = channel
        self.status = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)

    def set_high(self):
        GPIO.output(self.channel, GPIO.HIGH)
        self.status = True

    def set_low(self):
        GPIO.output(self.channel, GPIO.LOW)
        self.status = False

    def cleanup(self):
        GPIO.output(self.channel, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':

    my_relay = Relay()

    for i in range(10):
        my_relay.set_high()
        time.sleep(.25)
        my_relay.set_low()
        time.sleep(.25)

    my_relay.cleanup()
