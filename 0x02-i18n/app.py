#!/usr/bin/env python3
"""Entry point for flask application"""
import locale
from datetime import datetime
from typing import Dict, Union

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Flask application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets the user's default locale"""

    loc = request.args.get('locale')
    if loc and loc in app.config['LANGUAGES']:
        return loc

    if g.user:
        loc = g.user["locale"]
        if loc and loc in app.config['LANGUAGES']:
            return loc

    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Gets the user's default timezone"""

    tzone = request.args.get('timezone')
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


# babel.init_app(
#     app, locale_selector=get_locale,
#     timezone_selector=get_timezone
# )


def get_user() -> Union[Dict, None]:
    """Gets a user from database

    Returns:
        Union[Dict, None]: user object or None
    """

    id = request.args.get('login_as')
    if id is None:
        return None
    return users.get(int(id))


@app.before_request
def before_request() -> None:
    """
    Gets the signed in user
    """
    user = get_user()
    g.user = user
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Entry point for flask application"""

    return render_template('index.html', user=g.user)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
