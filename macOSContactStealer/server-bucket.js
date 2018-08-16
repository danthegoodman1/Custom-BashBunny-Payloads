const express = require('express');
const Multer = require('multer');
const app = express();
const Storage = require('@google-cloud/storage');
const storage = Storage({  
    projectId: 'freetier-213422',
    keyFilename: './creds.json'
  });
const bucket = storage.bucket("freetierupload");
const bodyParser = require('body-parser');
const format = require('util').format;

const multer = Multer({
    storage: Multer.memoryStorage(),
    limits: {
      fileSize: 5 * 1024 * 1024 * 1024 // 5gb
    }
});

app.get('/', (req, res) => {
    console.log("get")
    res.send("get")
})

app.post('/', multer.single('contact'), function(req, res){

    if (!req.file) {
        res.status(400).send('No file uploaded.');
        return;
    }
    let funtime = req.file
    const blob = bucket.file(`${funtime.originalname}`);
    const blobStream = blob.createWriteStream();
    blobStream.on('error', (err) => {
        console.log(err)
    });
    blobStream.on('finish', () => {
        console.log("uploaded a file");
    });
    blobStream.end(funtime.buffer);
    res.status(200).send("uploaded!");


});

app.listen(8080, () => {
    console.log(`App listening on port 8080`);
    console.log("Press Ctrl+C to quit.");
});
