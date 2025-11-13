# EjemploSqlAlchemy
* Las clases del presente ejemplo de la script genera_tablas.py, permite generar una base de datos con el siguiente modelo entidad relación
![er_diagram](https://github.com/user-attachments/assets/d6e9c874-3cfb-48c2-ae49-c7dcc570a74d)

### Ejecución

**IMPORTANTE**: para poder ejecutar el siguiente ejemplo, se debe instalar python y las librerías: sqlalchemy y pymysql. Se las puede instalar con pip.

#### Opción 1 (usar la base de datos sqlite)
1. Borrar el archivo base001.bd

2. Ejecutar el script genera_tablas.py (desde el terminal o algún IDE)

* Revisar las entidades generadas en la base de datos sqlite
<img width="778" height="533" alt="image" src="https://github.com/user-attachments/assets/e2334fac-25fb-40c7-af5a-7aae2a9da616" />


3. Ejecutar el script genera_datos.py

* Revisar los datos generados en la entidades de la base de datos sqlite
<img width="778" height="533" alt="image" src="https://github.com/user-attachments/assets/85ba7a6e-ce83-42e9-92c1-24a99153b566" />


4. Ejecutar los scripts consulta_datos_01.py, consulta_datos_02.py ... consulta_datos_05.py

<img width="626" height="404" alt="image" src="https://github.com/user-attachments/assets/0e01645f-43d3-4e5a-aaf6-06557be61d71" />


-----
#### Opción 2 (usar mysql con docker)

* Para esta opción se debe instalar Docker en el sistema operativo

1. Cambiar el nombre del archivo configuracion.py a configuracion.py.sqlite
2. Cambiar el nombre del archivo configuracion.py.bd a configuracion.py
3. Levantar el contenedor de mysql, a través de docker-compose, usar el siguiente comando desde el terminal.
```
docker compose up -d
```
4. Verificar el acceso a la base de datos y revisar las entidades en la base de datos miapp
```
docker exec -it mysql8 mysql -umiusuario -p
```
<img width="1205" height="472" alt="image" src="https://github.com/user-attachments/assets/6afca994-0b08-4434-bf52-657874a10163" />

5. Ejecutar el script genera_tablas.py (desde el terminal o algún IDE)

* Revisar las entidades generadas en la base de datos mysql

<img width="477" height="287" alt="image" src="https://github.com/user-attachments/assets/3fd5586b-6e30-44f1-95e0-f72016e05767" />


6. Ejecutar el script genera_datos.py

* Revisar los datos generados en las entidades de la base de datos mysql

<img width="703" height="304" alt="image" src="https://github.com/user-attachments/assets/649d90df-80d2-4f4f-a997-72945a5dc312" />


7. Ejecutar los scripts consulta_datos_01.py, consulta_datos_02.py ... consulta_datos_05.py
8. Dar de baja la instancia de mysql
```
docker compose down
```
