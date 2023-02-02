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


@babel.localeselector
def get_locale():
    """ Method to get_locale with best match """
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello():
    """ Simply outputs template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
