from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')


#Página Principal
@app.route('/')
def home():
    return render_template('home.html')


#Páginas Principales
@app.route('/about')
def about():
    return render_template('sobremi.html')

@app.route('/misproyectos')
def misproyectos():
    return render_template('misproyectos.html')

@app.route('/serviciossonorosmusicales')
def serviciossonorosmusicales():
    return render_template('serviciossonorosmusicales.html')

@app.route('/trabajosrealizados')
def trabajosrealizados():
    return render_template('trabajosrealizados.html')

@app.route('/fechasafuturo')
def fechasafuturo():
    return render_template('fechasafuturo.html')


#Subpáginas Servicios Sonoros Musicales
@app.route('/sesionista')
def sesionista():
    return render_template('sesionista.html')

@app.route('/trabajosvarios')
def trabajosvarios():
    return render_template('trabajosvarios.html')

@app.route('/sonidoenestudio')
def sonidoenestudio():
    return render_template('sonidoenestudio.html')

@app.route('/sonidoenvivo')
def sonidoenvivo():
    return render_template('sonidoenvivo.html')

@app.route('/afinacionpianos')
def afinacionpianos():
    return render_template('afinacionpianos.html')


#Subpáginas de mis proyectos
@app.route('/cuartetodelacabeza')
def cuartetodelacabeza():
    return render_template('cuartetodelacabeza.html')

@app.route('/auge')
def auge():
    return render_template('auge.html')

@app.route('/guibaj')
def guibaj():
    return render_template('guibaj.html')

@app.route('/grahvitty')
def grahvitty():
    return render_template('grahvitty.html')

@app.route('/seventhroad')
def seventhroad():
    return render_template('seventhroad.html')


#Para cuando sea necesario incluir una sección en desarrollo
@app.route('/seccionendesarrollo')
def seccionendesarrollo():
    return render_template('seccionendesarrollo.html')


#Para que la aplicación esté siempre corriendo
if __name__=='__main__':
    app.run(debug=True)