from datetime import date, datetime

from sqlalchemy import Column, Integer


from database import Base


class packagehistory(Base):
    __tablename__ = 'packagehistory'
    id = Column(Integer, primary_key=True, index=True)
    builder_id = Column(Integer)
    package_id = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)
    price = Column(Integer)


