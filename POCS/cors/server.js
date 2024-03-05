const express = require("express");
const path = require("path");

const app = express();

app.get("/hack",(req,res)=>{
    res.sendFile(path.join(__dirname,'index.html'));
})


app.listen(4500,()=>{
    console.log(`server is running `)
})