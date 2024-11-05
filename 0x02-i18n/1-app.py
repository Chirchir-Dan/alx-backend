#!/usr/bin/env python3
"""
1-app module
This module defines a Flask application with Babel configuration
for localization.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class config:
    """
    configuration class for Babel settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(config)
babel = Babel(app)

@app.route('/')
def index():
    """
    Renders the index page with a welcome message.
    """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run()
