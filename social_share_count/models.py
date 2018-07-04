import datetime
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String
from social_share_count.database import Base

##
# Models go here, they get mapped to your database automagically.
##

class Metrique(Base):
    __tablename__ = 'metric'
    id = Column(Integer, primary_key=True)
    taken = sa.DateTime(timezone=False)
    service = Column(String(50))
    url = Column(String(512))
    value = Column(Integer)

    def __init__(self, service, url, value):
        self.taken = datetime.datetime.utcnow()
        self.service = service
        self.url = url
        self.value = value

    def __repr__(self):
        return '<Metric of website {} at {} of type {}. Value: {}>'.format(self.url, self.taken, self.service, self.value)
