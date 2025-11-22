## 🚀 Características Básicas de Express

Crear Servidores → app.listen()
Permite iniciar un servidor HTTP de forma sencilla.

Enrutamiento → app.get(), app.post(), app.put(), app.delete()
Maneja rutas según el método HTTP.

Router Modular → express.Router()
Permite dividir rutas en módulos para organizar mejor el proyecto.

Middleware → app.use()
Funciones que procesan las solicitudes antes de llegar a la ruta final (autenticación, logs, manejo de errores, parsing, etc.)

Body Parsing → express.json(), express.urlencoded()
Permite leer datos enviados en el cuerpo de una petición (JSON, formularios).

Servir Archivos Estáticos → express.static()
Para servir imágenes, CSS, JS y otros archivos estáticos fácilmente.

Motores de Plantillas (Views) → app.set('view engine', ...)
Soporta EJS, Pug, Handlebars, etc., para renderizar HTML dinámico.

Manejo de Parámetros → req.params, req.query, req.body
Permite acceder a información enviada por el usuario en URL, query strings o body.

Manejo de Errores → Middlewares de error
Control centralizado de errores usando funciones con 4 parámetros (err, req, res, next).

Compatibilidad con JSON / APIs REST
Ideal para crear APIs modernas, ligeras y rápidas.

Integración con Bases de Datos
Fácil integración con MongoDB, MySQL, PostgreSQL, SQLite u ORMs como Sequelize o Prisma.

Ecosistema Amplio de Paquetes
Miles de middlewares listos para usar: morgan, cors, helmet, cookie-parser, etc.