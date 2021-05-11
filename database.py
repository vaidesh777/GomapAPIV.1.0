from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker

#username = "root"  # database Username
#password = "" # database password
#host = "@localhost"   # database Host
#port = "3306"     # database Port
#db_name = "gomap_whatsapp" # database Nmae

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" + username + ":" + password + host + ":/" + db_name
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://admin:40ea713569aad7d225ae2bafef198d2fbebc29297810cff5@143.110.242.84:3306/gomap"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
