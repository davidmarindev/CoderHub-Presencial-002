const express = require("express");
const cors = require("cors");
const app = express();
const port = 3030;
routes = require("./routes/index.js");
var corsOptions = {
  origin: "*",
  optionsSuccessStatus: 200,
  credentials: false,
};

// middlewares
app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/api", routes);

app.listen(port, () => {
  console.log(`API server running at http://localhost:${port}`);
});
