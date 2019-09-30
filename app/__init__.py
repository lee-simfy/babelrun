from flask import Flask, request, Response, g, has_request_context
from flask_babel import Babel, gettext, lazy_gettext

app = Flask(__name__)
babel = Babel(app, default_locale='en_ZA')
print(list(babel.translation_directories))
print(babel.list_translations())


# @babel.localeselector
# def get_locale():
#     # return request.accept_languages.best_match(app.config['LANGUAGES'])
#     raise Exception('yolo')
#     return 'en_za'


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@app.route('/')
def index():
    print(has_request_context())
    return Response(lazy_gettext('Your pos is now live!'))
