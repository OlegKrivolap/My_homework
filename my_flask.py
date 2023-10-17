from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница')

@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')

@app.route('/flask')
def flask():
    return render_template('flask.html', title='Про фласк')

@app.route('/picture')
def picture():
    return render_template('picture.html', title='Картиночка')

if __name__ == '__main__':
    app.run(debug=True)