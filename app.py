from flask import Flask, render_template
from itertools import islice
from data import *

app = Flask(__name__)


@app.route('/')
def main():     # страница открывается
    output = render_template('index.html', tours=dict(islice(tours.items(), 6)))
    return output


@app.route('/departures/<departure>/')
def dep(departure):      # страница открывается
    prompt_departure = departures[departure]
    filtered_tours = {
        key: value for key, value in tours.items() if value["departure"] == departure   # генератор
    }
    output = render_template('departure.html', departure=prompt_departure, tours=filtered_tours)
    return output


@app.route('/tours/<tour_id>/')
def tour_id(tour_id):     # страница открывается
    current_tour = tours[int(tour_id)]
    return render_template("tour.html", current_tour=current_tour)


@app.errorhandler(404)
def render_not_found(error):    # работает
    return "<h1>Ничего не нашлось! Вот неудача, отправляйтесь на главную!</h1>"


@app.errorhandler(500)
def render_server_error(error):     # работает
    return "<h1>Что-то не так, но мы все починим</h1>"


if __name__ == '__main__':
    app.run()




