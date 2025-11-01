# Principales comandos y tipos de datos en SQL

SQL (Structured Query Language) es un lenguaje de programación
utilizado para gestionar y manipular bases de datos relacionales.

## Comandos principales de SQL

1. Crear base de datos
   ```sql
   CREATE DATABASE nombre_base_de_datos;
   ```
2. SELECT: Se utiliza para consultar y recuperar datos de una o más tablas en una base de datos.
   Ejemplo:
   ```sql
   SELECT nombre, edad FROM estudiantes;
   ```
3. INSERT: Se utiliza para insertar nuevos registros en una tabla.
    Ejemplo:
   ```sql
   INSERT INTO estudiantes (nombre, edad) VALUES ('Juan', 20);
   ```
4. UPDATE: Se utiliza para modificar registros existentes en una tabla.
   Ejemplo:
   ```sql
   UPDATE estudiantes SET edad = 21 WHERE nombre = 'Juan';
   ```
5. DELETE: Se utiliza para eliminar registros de una tabla.
   Ejemplo:
   ```sql
   DELETE FROM estudiantes WHERE nombre = 'Juan';
   ```
6. CREATE TABLE: Se utiliza para crear una nueva tabla en la base de datos.
   Ejemplo:
   ```sql
   CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER);
   ```
7. ALTER TABLE: Se utiliza para modificar la estructura de una tabla existente, como agregar o eliminar columnas.
   Ejemplo:
   ```sql
   ALTER TABLE estudiantes ADD COLUMN direccion TEXT;
   ```
8. CREATE TABLE WITH RELATIONSHIP: Se utiliza para crear una nueva tabla con una relación a otra tabla mediante una clave foránea.
   Ejemplo:
   ```sql
   CREATE TABLE cursos (
       id INTEGER PRIMARY KEY,
       nombre TEXT,
       estudiante_id INTEGER,
       FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
   );
   ```
9. DROP TABLE: Se utiliza para eliminar una tabla de la base de datos.
   Ejemplo:
   ```sql
   DROP TABLE estudiantes;
   ```
10. DROP DATABASE: Se utiliza para eliminar una base de datos completa.
   Ejemplo:
   ```sql
   DROP DATABASE escuela;
   ```

## Tipos de datos comunes en SQL

1. INTEGER: Se utiliza para almacenar números enteros.
2. REAL: Se utiliza para almacenar números de punto flotante.
3. TEXT: Se utiliza para almacenar cadenas de texto.
4. BLOB: Se utiliza para almacenar datos binarios, como imágenes o archivos.
5. DATE: Se utiliza para almacenar fechas en formato AAAA-MM-DD.
6. BOOLEAN: Se utiliza para almacenar valores booleanos (TRUE o FALSE).

Estos comandos y tipos de datos son fundamentales para trabajar con bases de datos SQL y permiten realizar una amplia variedad de operaciones para gestionar y manipular los datos almacenados.

## Relaciones entre tablas

En una base de datos relacional, las tablas pueden estar relacionadas entre sí mediante claves primarias y claves foráneas. Estas relaciones permiten establecer conexiones entre los datos almacenados en diferentes tablas.

1. Clave primaria (Primary Key): Es un atributo o conjunto de atributos que identifica de manera única cada registro en una tabla.

2. Clave foránea (Foreign Key): Es un atributo o conjunto de atributos en una tabla que hace referencia a la clave primaria de otra tabla, estableciendo una relación entre ambas tablas.

Por ejemplo, en una base de datos de una escuela, podríamos tener dos tablas: "Estudiantes" y "Cursos". La tabla "Estudiantes" podría tener una clave primaria llamada "estudiante_id", y la tabla "Cursos" podría tener una clave foránea llamada "estudiante_id" que hace referencia a la clave primaria de la tabla "Estudiantes". Esto permitiría establecer una relación entre los estudiantes y los cursos que están inscritos, donde un estudiante puede estar inscrito en varios cursos y cada curso puede tener varios estudiantes.

