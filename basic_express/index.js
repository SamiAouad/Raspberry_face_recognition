const express = require("express")
const app = express()
const port = 8000
const cors = require("cors")
const path = require('path')
const multer = require("multer")

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'Images')
    },
    filename: (req, file, cb) => {
        console.log(file)
        cb(null, Date.now() +  path.extname(file.originalname))
    }
})

const upload = multer({storage: storage})


app.use(express.urlencoded({extended: true}))
app.use(express.json())
app.use(cors())

app.post('/recognize', upload.single("file"), async (req, res) => {
    res.send(req.body)
})


app.listen(port, () => {
    console.log(`listening at port: ${port}`)
})