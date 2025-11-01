# Clase SQL

## Que es SQL?

SQL (Structured Query Language) es un lenguaje de programación 
utilizado para gestionar y manipular bases de datos relacionales.
SQL permite realizar operaciones como crear, leer, actualizar y eliminar
datos en una base de datos.
SQL es un lenguaje declarativo, lo que significa que se centra en
describir qué se quiere hacer con los datos, en lugar de cómo hacerlo.
SQL es un lenguaje estándar utilizado por muchos sistemas de gestión
de bases de datos, como MySQL, PostgreSQL, Oracle y Microsoft SQL Server o SQLite.

## Que es SQLite?

SQLite es un sistema de gestión de bases de datos relacional, ligero y
autónomo. Es una biblioteca escrita en C que proporciona una base de datos
SQL integrada. SQLite es ampliamente utilizado debido a su simplicidad,
portabilidad y facilidad de uso. No requiere un servidor separado para
funcionar, lo que lo hace ideal para aplicaciones pequeñas y medianas,
así como para aplicaciones móviles y de escritorio. SQLite almacena
todos los datos en un solo archivo, lo que facilita la gestión y
distribución de la base de datos. Además, es compatible con la mayoría
de los estándares SQL, lo que permite realizar consultas y operaciones
de bases de datos de manera similar a otros sistemas de gestión de bases
de datos más grandes.

## Bases de datos

1. Base de datos relacional
2. Base de datos no relacional

## Bases de datos relacionales

### Componentes principales de bases de datos relacionales

1. Tablas
2. Filas
3. Columnas
4. Claves primarias
5. Claves foráneas
6. Índices

### Entidades

1. Entidades
2. Tipos de entidades
3. Relaciones entre entidades
4. Tipos de relaciones entre entidades


## Tipos de entidades 

1. Entidad: Es un objeto o concepto que tiene una existencia independiente

2. Atributo: Es una propiedad o característica de una entidad

3. Relación: Es una asociación entre dos o más entidades

4. ERD - Entity Relationship Diagram

Un diagrama de entidad-relación (ERD) es una representación gráfica de
las entidades y sus relaciones en una base de datos. Se utiliza para
diseñar y visualizar la estructura de una base de datos.

Notacion de chen: Utiliza rectángulos para representar entidades, óvalos para atributos y rombos para relaciones.

Un ERD consta de tres componentes principales:

Entidades: Representadas por rectángulos, son los objetos o conceptos
que se desean almacenar en la base de datos. Cada entidad tiene un
nombre y una serie de atributos.

Atributos: Representados por óvalos, son las propiedades o
características de una entidad. Cada atributo tiene un nombre y un
tipo de dato. Existen diferentes tipos de atributos, como atributos simples, compuestos, derivados y multivaluados.

Relaciones: Representadas por rombos, son las asociaciones entre
entidades. Las relaciones pueden ser de uno a uno, uno a muchos o
muchos a muchos.

## Tipos de relaciones entre entidades

1. Uno a uno (1:1): Cada entidad A se relaciona con una sola entidad B,
y cada entidad B se relaciona con una sola entidad A. Ejemplo: Un
empleado tiene un único número de seguro social.

2. Uno a muchos (1:N): Cada entidad A se relaciona con varias entidades
B, pero cada entidad B se relaciona con una sola entidad A. Ejemplo:
Un autor puede tener varios libros, pero cada libro tiene un solo autor.

3. Muchos a uno (N:1): Cada entidad B se relaciona con varias entidades
A, pero cada entidad A se relaciona con una sola entidad B. Ejemplo:
Varios libros pueden pertenecer a una sola editorial, pero cada
editorial puede tener varios libros.

4. Muchos a muchos (N:M): Cada entidad A se relaciona con varias
entidades B, y cada entidad B se relaciona con varias entidades A.
Ejemplo: Un estudiante puede estar inscrito en varios cursos, y
cada curso puede tener varios estudiantes.


## Bases de datos relacionales

Una base de datos relacional es un tipo de base de datos que
organiza los datos en tablas, donde cada tabla representa una entidad
y cada fila de la tabla representa una instancia de esa entidad.
Las columnas de la tabla representan los atributos de la entidad.


## Mapeo de entidades a tablas

Entidad = Tabla
Atributo = Columna
Instancia/Objeto = Fila
