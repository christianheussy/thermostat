import threading


class AppState:

    """
    AppState object is a thread safe object used to indicate the operating mode of the application.
    This object can be used by the flask application and the controller thread to indicate the users
    desired operating state.
    """

    def __init__(self):
        self.auto_mode = True
        self.heat_on = None
        self._state_lock = threading.Lock()

    def set_auto(self):
        with self._state_lock:
            self.auto_mode = True

    def set_manual_on(self):
        with self._state_lock:
            self.auto_mode = False
            self.heat_on = True

    def set_manual_off(self):
        with self._state_lock:
            self.auto_mode = False
            self.heat_on = False