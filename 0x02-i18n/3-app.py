#!/usr/bin/env python3
"""
3-app module
This module defines a Flask application with Babel configuration
for localization and locale selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
    Configuration class for Babel settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index page with a welcome message.
    """
    return render_template(
            '3-index.html', title=_('home_title'), header=_('home_header')
            )


if __name__ == "__main__":
    app.run()
