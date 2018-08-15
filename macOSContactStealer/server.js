const express = require('express');
const multer = require('multer');

const app = express();
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, './uploads/')
    },
    filename: function (req, file, cb) {
        cb(null, file.originalname)
    }
})
const upload = multer({ storage })

app.route('/')
.get((req, res) => {
    console.log("Get request")
    res.send("Get")
})
.post(upload.single('contact'), (req, res) => {
    console.log("Got request")
    res.send("Thanks")
})

app.listen(8080, () => {
    console.log("Listening on port 8080")
})
