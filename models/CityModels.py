from sqlalchemy import Column, Integer, String

from database import Base


class CityModel(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    string = Column(String, nullable=False)