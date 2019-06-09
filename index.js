const express = require('express');
const app = express();
const servjs = require('./injs/servjs');
const mconfig=require('./mconfig');

app.use('/cdn', express.static('./cdn'));
app.use('/datas', express.static('./datas'));
app.use('/data', express.static('./data'));
app.use('/pages',express.static('./pages'));
app.use('/front', express.static('./front'));

app.get('/', function (req, res) {
    res.redirect('/pages/main.html');
});

app.get('/favicon.ico', function (req, res) {
    res.sendFile(__dirname+'/favicon.ico');
})

app.get('/gene/:confi',function(req,res){
    //console.log('gene');
    mainpr=servjs.childpycmd(req.params.confi);
    mainpr.then(
        ()=>{
            res.end("1");
        }
    )
    //console.log(req.params.confi);
})

app.get('/environment',(req,res)=>{
    res.json({"stat":"1","mconfig":{"dataroot":mconfig.dataroot}});
})

app.listen(3000);