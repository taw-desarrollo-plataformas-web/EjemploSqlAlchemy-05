# EjemploSqlAlchemy
* Las clases del presente ejemplo de la script genera_tablas.py, permite generar una base de datos con el siguiente modelo entidad relación
![er_diagram](https://github.com/user-attachments/assets/d6e9c874-3cfb-48c2-ae49-c7dcc570a74d)

### Ejecución

**IMPORTANTE**: para poder ejecutar el siguiente ejemplo, se debe instalar python y las librerías: sqlalchemy y pymysql. Se las puede instalar con pip.

#### Opción 1 (usar la base de datos sqlite)
1. Borrar el archivo base001.bd

2. Ejecutar el script genera_tablas.py (desde el terminal o algún IDE)

* Revisar las entidades generadas en la base de datos sqlite


3. Ejecutar el script genera_datos.py

* Revisar los datos generados en la entidades de la base de datos sqlite

4. Ejecutar los scripts consulta_datos_01.py, consulta_datos_02.py ... consulta_datos_05.py

-----
#### Opción 2 (usar mysql con docker)

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
5. Ejecutar el script genera_tablas.py (desde el terminal o algún IDE)

* Revisar las entidades generadas en la base de datos mysql

6. Ejecutar el script genera_datos.py

* Revisar los datos generados en las entidades de la base de datos mysql

7. Ejecutar los scripts consulta_datos_01.py, consulta_datos_02.py ... consulta_datos_05.py
8. Dar de baja la instancia de mysql
```
docker compose down
```
