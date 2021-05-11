from sqlalchemy import Column, Integer, String


from GomapAPI.database import Base

class post_repeat(Base):
    __tablename__ = 'post_repeat'
    id = Column(Integer, primary_key=True, index=True)
    sch_id = Column(String)
    message = Column(int)
    images = Column(String)
    email = Column(String)
    mobile= Column(int)
    created= Column(int)


