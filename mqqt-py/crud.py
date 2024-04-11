from sqlalchemy.orm import Session
import database

def insert_data_temperature(session: Session, fecha, topico, valor, atributo1=None, atributo2=None):
    nuevo_valor = database.ValoresMQTTTemperatura(
        fecha=fecha,
        topico=topico,
        valor=valor,
        atributo1=atributo1,
        atributo2=atributo2
    )
    session.add(nuevo_valor)
    session.commit()
    session.refresh(nuevo_valor)
    return nuevo_valor
