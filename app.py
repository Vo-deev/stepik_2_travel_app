from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():     # страница открывается
    output = render_template('index.html')
    return output


@app.route('/departures/<departure>/')
def dep(departure):      # страница открывается
    output = render_template('departure.html', departure=departure)
    return output


@app.route('/tours/<id>/')
def tour(id):     # страница открывается
    output = render_template('tour.html', id=id)
    return output

@app.errorhandler(404)
def render_not_found(error):    # работает
    return "<h1>Ничего не нашлось! Вот неудача, отправляйтесь на главную!</h1>"


@app.errorhandler(500)
def render_server_error(error):     # работает
    return "<h1>Что-то не так, но мы все починим</h1>"


if __name__ == '__main__':
    app.run()
