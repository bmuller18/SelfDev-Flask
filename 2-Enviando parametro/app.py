from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'<H2>Hola {nombre} desde Flask</H2>/n <p>Este es un parrafo</p> /n <a href="/">Volver a la pagina principal</a>'


if __name__ == '__main__':
    app.run(debug=True)