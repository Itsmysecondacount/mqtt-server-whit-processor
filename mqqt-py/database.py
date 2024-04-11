from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey, DateTime, Sequence

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:PASSWORD@IP:3410/IOT_DATABASE"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ValoresMQTTTemperatura(Base):
    __tablename__ = 'VALORES_MQTT_TEMPERATURA'
    
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    fecha = Column(DateTime)
    topico = Column(String(255))
    valor = Column(String(255))
    atributo1 = Column(String(255))
    atributo2 = Column(String(255))