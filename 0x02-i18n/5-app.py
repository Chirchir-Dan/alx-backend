#!/usr/bin/env python3
"""
5-app module
This module defines a Flask application with Babel configuration
for localization and user emulation.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    If a 'locale' argument is provided in the request, it takes precedence.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id is not None and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Executes before each request to set the user.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Renders the index page with a welcome message.
    """
    if g.user:
        welcome_message = _("You are logged in as %(username)s.") % {
                'username': g.user['name']}
    else:
        welcome_message = _("You are not logged in.")

    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
