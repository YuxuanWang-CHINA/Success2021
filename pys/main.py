import numpy
import scipy.stats
import matplotlib.pyplot as plt
import json


def genes(_fmu, _fsigma,  _setall, _rmn,_seed):
    numpy.random.seed(_seed)
    s = numpy.random.normal(_fmu, _fsigma,20000000)
    r = plt.hist(s, bins=100, density=1)
    x = r[1]
    y = scipy.stats.norm.pdf(x, _fmu, _fsigma)

    nx = x.tolist()
    ny = y.tolist()
    
    #round x
    for i in range(len(nx)):
        nx[i]=round(nx[i])

    #make it 0-100
    nnx = []
    nny = []
    for i in range(len(nx)):
        if (nx[i]>0 and nx[i]<101):
            nnx.append(nx[i])
            nny.append(ny[i])

    #make it unique
    nnnx =[]
    nnny=[]
    uniq = 0
    for i in range(len(nnx)):
        if nnx[i]!=uniq:
            nnnx.append(nnx[i])
            nnny.append(nny[i])
            uniq=nnx[i]

    #create a
    realall=0
    for i in range(len(nnnx)):
        realall=realall+nnny[i]
    genea=round(_setall/realall)

    #y*a
    for i in range(len(nnnx)):
        nnny[i]=round(nnny[i]*genea)

    rex=[]
    rey=[]
    for i in range(len(nnnx)):
        if nnny[i]>_rmn:
            rex.append(nnnx[i])
            rey.append(nnny[i])

    allp = 0
    for i in range(len(rex)):
        allp=allp+rey[i]

    plt.close()
    opis = {"centerscore":_fmu,"fsigma": _fsigma,"allpeople":allp,"cutscore": _rmn}
    return [rex, rey, allp, opis]


def writej(_x, _y, _posi, _config, _fufen):
    wrj = {'config': _config, "peoplescore":{"score":_x,"people":_y},"scorefufen":{"fufen":_fufen,"score":_x}}
    jsObj = json.dumps(wrj)
    fileObject = open(_posi, 'w')
    fileObject.write(jsObj)
    fileObject.close()


def drawj(_x, _y, _posi, _allp,_cent):
    plt.title(str(_allp)+'   '+str(_cent))
    plt.plot(numpy.array(_x), numpy.array(_y), 'r-')
    plt.savefig(_posi)
    plt.close()
    #pltx.show()

# centerscore,sigma,allpeople,cutscore,json-location,png1,png2
def starts(_fmu, _fsigma, _setall, _rmn,_seed, _jsonpo, _pngpo,_pngpo2):
    genere = genes(_fmu, _fsigma, _setall, _rmn,_seed)
    rx = genere[0]
    ry = genere[1]
    allp = genere[2]
    opis = genere[3]
    rere = devided(rx, ry, allp)
    fufen=fuf(ry,rere[0],rere[1])
    writej(rx, ry, _jsonpo, opis,fufen)
    drawj(rx, ry, _pngpo, allp,_fmu)
    drawj(rx, fufen, _pngpo2, allp,_fmu)


def fuf(_y,_stan,_fen):
    re=[]
    fsfs=[30,40,55,70,85,100]
    i=0
    while i<5:
        for sco in _stan[i]:
            lows=fsfs[i]
            highs=fsfs[i+1]
            rlow=_fen[i]
            rhign=_fen[i+1]
            fufenscore=((sco*highs)-(highs*rlow)+(lows*rhign)-(lows*sco))/(rhign-rlow)
            fufenscore=round(fufenscore)
            re.append(fufenscore)
        i=i+1
    return re

def devided(_x, _y, _allp):
    standa = [round(_allp*0.02), round(_allp*0.15),
              round(_allp*0.5), round(_allp*0.85), _allp]

    total = 0
    nows = 0
    res = []
    rfen=[]
    rfen.append(_x[0])

    iii = 1
    while iii <= 5:
        res.append([])
        iii = iii+1

    i = 0
    while i < len(_x):
        xval = _x[i]
        yval = _y[i]
        addp = yval
        total = total+addp
        if total > standa[nows]:
            rfen.append(_x[i-1])
            nows = nows+1
            res[nows].append(xval)
        else:
            res[nows].append(xval)
        i = i+1
    rfen.append(_x[-1])
    return [res,rfen]


# starts(70, 7.1, 200000, 1,1 ,"./data.json", "./test.png","./test2.png")

def creatorr():
    mu=0
    sigma=0
    totalp=0
    cuts=1
    seedn=1
    jsonl="./datas/jsons/"
    p1l="./datas/png1/"
    p2l="./datas/png2/"

    namee=3571
    totalp=270000
    mu=58
    while mu<=92:
        sigma=4
        while sigma<=9:
            starts(mu, sigma, totalp, cuts,seedn ,str(jsonl+str(namee)+".json"), str(p1l+str(namee)+".png"),str(p2l+str(namee)+".png"))
            namee=namee+1
            sigma=sigma+0.1
        mu=mu+1

# creatorr()

#1785
#3570