const express = require("express");
const multer = require("multer");
const app = express();
const bodyParser = require("body-parser");

const upload = multer({ dest: "uploads/" });

let runPy = function runPy(imageOne, imageTwo) {
  return new Promise(function(success, nosuccess) {
    const { spawn } = require("child_process");
    const pyprog = spawn("python", ["./lib/similiar.py", imageOne, imageTwo]);

    pyprog.stdout.on("data", function(data) {
      success(data);
    });
    pyprog.stderr.on("data", data => {
      nosuccess(data);
    });
  });
};

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/upload", upload.array("images"), function(req, res, next) {
  console.log(req.files);
  if (!req.files) {
    console.log("No file uploaded");
    return res.send({
      success: false
    });
  }
  runPy(req.files[0].path + ".jpg", req.files[1].path + ".jpg").then(function(
    fromRunpy
  ) {
    console.log(fromRunpy.toString());
    res.send({
      success: true
    });
  });
});

app.listen(8080, () => console.log("ZeebeeIR listening on port 4000!"));
