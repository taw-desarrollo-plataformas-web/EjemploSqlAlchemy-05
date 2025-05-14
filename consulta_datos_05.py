from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador, Logro

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener los logros de los jugadores, que tengan logros

jugadores = session.query(Jugador).all()

print("Consulta 1: Obtener los logros de los jugadores, que tengan logros ")
for e in jugadores:
    if len(e.logros)>0:
        print(e)
        for l in e.logros:
            print(f"    {l}")

print("############################################")
# Obtener los clubs en función del año de los logros de los jugadores
print("Consulta 2: Obtener los clubs en función del año de los logros de los jugadores ")
clubs = session.query(Club).join(Jugador).join(Logro).filter(or_(Logro.anio=="2012", Logro.anio=="2020")).all()


for c in clubs:
    print(c)

print("############################################")

# Obtener los logros de los jugadores que pertenecen a un club específico
print("Consulta 3: Obtener los logros de los jugadores que pertenecen a un club específico")

logros = session.query(Logro).join(Jugador).join(Club).filter(Club.nombre=="Barcelona").all()

for l in logros:
    print(l)
print("############################################")
