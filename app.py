from flask import Flask
from flask import render_template
from integrar import *

app = Flask(__name__)

@app.route('/', methods=["POST","GET","DELETE"])
def inicio():
    return render_template('sitio/index.html',sp=Soluciondeprimal, vo=Valoroptimo, vd= Valoresdelasvariablesduales,pa=A, pb=b, pc=c)


@app.route('/egg')
def egg():
    return render_template('sitio/egg.html')

if __name__ == '__main__':
    app.run(debug=True)
    