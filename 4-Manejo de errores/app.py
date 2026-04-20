from flask import Flask, render_template, request, url_for, abort

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return abort(404)

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)