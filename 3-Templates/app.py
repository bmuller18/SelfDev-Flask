from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hola Mundo"

@app.route('/mostrar')
def mostrar():
    return render_template("mostrar.html")

if __name__ == '__main__':
    app.run(debug=True)