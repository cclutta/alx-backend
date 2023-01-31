#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Config class. """
    LANGUAGES = ["en", "fr"]

    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def hello():
    """ Simply outputs template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
