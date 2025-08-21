# Impor
from flask import Flask, render_template


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman kedua
@app.route('/1')
def ultah_nakei():
    return render_template(
                            'greatingcard.html',
                           )

# Halaman ketiga
@app.route('/2')
def electronics():
    return render_template(
                            'kue_ultah.html',               
                           )

app.run(debug=True)
