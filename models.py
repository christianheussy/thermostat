from sqlalchemy import Column, Integer, DateTime, String, Boolean
import datetime
from database import Base


class TempData(Base):
    __tablename__ = 'tempdata'
    id = Column(Integer, primary_key=True)
    temp = Column(Integer)
    humidity = Column(Integer)
    auto_mode = Column(Boolean)
    relay_state = Column(Boolean)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, temp=None, humidity=None, auto_mode=None, relay_state=None):
        self.temp = temp
        self.humidity = humidity
        self.auto_mode = auto_mode
        self.relay_state = relay_state

    def __repr__(self):
        return '<User %r>' % (self.name)
