firstf();
let dataroot;

function gogene() {
    let cs = document.getElementById("cs").value.toString();
    let sg = document.getElementById("sg").value;
    sg = (sg * 10).toString();
    let tp = document.getElementById("tp").value.toString();

    let stsend = cs + sg + 's' + tp;

    axios.get('/gene/' + stsend)
        .then((res) => {
            getjsonf(stsend);
        });
}

function firstf() {
    document.getElementById("geneb").addEventListener("click", gogene);

    axios.get('/environment').then(
        (res) => {
            dataroot=res.data.mconfig.dataroot;
            let classAtr = document.getElementById("geneb").getAttribute("class");
            let newClass = classAtr.replace("pure-button-disabled", "");
            document.getElementById("geneb").setAttribute("class", newClass);
        }
    )
}

function getjsonf(sendname) {
    axios.get('/'+dataroot+'/json/' + sendname+'.json').then((res)=>{
        drawf(res.data,"main1","main2")
    })
}

function drawf(dataa, id1, id2) {
    titlee = dataa.config.allpeople.toString() + '   ' + dataa.config.centerscore.toString();
    let myChart1 = echarts.init(document.getElementById(id1));
    let option1 = {
        backgroundColor: 'white',
        tooltip: {
            trigger: 'axis'
        },
        title: {
            show: true,
            text: titlee,
            x: 'center'
        },
        xAxis: {
            name: 'real',
            type: 'category',
            data: dataa.peoplescore.score
        },
        yAxis: {
            name: 'people',
            type: 'value'
        },
        series: [{
            data: dataa.peoplescore.people,
            type: 'line',
            smooth: true
        }]
    };
    myChart1.setOption(option1);

    let myChart2 = echarts.init(document.getElementById(id2));
    let option2 = {
        backgroundColor: 'white',
        tooltip: {
            trigger: 'axis'
        },
        title: {
            show: true,
            text: titlee,
            x: 'center'
        },
        xAxis: {
            name: 'real',
            type: 'category',
            data: dataa.scorefufen.score
        },
        yAxis: {
            name: 'finalpoint',
            type: 'value'
        },
        series: [{
            data: dataa.scorefufen.fufen,
            type: 'line',
            smooth: true
        }]
    };
    myChart2.setOption(option2);
}
