from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'<H2>Hola {nombre} desde Flask</H2>/n <p>Este es un parrafo</p> /n <a href="/">Volver a la pagina principal</a>'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'<H2>Tu edad es {edad}</H2>'
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f'<H2>La suma de {num1} y {num2} es {num1 + num2}</H2>'

if __name__ == '__main__':
    app.run(debug=True)