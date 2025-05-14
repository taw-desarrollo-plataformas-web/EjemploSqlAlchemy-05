from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    deporte = Column(String)
    fundacion = Column(Integer, nullable=False)

    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundacion=%d" % (
                          self.nombre,
                          self.deporte,
                          self.fundacion)

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String)
    club_id = Column(Integer, ForeignKey('club.id'))
    club  = relationship("Club", back_populates="jugadores")

    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)

Club.jugadores = relationship("Jugador", \
        back_populates="club")


class Logro(Base):
    __tablename__ = 'logro_jugador'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    anio = Column(Integer)
    jugador_id = Column(Integer, ForeignKey('jugador.id'))
    jugador  = relationship("Jugador", back_populates="logros")

    def __repr__(self):
        return "Logro: %s - año: %d" % (self.descripcion, self.anio)

Jugador.logros = relationship("Logro", \
        back_populates="jugador")

Base.metadata.create_all(engine)
