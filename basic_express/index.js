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

app.post('/api', upload.single("file"), async (req, res) => {
    res.send(req.body)
})

app.post('/api/devices', async (req, res) => {
    console.log(req.body.name)
    result = {
        "device": {
            "device_name": req.body.name
        },
        "admin": {
            "email": 'samiaouad7@gmail.com',
            "password": "1234"
        }
    }
    res.status(200).send(result)
})

app.post('/api/users/login', async (req, res) => {
    const {email, password} = req.body
    console.log(req.body)
    result = {
        "token": "this is a token"
    }
    if (email == 'samiaouad7@gmail.com' && password == "1234"){
        return res.json(result)
    }
    res.status(202).json({'err': "Invalid credentials"})
})

app.post('/api/nfc/login', async (req, res) => {
    console.log(req.body.id)
})


app.listen(port, () => {
    console.log(`listening at port: ${port}`)
})