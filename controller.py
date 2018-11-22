from utils import relay
from utils import sensor
import models
import threading
import time

sensor = sensor.Sensor()
relay = relay.Relay()


class Controller:
    def __init__(self, db_sesstion, state_object, low_thresh=77.5, high_thresh=80):
        self.low_thresh = low_thresh
        self.high_thresh = high_thresh
        self.state_object = state_object
        self.temp = None
        self.humidity = None
        self.session = db_sesstion()

    def write_data(self):
        """This method writes timestamp, sensor date, and control state to database every cycle"""
        row_entry = models.TempData(
            temp=self.temp,
            humidity=self.humidity,
            auto_mode=self.state_object.auto_mode,
            relay_state=relay.status
        )
        self.session.add(row_entry)
        self.session.commit()

    def main_loop(self, period):
        while True:
            self.temp, self.humidity = sensor.get_data()

            if self.state_object.auto_mode:  # app is in auto mode
                if self.temp < self.low_thresh:
                    relay.set_high()
                    
                elif self.temp > self.high_thresh:
                    relay.set_low()
            else:  # app is in manual mode
                if self.state_object.heat_on != relay.status:
                    if self.state_object.heat_on:
                        relay.set_high()
                    else:
                        relay.set_low()

            print('Temp:{} Relay Status:{}'.format(self.temp, relay.status))
            
            self.write_data()

            # time.sleep(period)

    def start_controller(self, daemon=True, period=1):
        """This method starts a thread"""
        t = threading.Thread(target=self.main_loop, args=[period])
        if daemon:
            t.daemon = True
        t.start()
