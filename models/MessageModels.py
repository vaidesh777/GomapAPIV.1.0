from sqlalchemy import Column, Integer, String

from GomapAPI.database import Base


class Message(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    device = Column(String)
    groups = Column(String)
    message_id = Column(Integer)
    message = Column(String)
    images = Column(String)
    schedule = Column(Integer)
    status = Column(Integer)
    created= Column(Integer)