const exec = require('child-process-promise').exec;
const mconfig = require('../mconfig');
const fs = require('fs-extra')

function cmdd(_datas) {
    console.log(_datas)
    return new Promise((resolve, reject) => {
        //console.log('serve')

        checkj(_datas).then(() => {resolve();})
        .catch(()=>{
            deonest(_datas).then(({ mu, sigma, people, lo1, lo2, lo3 }) => {
                let query = "python ./pys/requ.py " + mu + " " + sigma + " " + people + " " + lo1 + " " + lo2 + " " + lo3;
                console.log(query);
                exec(query).then(() => {
                    console.log('Python OK');
                    resolve();
                }
                ).catch(() => { console.log("Python no"); }
                );
            })
        })
    })
}

function checkj(_datas){
    return new Promise((resolve,reject)=>{
        let root = mconfig.dataroot;
        let lo1 = root + "/json/" + _datas + ".json";
        let profs = fs.access(lo1);
        profs.then(()=>{resolve();})
        .catch(()=>{reject();})
    })
}

function deonest(_datas) {
    return new Promise((resolve, reject) => {
        let mu = _datas.substr(0, 2);
        let sigma = _datas.substr(2, 2) * 0.1;
        sigma = sigma.toFixed(1);
        let ada = _datas.split("s");
        let people = ada[1];
        let root = mconfig.dataroot;
        let lo1 = root + "/json/" + _datas + ".json";
        let lo2 = root + "/png1/" + _datas + ".png";
        let lo3 = root + "/png2/" + _datas + ".png";

        resolve({ mu, sigma, people, lo1, lo2, lo3 });
    })
}

exports.childpycmd = cmdd;
