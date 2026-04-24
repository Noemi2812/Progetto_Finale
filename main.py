from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sito.html')

@app.route('/tanjiro')
def tanjiro():
    return render_template('tanjiro.html')

@app.route('/nezuko')
def nezuko():
    return render_template('nezuko.html')

@app.route('/zenitsu')
def zenitsu():
    return render_template('zenitsu.html')

@app.route('/inosuke')
def inosuke():
    return render_template('inosuke.html')

@app.route('/kanao')
def kanao():
    return render_template('kanao.html')

@app.route('/aoi')
def aoi():
    return render_template('aoi.html')

@app.route('/shinobu')
def shinobu():
    return render_template('shinobu.html')

@app.route('/tengen')
def tengen():
    return render_template('tengen.html')

@app.route('/kanae')
def kanae():
    return render_template('kanae.html')

@app.route('/mitsuri')
def mitsuri():
    return render_template('mitsuri.html')

@app.route('/kyojuro')
def kyojuro():
    return render_template('kyojuro.html')

@app.route('/giyuu')
def giyuu():
    return render_template('giyuu.html')

@app.route('/obanai')
def obanai():
    return render_template('obanai.html')

@app.route('/muichiro')
def muichiro():
    return render_template('muichiro.html')

@app.route('/sanemi')
def sanemi():
    return render_template('sanemi.html')

@app.route('/gyomei')
def gyomei():
    return render_template('gyomei.html')
