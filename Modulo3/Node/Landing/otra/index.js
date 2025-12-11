const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const bullBoard = require("./lib/bullboard");
const routes = require("./routes");
const { scheduleProductSync } = require("./jobs/schedulers.js");
const { Server } = require("socket.io"); // 👈 nuevo

const app = express();
const port = 9000;

app.use(express.json());
app.use(cors());
app.use(morgan("dev"));
app.use("/admin/queues", bullBoard.getRouter());
app.use("/api", routes);

// Servir archivos estáticos (para chat.html)
app.use(express.static("public"));

if (process.env.CRON_SYNC === "true") {
  console.log("Scheduling product sync job every 26 minutes.");
  scheduleProductSync();
}

// 👉 1) Guardamos el server que devuelve app.listen
const server = app.listen(port, () => {
  console.log("App is listening in port: " + port);
});

// 👉 2) Creamos instancia de Socket.IO sobre ese server
const io = new Server(server, {
  cors: {
    origin: "*", // en prod limita a tu dominio
    methods: ["GET", "POST"],
  },
});

// 👉 3) Lógica básica de chat grupal
const messages = []; // [{ username, message, timestamp }]

io.on("connection", (socket) => {
  console.log("🟢 Cliente conectado:", socket.id);

  // Enviar últimas 20 al nuevo
  socket.emit("chat:history", messages.slice(-20));

  // Cliente se "presenta" con un nombre
  socket.on("chat:join", (username) => {
    socket.data.username = username || "Anon";
    console.log(`👤 ${socket.data.username} se unió (${socket.id})`);

    socket.broadcast.emit("chat:system", {
      message: `${socket.data.username} se unió al chat`,
    });
  });

  // Mensaje normal de chat
  socket.on("chat:message", (text) => {
    const username = socket.data.username || "Anon";
    const msg = {
      username,
      message: text,
      timestamp: new Date().toISOString(),
    };

    messages.push(msg);
    io.emit("chat:message", msg); // broadcast a todos
  });

  socket.on("disconnect", () => {
    const username = socket.data.username || "Anon";
    console.log("🔴 Cliente desconectado:", socket.id);
    socket.broadcast.emit("chat:system", {
      message: `${username} salió del chat`,
    });
  });
});
